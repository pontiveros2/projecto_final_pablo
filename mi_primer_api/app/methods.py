from app.extensions import db
from .mlodels.producto import Producto
from .mlodels.usuarios import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

def inicio_sesion(email, password):
    #crea un nuevo usuario
    user = User.get_user_by_email(email=email)
    # Tiempo que el token dura
    caducidad = timedelta(minutes=120) # puesto a 120 minutos como ejemplo para ver como funciona

    if user and (user.check_password(password=password)):
        token_acceso = create_access_token(identity = user.nombre, expires_delta = caducidad) # creamos token de acceso
        return {'Mensaje': 'Loggeado',
        'Token': token_acceso}, 200
    return {'Error': 'Correo o contraseña no existen :('}, 400


def user_register(nombre, apellidos, fechadenacimiento, telefono, email, password ):
    # Busca un usuario por su email
    user = User.get_user_by_email(email=email)

    if user is not None: # Si el usuario existe, regresa un error
        return {'Error': 'Este correo ya esta registrado :('}, 403
    print(nombre, email, password)
    nuevo_usuario = User(nombre=nombre, apellidos=apellidos, fechadenacimiento=fechadenacimiento, telefono=telefono,  email=email) # Se crea un objeto de tipo User con el usuario e imail
    nuevo_usuario.set_password(password=password) #A este objeto se la asigna una contraseña
    nuevo_usuario.save() # Guardamos el usuario en la DB
    return{'Nuevo usuario':{
        'email': email,
        'nombre': nombre
        }
    }, 200 # le damos una respuesta satisfactotia



def buscar_id_nombre(parametro_id, parametro_nombre):
    if parametro_id != None:
        producto_obtenido = Producto.query.get_or_404(parametro_id)
        json_retornado ={
            'ID':producto_obtenido.id,
            'Nombre':producto_obtenido.nombre,
            'Cantidad': producto_obtenido.cantidad
        }
        return json_retornado


    elif parametro_nombre != None:
        producto_obtenido = Producto.query.filter_by(nombre=parametro_nombre).first_or_404()
        json_retornado ={
            'ID':producto_obtenido.id,
            'Nombre':producto_obtenido.nombre,
            'Cantidad': producto_obtenido.cantidad
        }
        return json_retornado
    
    def crear_producto(nombre, cantidad):
        nuevo_producto = Producto(nombre=nombre,cantidad=cantidad)
        db.session.add(nuevo_producto)
        db.session.commit()
        json_retornado ={
            'ID':nuevo_producto.id,
            'Nombre':nuevo_producto.nombre,
            'Cantidad': nuevo_producto.cantidad
        }
        return json_retornado
    

    

