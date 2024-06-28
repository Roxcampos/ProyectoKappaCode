from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from app import app, db   #,ma

# defino las tablas
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.String(200), nullable=False)
   
    def __init__(self, nombre, precio, stock, categoria, genero, imagen):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.genero = genero
        self.imagen = imagen

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
