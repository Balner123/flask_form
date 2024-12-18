# app/app.py
from flask import Flask
from app.database import db
from app.models import User

def create_app():
    # Vytvoření aplikace
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Inicializace databáze
    db.init_app(app)

    # Import rout až po vytvoření aplikace
    from app.routes import init_routes
    init_routes(app)

    return app