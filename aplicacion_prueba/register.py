
# This Python file uses the following encoding: utf-8
import sys
import requests
import json

from PySide6.QtWidgets import QApplication, QMainWindow   # Herramientas para renderizar las aplicaciones
from ui_register import Ui_RegisterWindow   #Importamos todo el apartado gráfico "register.ui"
from routes import RouteManager
from helpers import url_api

# Important:
# You need to run the following command to generate the ui_register.py file
#     pyside6-uic register.ui -o ui_register.py

class RegisterWindow(QMainWindow):  #Clase que contiene la ventana de registro
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_RegisterWindow()  #Este atributo contendra todo el apartado gráfico
        self.ui.setupUi(self)  # Inicializamos el apartado gráfico
        #Accines de la ventana
        #Le pedimos que ejecute capturar_info si se presiona el Boton_crear_cuenta
        self.route_manager = RouteManager()
        self.ui.Boton_crear_cuenta.clicked.connect(self.capturar_info)
        self.ui.Regresar.clicked.connect(self.dirigir_a_login)

    def capturar_info(self): #Captura y verifica info

        nombre = self.ui.Nombre.text()
        apellidos = self.ui.Apellidos.text()
        fechadenacimiento = self.ui.Fechadenacimiento.text()
        telefono = self.ui.Telefono.text()
        email = self.ui.Email.text()
        password1 = self.ui.Password1.text()
        password2 = self.ui.Password2.text()

        if len(nombre) == 0 or len(apellidos) == 0 or len(fechadenacimiento) == 0 or len(telefono) == 0 or len(email) == 0 or len(password1) == 0 or len(password2) == 0:
            self.ui.Error.setText('Falta completar campos')
            return 1
        elif '@' not in email or '.' not in email:
            self.ui.Error.setText('Ingresa un email valido')
            return 1
        elif password1 != password2:
            self.ui.Error.setText('Las contraseñas no concuerdan')
            return 1
        else:
            self.ui.Error.setText(' ')
            self.crear_usuario(nombre, apellidos, fechadenacimiento, telefono, email, password1)


    def crear_usuario(self, nombre, apellidos, fechadenacimiento, telefono, email, password1):
        url =  url_api + '/usuarios/registro'
        informacion_usuario = {
            'nombre': nombre,
            'apellidos': apellidos,
            'fechadenacimiento': fechadenacimiento,
            'telefono': telefono,
            'email': email,
            'password': password1
        }

        print('Se esta creando un usuario')

        response = requests.post(url, data = informacion_usuario)
        print('Se obtuvo una respuesta')

        respuesta_decodificada = response.content.decode('utf-8')
        respuesta_decodificada = json.loads(respuesta_decodificada)
        print(respuesta_decodificada)
        if 'Error' in respuesta_decodificada: #si el correo ya existe
            print('Ususario Duplicado')
            self.ui.Error.setText('Este correo ya esta registrado')
            return 1
        elif 'Nuevo usuario' in respuesta_decodificada: #el usuario se creo correctamentw
            print('Se creo un nuevo usuario')
            self.route_manager.mandar_a_login(self) #enviamos a logging (mainwindow) y cerramos venta de registro
            return 1
        else: # hay un error con el servidor
            print('Error interno')
            self.ui.Error.setText('Error Interno')
            return 1


    def dirigir_a_login(self):
        self.route_manager.mandar_a_login(self)



if __name__ == '__main__':  # Metodo magico, verifica si el archivo se esta ejecutando de raiz
    app = QApplication(sys.argv) # Iniciamos la plicacion ventana
    widget = RegisterWindow() # Creamos objeto de tipo RegisterWindo
    widget.show()   # este metodo muestra la ventana
    sys.exit(app.exec())  # Para cerrar ventana

