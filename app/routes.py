from app import app,db
from flask import render_template,url_for,flash,redirect,request
from app.forms import Contato
from app.models import ContatoModels
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
    if formulario.validate_on_submit:
        flash('Seu formulario foi enviado com sucesso !!')
        nome = formulario.nome.data
        email =formulario.email.data
        conteudo = formulario.conteudo.data
       
        novo_contato = ContatoModels(nome=nome,email=email,conteudo=conteudo)
        db.session.add(novo_contato)
        db.session.comit()
    
    return render_template('contato.html', title ='Contato', formulario = formulario, dados_formulario = dados_formulario)

@app.route('/projetos')
def projetos():
    return render_template('projetos.html',title= 'projetos')

@app.route('/base')
def base():
    return render_template('base.html',title= 'base')
