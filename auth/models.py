from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Cliente(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))    
    cpf= db.Column(db.String(150))   
    idade = db.Column(db.Integer)
    

    def __init__(self, nome,cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade    



class Produto(db.Model): 
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))    
    valor = db.Column(db.String(150)) 
    image = db.Column(db.Text)

    def __init__(self, nome,valor, image):
        self.nome = nome    
        self.valor = valor 
        self.image = image
