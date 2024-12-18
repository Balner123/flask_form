# run.py
from app.app import create_app
from app.database import db

# Funkce pro inicializaci databáze
def init_db():
    app = create_app()  # Vytvoření aplikace
    with app.app_context():
        db.create_all()  # Vytvoření tabulek
        print("Database initialized!")

if __name__ == '__main__':
    # Inicializace databáze při spuštění aplikace
    init_db()
    
    # Spuštění Flask aplikace
    create_app().run(host='0.0.0.0', port=5000, debug=True)
