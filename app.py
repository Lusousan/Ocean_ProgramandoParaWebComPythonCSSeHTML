# Importa a Classe Flask a partir do módulo flask
# flask é a biblioteca e Flask é o recurso desejado desta biblioteca
from flask import Flask, render_template, g
import sqlite3

# Armazenando os recursos da Classe Flask dentro de uma variável
app = Flask('Aplicação 01')

#Criação da variável para manipular a base de dados
DATABASE = 'banco.bd'
#Criação da variável que permitirá acessar a base de dados
SECRET_KEY = '1234'

#Carrega as configurações associadas aos recursos necessários à manipulação da base de dados
app.config.from_object(__name__)

#Criação da função para conectar a base de dados
def conectar():
    return sqlite3.connect(DATABASE)

#Chama a função que conecta à base de dados
#Efetiva a conexão com o banco de dados
@app.before_request
def before_request():
    g.bd = conectar()

#Finaliza a conexão com o banco de dados
@app.teardown_request
def teardown_request(f):
    g.bd.close()


# @app é a interface que permite que sejam criadas rotas para serem acessadas
@app.route('/')
def page_01_cardapio():
    nomeUsuario = ['Cliente']
    return render_template('page_01_cardapio.html', nome=nomeUsuario)

