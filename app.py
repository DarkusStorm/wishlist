from flask import Flask, render_template, request, redirect, url_for
from models.obra import Obra
from models.database import init_db

app = Flask(__name__)

init_db()

# Rotas:

@app.route('/', methods=['GET', 'POST'])
def wishlist():

    if request.method == 'POST':
        titulo_obra = request.form['titulo-obra']
        indicacao_obra = request.form['indicacao-obra']
        tipo_obra = request.form['tipo-obra']
        obra = Obra(titulo_obra, indicacao_obra, tipo_obra)
        obra.salvar_obra()

    obras_por_tipo = Obra.obter_obras_agrupadas()

    return render_template('lista.html', titulo="Lista de Desejos", obras_por_tipo=obras_por_tipo)

@app.route('/delete/<int:idObra>')
def delete(idObra):
    obra = Obra.id(idObra)
    obra.excluir_obra()
    return redirect(url_for('wishlist'))

@app.route('/update/<int:idObra>', methods=['GET', 'POST'])
def update(idObra):
    if request.method == 'POST':
        titulo = request.form['titulo-obra']
        indicacao = request.form['indicacao-obra']
        tipo = request.form['tipo-obra']
        obra = Obra(titulo, indicacao, tipo, idObra)
        obra.atualizar_obra()
        return redirect(url_for('wishlist'))
    
    obras_por_tipo = Obra.obter_obras_agrupadas()

    obra_selecionada = Obra.id(idObra)
    return render_template('lista.html', titulo=f'Editando a obra de ID: {idObra}', obras_por_tipo=obras_por_tipo, obra_selecionada=obra_selecionada)

# Comentários para não se esquecer abaixo:
 
#     Métodos HTTP:
#     POST - "posta" (cadastra/envia) as informações (CREATE);
#     GET - "pega" (recupera/obtém) as informações (READ);
#     UPDATE/PATCH - "atualizam" as informações ou parte delas (UPDATE);
#     DELETE - "apaga" as informações (DELETE);
#     — C.R.U.D. (Create, Read, Update, Delete) —

#         — Outros:
#             PUT;
#             HEAD;
#             PATCH;
#             CONNECT;
#             TRACE;
#             OPTIONS.

#     Códigos de Retorno:
#     2XX - Sucesso;
#     3XX - Sucesso, mas redirecionado;
#     4XX - Não encontrado (falha na REQUISIÇÃO);
#     5XX - Erro do servidor (falha na RESPOSTA)