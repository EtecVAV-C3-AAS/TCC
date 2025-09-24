
import os
class Configuracao:
    SECRET_KEY = os.environ.get("SECRET_KEY", "segredo-super-seguro-para-desenvolvimento")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///educa.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
