from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TextAreaField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

class Contato(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email',validators=[DataRequired()])
    conteudo = TextAreaField('conteudo',validators=[DataRequired()])
    enviar = SubmitField('enviar')
 