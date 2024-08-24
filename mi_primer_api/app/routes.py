#Importamos el modulo "Resource" de flask_restful
from flask_restful import Resource
#El modulo request nos permite aceotar info de un usuario
from flask import request
from .methods import *
from flask_jwt_extended import jwt_required, get_jwt_identity

#Creamos una clase que va a heredar atributos del modulo "Resource"
class HelloWorld(Resource):

    #Este metodo se ejecuta cuandop el ususrio accede a cierta Ruta
    @jwt_required() # verificamos que el usuario este autenticado
    def get(self):
        identidad = get_jwt_identity()
        #regresa un diccionarion con el mensaje que queremos mostrar
        return{'message': 'Hola mundo desde la API', 'status':200}
    
class Almacen(Resource):
    #obtenemos info del almacen
    #Le pedimos informacion con un get
    @jwt_required() # verificamos que el usuario este autenticado
    def get(self):
        parametro_id = request.args.get('id')
        parametro_nombre = request.args.get('nombre')
        return buscar_id_nombre(parametro_id, parametro_nombre)

    #ponemos un nuevo objeto en almacen.
    #Le enviamos info a la API 
    @jwt_required() # verificamos que el usuario este autenticado
    def post(self):
        data = request.get_json()
        return crear_producto(data['nombre'], data['cantidad'])
    

    #crear una variable que guarda lo que se posteo
   
    #Creamos una clase  ue va a manejar todas las rutas

class User_register(Resource):
    def post(self):
        data = request.form
        nombre = data.get('nombre')
        apellidos = data.get('apellidos')
        fechadenacimiento = data.get('fechadenacimiento')
        telefono = data.get('telefono')
        email = data.get('email')
        password = data.get('password')
        print(nombre,email, password, fechadenacimiento)
        respuesta, status = user_register(nombre, apellidos, fechadenacimiento, telefono, email, password)

        return respuesta , status
    
class User_login(Resource):
    def post(self):
        data = request.form
        email = data.get('email')
        password = data.get('password')

        respuesta, status = inicio_sesion(email, password)
        return respuesta , status
        


class APIRoutes():

    #Se declara un metodo para inicializar las rutas
    def init_routes(self, api):
        #Agreganmos una nueva ruta a nuetro API
        api.add_resource(HelloWorld, '/')
        api.add_resource(User_login, '/usuarios/login')
        api.add_resource(User_register, '/usuarios/registro')
        api.add_resource(Almacen,'/objetos_almacen')


    