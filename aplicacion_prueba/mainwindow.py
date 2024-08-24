# This Python file uses the following encoding: utf-8
import sys
import requests
import json

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_MainWindow
from routes import RouteManager
from helpers import url_api


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Login')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.route_manager = RouteManager() #inicializa el administrador de rutas
        self.ui.Boton_registro.clicked.connect(self.dirigir_a_registro) # le pedimos que cuando se oprima el boton de registro ejecute el metodo  dirigir_a_registro
        self.ui.Boton_inicio.clicked.connect(self.iniciar_sesion)


    def iniciar_sesion(self):

        url = url_api + '/usuarios/login'# ruta de mi api
        email = self.ui.Ingreso_nombre.text() #informacion de los inputs nombre
        password = self.ui.Ingreso_pass.text() #informacion de los inputs pass
        # informacion que se va a envar a el api
        info_a_enviar = {
            'email': email,
            'password': password
        }

        response = requests.post(url, data=info_a_enviar) # Creamos una variable para la respuesta del servidor
        print('Se obtuvo una respuesta del servicor')

        respuesta_decodificada = response.content.decode('utf-8')
        respuesta_decodificada = json.loads(respuesta_decodificada)
        print(respuesta_decodificada)

        if 'Error' in respuesta_decodificada:
            print('El email o contraseña no coincide')
            self.ui.Texto_salida.setText('El email o contraseña no coinciden :(')
        elif 'Token' in respuesta_decodificada:  # Se redirige al usuario a la ventana principal
            print('Sesión inicio corretamente')
            token = respuesta_decodificada['Token']
            self.route_manager.mandar_a_principal(self, token)
        else:
            print('Error en el servidor')
            self.ui.Texto_salida.setText('Error interno del servvicod :(')


    def dirigir_a_registro(self):
        self.route_manager.mandar_a_registro(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
#-------------------------------------------------

#-------------------------------------------------
    widget.show()
    sys.exit(app.exec())
