from datetime import datetime
from app import app, db, ma
from sqlalchemy import Column, ForeignKey, Integer, Float, DateTime
from sqlalchemy.orm import relationship
from modelos.producto_modelo import *
from modelos.usuario_modelo import *

# Definir la tabla Compra
class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    importe_total = db.Column(db.Float, nullable=False)
    fecha_compra = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    usuario = db.relationship('Usuario', backref=db.backref('compras', lazy=True))
    producto = db.relationship('Producto', backref=db.backref('compras', lazy=True))

    def __init__(self, id_usuario, id_producto, cantidad, importe_total):
        self.id_usuario = id_usuario
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.importe_total = importe_total
        self.fecha_compra = datetime.utcnow()

    def __repr__(self):
        return f'<Compra {self.id_usuario} - {self.id_producto}>'

# Crear todas las tablas
with app.app_context():
    db.create_all()

#  ************************************************************
