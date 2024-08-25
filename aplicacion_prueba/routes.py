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
            self.mandar_a_principal(token=token_actual)
            print('Exite un token')
        else:
            print('No hay token o ya expiro')
            self.mandar_a_login()

    def mandar_a_login(self, ventana_anterior=None): # Mandar al usuario a la vista login
        from mainwindow import MainWindow  # Importación diferida
        print(ventana_anterior)
        if ventana_anterior:
            self.current_window = MainWindow() # La ventana actual se conviernte en MainWindow
            self.current_window.show() # Mostramos la ventana actual
            ventana_anterior.close() # Se cierra la anterior
        else:
            self.current_window = MainWindow()
            self.current_window.show() # Mostramos la ventana actual

    def mandar_a_registro(self, ventana_anterior): # Mandar al usuario a la vista registro
        from register import RegisterWindow  # Importación diferida
        self.current_window = RegisterWindow() #Asignamos la ventana de register
        self.current_window.show() # mostramos la ventana register
        ventana_anterior.close() # Se cierra la ventana actual

    def mandar_a_principal(self, ventana_anterior = None, token=None):  # Mandar al usuario a la vista home
        from home import HomeWindow  # Importación diferida

        if ventana_anterior:
            save_token(token)
            info_user = decode_token(token)
            nombre_usuario = info_user['sub'] # Subject (a quien le pertenece el token)
            self.current_window = HomeWindow(nombre_usuario=nombre_usuario)
            self.current_window.show()
            ventana_anterior.close() # Se cierra la ventana actual
        else:
            info_user = decode_token(token)
            nombre_usuario = info_user['sub'] # Subject (a quien le pertenece el token)
            self.current_window = HomeWindow(nombre_usuario=nombre_usuario)
            self.current_window.show() # Mostramos la ventana actual
