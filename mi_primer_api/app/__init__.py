from flask import Flask
from flask_restful import Api
from .routes import APIRoutes
from .config import Config
from .extensions import db, jwt


#Creamos una funcion para montar el servidor
def crear_app():
    #La variable app contendrá el servidor
    app = Flask(__name__)
    #Le decimos que se configure atravez de un objeto
    app.config.from_object(Config)
    # Se conecta la app con la BD
    db.init_app(app)
    # Conectamos la app con jwt
    jwt.init_app(app)
    # se inicializa la app y carga las variables 
    with app.app_context():
        db.create_all() #inicializa la BD

        # La variablñe api manejara las peticiones hacia nuetro servidor
        api = Api(app)
        #Agreganos una variale
        routes = APIRoutes()
        routes.init_routes(api)


    #Regresamos el servidor montado
    return app
