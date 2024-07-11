from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from app import app, db   #,ma

# defino las tablas
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    nombres = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), unique=True, nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)  # admin, cliente, visitante

    def __init__(self, usuario, nombres, apellidos, correo, contrasena, rol):
        self.usuario = usuario
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
        
  

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
