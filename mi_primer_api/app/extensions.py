from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager # ignrar error de deteccion

db= SQLAlchemy() # Creamos una instancia de Base de datos

jwt = JWTManager() # Creamos una instancia de JWT
