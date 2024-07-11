from flask import jsonify, request  # Importar jsonify y request de Flask
from app import app, db, ma  # Importar la aplicación, la base de datos y Marshmallow de app
from modelos.compra_modelo import * # Importar el modelo Compra
from modelos.producto_modelo import *
from modelos.usuario_modelo import *
from controladores.producto_controlador import *
from controladores.usuario_controlador import *

# Esquema para Compra
class CompraSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_usuario', 'id_producto', 'cantidad', 'importe_total', 'fecha_compra')

compra_schema = CompraSchema()  # Para traer una compra
compras_schema = CompraSchema(many=True)  # Para traer múltiples compras

# Crear una nueva compra
@app.route('/compras', methods=['POST'])
def create_compra():
    id_usuario = request.json['id_usuario']
    id_producto = request.json['id_producto']
    cantidad = request.json['cantidad']
    importe_total = request.json['importe_total']
    
    new_compra = Compra(id_usuario, id_producto, cantidad, importe_total)
    db.session.add(new_compra)
    db.session.commit()
    
    return compra_schema.jsonify(new_compra)

# Obtener todas las compras
@app.route('/compras', methods=['GET'])
def get_compras():
    all_compras = Compra.query.all()
    result = compras_schema.dump(all_compras)
    return jsonify(result)

# Obtener una compra por ID
@app.route('/compras/<id>', methods=['GET'])
def get_compra(id):
    compra = Compra.query.get(id)
    return compra_schema.jsonify(compra)

# Actualizar una compra por ID
@app.route('/compras/<id>', methods=['PUT'])
def update_compra(id):
    compra = Compra.query.get(id)
    
    compra.id_usuario = request.json['id_usuario']
    compra.id_producto = request.json['id_producto']
    compra.cantidad = request.json['cantidad']
    compra.importe_total = request.json['importe_total']
   
    
    db.session.commit()
    return compra_schema.jsonify(compra)

# Eliminar una compra por ID
@app.route('/compras/<id>', methods=['DELETE'])
def delete_compra(id):
    compra = Compra.query.get(id)
    db.session.delete(compra)
    db.session.commit()
    return compra_schema.jsonify(compra)

