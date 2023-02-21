# Importa a Classe Flask a partir do módulo flask
# flask é a biblioteca e Flask é o recurso desejado desta biblioteca
from flask import Flask, render_template

# Armazenando os recursos da Classe Flask dentro de uma variável
app = Flask("Aplicação 01")

# @app é a interface que permite que sejam criadas rotas para serem acessadas
@app.route('/Alunos')
def page_01_alunos():
    return render_template('page_01_alunos.html')

@app.route('/Notas')
def page_02_notas():
    return render_template('page_02_notas.html')