from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    from src.router import bp  # Importa el blueprint de rutas

    app.register_blueprint(bp)  # Registra el blueprint con la aplicación
    return app