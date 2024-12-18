## Formulář ve Flask Python

Tento projekt je jednoduchá webová aplikace pro správu uživatelů, postavená pomocí Flask, SQLAlchemy a WTForms.

## Instalace 

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # Na Windows použijte .venv\Scripts\activate
    pip install -r requirements.txt
    python run.py
    flask run
    ```

Otevřete webový prohlížeč a přejděte na `http://127.0.0.1:5000`.

## Docker

1. Vytvořte Docker image:
    ```sh
    docker build -t flask-app .
    ```

2. Spusťte Docker container:
    ```sh
    docker run -p 5000:5000 flask-app
    ```

## Funkce

- Přidávání uživatelů s validací formuláře (WTForms)
- Zobrazení seznamu uživatelů (table)
- Mazání uživatelů
