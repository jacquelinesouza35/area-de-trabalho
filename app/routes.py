from app import app
from flask import render_template,url_for,flash,redirect,request
from app.forms import Contato
import time


@app.route ('/')
def index():
    return render_template('index.html',title= 'inicio')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html',title= 'sobre')

@app.route('/contato',methods=['GET','POST'])
def contato():
    dados_formulario = None
    formulario = Contato()
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        conteudo = request.form.get('conteudo')
        
        dados_formulario = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'conteudo': conteudo
        }
    return render_template('contato.html', title ='Contato', formulario = formulario, dados_formulario = dados_formulario)

@app.route('/projetos')
def projetos():
    return render_template('projetos.html',title= 'projetos')

@app.route('/base')
def base():
    return render_template('base.html',title= 'base')
