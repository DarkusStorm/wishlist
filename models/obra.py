from sqlite3 import Cursor
from models.database import Database
from typing import Self, Any, Optional

class Obra:
    """
        Classe para representar uma obra, com métodos para salvar, obter, excluir e atualizar obras em um banco de dados usando a classe `Database`.
    """
    def __init__(self: Self, titulo_obra: Optional[str], indicacao_obra: Optional[str] = None, tipo_obra: Optional[str] = None, id_obra: Optional[int] = None) -> None:
        self.titulo_obra: Optional[str] = titulo_obra
        self.indicacao_obra: Optional[str] = indicacao_obra
        self.tipo_obra: Optional[str] = tipo_obra
        self.id_obra: Optional[int] = id_obra
        # Atributos pertencentes ao OBJETO.

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = ('SELECT titulo_obra, indicacao_obra, tipo_obra FROM obras WHERE id = ?;')
            params: tuple = (id,)
            resultado = db.buscar_tudo(query, params)
            [[titulo, indicacao, tipo]] = resultado
        return cls(id_obra=id,titulo_obra=titulo, indicacao_obra=indicacao, tipo_obra=tipo)
    
    def salvar_obra(self: Self) -> None:
        with Database() as db:
            query: str = ('INSERT INTO obras (titulo_obra, indicacao_obra, tipo_obra) VALUES (?, ?, ?);')
            params: tuple = (self.titulo_obra, self.indicacao_obra, self.tipo_obra)
            db.executar(query, params)
            # POST;

    @classmethod
    def obter_obras(cls) -> list[Self]:
        with Database() as db:
            query: str = ('SELECT titulo_obra, indicacao_obra, tipo_obra, id FROM obras;')
            resultados: list[Any] = db.buscar_tudo(query)
            obras: list[Self] = [cls(titulo, indicacao, tipo, id) for titulo, indicacao, tipo, id in resultados]
            return obras
            # GET;
    
    def atualizar_obra(self) -> Cursor:
        with Database() as db:
            query: str = ('UPDATE obras SET titulo_obra = ?, indicacao_obra = ?, tipo_obra = ? WHERE id = ?;')
            params: tuple = (self.titulo_obra, self.indicacao_obra, self.tipo_obra, self.id_obra)
            resultado: Cursor = db.executar(query, params)
            return resultado
    
    def excluir_obra(self) -> Cursor:
        with Database() as db:
            query: str = ('DELETE FROM obras WHERE id = ?;')
            params: tuple = (self.id_obra,)
            resultado: Cursor = db.executar(query, params)
            return resultado