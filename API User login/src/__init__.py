from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    from src.router import routers  # Importa el blueprint de rutas

    app.register_blueprint(routers)  # Registra el blueprint con la aplicación
    return app