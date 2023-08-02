from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class Contato(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email',validators=[DataRequired()])
    conteudo = TextAreaField('conteudo',validators=[DataRequired()])
    enviar = SubmitField('enviar')