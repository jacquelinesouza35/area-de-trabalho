from app import app
from flask import render_template

@app.route ('/')
def index():
    return render_template('index.html',title= 'inicio')
@app.route('/sobre')
def sobre():
    return render_template('sobre.html',title= 'sobre')
@app.route('/projetos')
def projetos():
    return render_template('projetos.html',title= 'projetos')
@app.route('/contato')
def contato():
    return render_template('contato.html',title= 'contato')