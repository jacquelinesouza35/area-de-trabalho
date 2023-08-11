from app import app,db

class ContatoModels(db.Model):
    id = db.Column(id.Integer,primary_Key=True)
    nome = db.column(db.String(30),nullable=False)
    email = db.column(db.String(40),nullable=False)
    menssagem = db.column(db.text,nullable=True)


    def _repr_(self):
        return f'<contato {self.nome}>'
    