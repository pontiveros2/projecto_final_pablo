class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:pol@127.0.0.1:5435/onti' #.  URL  para base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = '37b2fdbac4860ebb93fe391d2730604864'
    JWT_ALGORITHM = 'HS256'