from app import app,db

class ContatoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(60), nullable = False)
    telefone = db.Column(db.String(14), nullable = False)
    mensagem = db.Column(db.Text, nullable = True)
    
    def __repr__(self):
        return 'Contato!'

class CadastroModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False)
    sobrenome = db.Column(db.String(40), nullable = False)
    cpf = db.Column(db.String(11), nullable = False, unique = True)
    email = db.Column(db.String(60), nullable = False,unique = True )
    senha = db.Column(db.String(10), nullable = False)
    uf = db.Column(db.String(30), nullable = False )
    cidade = db.Column(db.String(30), nullable = False )
    endereco = db.Column(db.String(30), nullable = False )
    numero_residencial = db.Column(db.String(30), nullable = False )
    def __repr__(self):
        return 'Cadastro!'
    