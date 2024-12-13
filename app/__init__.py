# app/__init__.py
from flask import Flask
# from app.service.service import *
# import threading
from app.routes.main_routes import main_bp


def create_app():
    app = Flask(__name__)

    # Enregistrement des blueprints pour les routes
    app.register_blueprint(main_bp)

    # # Démarrage des threads pour les tâches de fond
    # def start_background_tasks():
    #     # Thread pour récupérer les données
    #     thread_fetch = threading.Thread(target=fetch_influx_data)
    #     thread_fetch.daemon = True
    #     thread_fetch.start()

    #     # Thread pour transférer les données
    #     thread_transfer = threading.Thread(target=transfer_data)
    #     thread_transfer.daemon = True
    #     thread_transfer.start()

    # # Lancer les tâches de fond avant la première requête
    # @app.before_first_request
    # def before_first_request():
    #     start_background_tasks()

    return app
