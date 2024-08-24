# Archivo routes.py

# Este archivo se va a encargar de manejar las redirecciones

from helpers import decode_token, save_token, load_token, token_is_valid, obtenet_usuario_token

class RouteManager:
    def __init__(self):
        self.current_window = None # None especifica que estara vacia



    def dirigir_a_login(self):

        token_actual = load_token()

        if token_actual != '' and token_is_valid(token_actual):
            self.nombre_usuario = obtenet_usuario_token(token_actual)
            self.mandar_a_principal()
            self.cerrar_sesion()
            print('Exite un token')
        else:
            self.mandar_a_login()

            print('No hay token o ya expiro')



    # Mandar al usuario a la vista login
    def mandar_a_login(self, ventana_anterior):
        from mainwindow import MainWindow  # Importación diferida
        self.current_window = MainWindow() #Asignamos la ventana mainwindow
        self.current_window.show() # mostramos la ventana mainwindow
        ventana_anterior.close() # Se cierra la ventana actual

    # Mandar al usuario a la vista registro
    def mandar_a_registro(self, ventana_anterior):
        from register import RegisterWindow  # Importación diferida
        self.current_window = RegisterWindow() #Asignamos la ventana de register
        self.current_window.show() # mostramos la ventana register
        ventana_anterior.close() # Se cierra la ventana actual

    # Mandar al usuario a la vista home
    def mandar_a_principal(self, ventana_anterior, token):
        from home import HomeWindow  # Importación diferida

        save_token(token)
#--------------------------------------------------------------
        info_user = decode_token(token)
        nombre_usuario = info_user['sub']

        self.current_window = HomeWindow(nombre_usuario=nombre_usuario)
        self.current_window.show()
        ventana_anterior.close() # Se cierra la ventana actual
