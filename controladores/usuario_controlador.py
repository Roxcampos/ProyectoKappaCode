from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request

from app import app, db,ma
from modelos.usuario_modelo import *

#Creando objeto usuario
class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('id','usuario','nombres','apellidos','correo','contrasena','rol')


usuario_schema=UsuarioSchema()  # El objeto producto_schema es para traer un producto
usuarios_schema=UsuarioSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto

# crea RUTAS para usuarios
#@app.route('/usuarios',methods=['GET'])
#def get_Usuarios():
 #   all_usuarios=Usuario.query.all() # el metodo query.all() lo hereda de db.Model
  #  result=usuario_schema.dump(all_usuarios)  #el metodo dump() lo hereda de ma.schema y
   #                                              # trae todos los registros de la tabla
   # return jsonify(result)     # retorna un JSON de todos los registros de la tabla

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    all_usuarios=Usuario.query.all()         # el metodo query.all() lo hereda de db.Model
    result=usuarios_schema.dump(all_usuarios)  # el metodo dump() lo hereda de ma.schema y
                                               # trae todos los registros de la tabla
    return jsonify(result)  

@app.route('/usuarios/<id>',methods=['GET'])
def get_usuario(id):
    usuario=Usuario.query.get(id)
    return usuario_schema.jsonify(usuario)   # retorna el JSON de un producto recibido como parametro


@app.route('/usuarios/<id>',methods=['DELETE'])
def delete_usuario(id):
    usuario=Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()                     # confirma el delete
    return usuario_schema.jsonify(usuario) # me devuelve un json con el registro eliminado


@app.route('/usuarios', methods=['POST']) # crea ruta o endpoint
def create_usuario():
    #print(request.json)  # request.json contiene el json que envio el cliente
    usuario=request.json['usuario']
    nombres=request.json['nombres']
    apellidos=request.json['apellidos']
    correo=request.json['correo']
    contrasena=request.json['contrasena']
    rol=request.json['rol']
    new_usuario=Usuario(usuario,nombres,apellidos,correo,contrasena,rol)
    db.session.add(new_usuario)
    db.session.commit() # confirma el alta
    return usuario_schema.jsonify(new_usuario)


@app.route('/usuarios/<id>' ,methods=['PUT'])
def update_usuario(id):
    usuario=Usuario.query.get(id)
 
    usuario.usuario=request.json['usuario']
    usuario.nombres=request.json['nombres']
    usuario.apellidos=request.json['apellidos']
    usuario.correo=request.json['correo']
    usuario.contrasena=request.json['contrasena']
    usuario.rol=request.json['rol']
  
    
    db.session.commit()    # confirma el cambio
    return usuario_schema.jsonify(usuario)    # y retorna un json con el producto
