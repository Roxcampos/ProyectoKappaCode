from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request

from app import app, db,ma
from modelos.producto_modelo import *

class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','stock','categoria','genero','imagen')

producto_schema=ProductoSchema()            # El objeto producto_schema es para traer un producto
productos_schema=ProductoSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto

# crea los endpoint o rutas (json)
@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
    result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
                                               # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla

@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    return producto_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro

@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)   # me devuelve un json con el registro eliminado

@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    precio=request.json['precio']
    stock=request.json['stock']
    categoria=request.json['categoria']
    genero=request.json['genero']
    imagen=request.json['imagen']
    new_producto=Producto(nombre,precio,stock,categoria,genero,imagen)
    db.session.add(new_producto)
    db.session.commit() # confirma el alta
    return producto_schema.jsonify(new_producto)


@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Producto.query.get(id)
 
    producto.nombre=request.json['nombre']
    producto.precio=request.json['precio']
    producto.stock=request.json['stock']
    producto.categoria=request.json['categoria']
    producto.genero=request.json['genero']
    producto.imagen=request.json['imagen']
    
    db.session.commit()
    return producto_schema.jsonify(producto)

@app.route('/')
def bienvenida():
    return "Bienvenidos al backend"   # retorna el JSON de un usuario recibido como parametro
