from flask import Flask, render_template, request, redirect, url_for
from models.obra import Obra
from models.database import init_db

app = Flask(__name__)

init_db()

# Rotas:

@app.route('/', methods=['GET', 'POST'])
def wishlist():
    obras = None

    if request.method == 'POST':
        titulo_obra = request.form['titulo-obra']
        indicacao_obra = request.form['indicacao-obra']
        tipo_obra = request.form['tipo-obra']
        obra = Obra(titulo_obra, indicacao_obra, tipo_obra)
        obra.salvar_obra()

    obras = Obra.obter_obras()
    return render_template('lista.html', titulo="Lista de Desejos", obras=obras)

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
    
    obras = Obra.obter_obras()
    obra_selecionada = Obra.id(idObra)
    return render_template('lista.html', titulo=f'Editando a obra de ID: {idObra}', obras=obras, obra_selecionada=obra_selecionada)