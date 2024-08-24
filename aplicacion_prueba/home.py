# This Python file uses the following encoding: utf-8
import sys
import requests
import json


from helpers import load_token, obtenet_usuario_token, token_is_valid, url_api, delete_token
from PySide6.QtWidgets import QApplication, QMainWindow   # Herramientas para renderizar las aplicaciones


# Important:
# You need to run the following command to generate the ui_register.py file
#     pyside6-uic home.ui -o ui_home.py


#Importamos todo el apartado gráfico "register.ui"
from ui_home import Ui_HomeWindow
from routes import RouteManager

#Clase que contiene la ventana de registro
class HomeWindow(QMainWindow):
    def __init__(self, nombre_usuario = "1", parent = None):
        super().__init__(parent)
        self.route_manager = RouteManager()
        self.nombre_usuario = nombre_usuario
        token_actual = load_token()
        #print(token_is_valid(token_actual))



        #Este atributo contendra todo el apartado gráfico
        self.ui = Ui_HomeWindow()
        # Inicializamos el apartado gráfico
        self.ui.setupUi(self)

        self.ui.mensage_home.setText(f'Bienvenido: {self.nombre_usuario}') # Le decimos a la etiqueta que sobreescriba su contenido con el correo del usuario

        self.ui.boton_buscar.clicked.connect(self.buscar)
        self.ui.salir.clicked.connect(self.cerrar_sesion)

        self.ui.checkBox_id.setChecked(True)
        self.ui.checkBox_id.toggled.connect(self.check_id_presionado)
        self.ui.checkBox_nombre.toggled.connect(self.check_name_presionado)

        #self.route_manager.dirigir_a_login(self)



    def check_name_presionado(self, checked):
        if checked and self.ui.checkBox_id.isChecked():
            self.ui.checkBox_id.setChecked(False)


    def check_id_presionado(self, checked):
        if checked and self.ui.checkBox_nombre.isChecked():
            self.ui.checkBox_nombre.setChecked(False)


    def buscar_producto_id(self):
        id_producto = self.ui.buscador.text()
        token_actual = load_token()
        headers = {"Authorization":f"Bearer {token_actual}"}


        url = f"{url_api}/objetos_almacen?id={id_producto}"


        response = requests.get(url, headers=headers)
        datos_producto = response.content.decode('utf-8')
        datos_producto = json.loads(datos_producto)

        if 'message' in datos_producto:
            self.ui.nombre_producto.setText('No se encontro el producto')
            self.ui.cantidad_producto.setText('')
        elif 'Nombre' in datos_producto:
            self.ui.nombre_producto.setText(f"Producto: {datos_producto['Nombre'].capitalize()}")
            self.ui.cantidad_producto.setText(f"Cantidad: {str(datos_producto['Cantidad'])}")

    def buscar_producto_nombre(self):
        nombre_producto = self.ui.buscador.text()
        token_actual = load_token()
        headers = {"Authorization":f"Bearer {token_actual}"}


        url = f"{url_api}/objetos_almacen?nombre={nombre_producto}"


        response = requests.get(url, headers=headers)
        datos_producto = response.content.decode('utf-8')
        datos_producto = json.loads(datos_producto)

        if 'message' in datos_producto:
            self.ui.nombre_producto.setText('No se encontro el producto')
            self.ui.cantidad_producto.setText('')
        elif 'Nombre' in datos_producto:
            self.ui.nombre_producto.setText(f"Producto: {datos_producto['Nombre'].capitalize()}")
            self.ui.cantidad_producto.setText(f"Cantidad: {str(datos_producto['Cantidad'])}")

    def cerrar_sesion(self):
        print('Cerrando sesión')
        #borramos el toke
        delete_token()
        self.route_manager.mandar_a_login(self) #envia a la pantalla de looging
        #borramos el toke

    def buscar(self):
        if self.ui.checkBox_id.isChecked():
            self.buscar_producto_id()
        elif self.ui.checkBox_nombre.isChecked():
            self.buscar_producto_nombre()


# Metodo magico, verifica si el archivo se esta ejecutando de raiz
if __name__ == '__main__':
    # Iniciamos la plicacion ventana
    app = QApplication(sys.argv)
    # Creamos objeto de tipo HomeWindow
    widget = HomeWindow()





    # este metodo muestra la ventana
    widget.show()
    # Para cerrar ventana
    sys.exit(app.exec())
