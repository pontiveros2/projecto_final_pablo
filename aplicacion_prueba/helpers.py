# Este archivo se ejecuta muchas veces para ayudar a deferentes acciones
# conocidos como: methods, helpers, extensions, manejadores, auxiliares, aux

import jwt
import os # servira para crear un archivo
import datetime # para determinar si token esta vigente


token_file_path = 'token.txt' # Archivo donde se almacenara el token

url_api ='https://95a6-189-159-128-142.ngrok-free.app'

# funcion para desencriptar token
def decode_token(token):
    payload = jwt.decode(token, options={'verify_signature': False})
    return payload

def obtenet_usuario_token(token):
    info_user = decode_token(token)
    return info_user['sub']


def save_token(token):
    #abrimos el archivo donde se va a almacenar el token en modo de escritura
    with open(token_file_path, 'w') as file:
        file.write(token)


def load_token():
    #abrimos el archivo donde se va a almacenar el token en modo de lectura
    if os.path.exists(token_file_path): # solo por si es la primera vez y no existe el archivo aun
        with open(token_file_path, 'r') as file:
            return file.read()
    else:
        return None

def token_is_valid(token):

    info_token = decode_token(token)
    expiration = datetime.datetime.fromtimestamp(info_token['exp']) #combierte a fecha el valor de exp que esta en segundos

    return expiration > datetime.datetime.now()

def delete_token():
    #abrimos archivo
    with open(token_file_path, 'w') as file:
        #borrar el contenido del archivo
        file.write('')





