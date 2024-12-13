# app/routes/main_routes.py
from flask import Blueprint, jsonify
# from app.services.influx_service import latest_dat


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return jsonify({
        "message": "Bienvenue sur l'API",
        "routes_disponibles": {
            "test": "/test"
        }
    })

@main_bp.route('/test')
def test():
    return jsonify({"message": "Hello World!"})


# @app.before_first_request
# def startup_event():
#     def fetch_task():
#         fetch_influx_data()

#     def transfer_task():
#         while True:
#             transfer_data()
#             time.sleep(300)  # Transfert toutes les 5 minutes

#     # Thread pour récupérer les données
#     thread_fetch = threading.Thread(target=fetch_task)
#     thread_fetch.daemon = True
#     thread_fetch.start()

#     # Thread pour transférer les données
#     thread_transfer = threading.Thread(target=transfer_task)
#     thread_transfer.daemon = True
#     thread_transfer.start()


# @app.route("/data", methods=["GET"])
# def get_data():
#     try:
#         if not latest_data:  # Vérifie si les données sont vides ou invalides
#             return jsonify({"error": "No data available"}), 404
#         return jsonify(latest_data)
#     except Exception as e:
#         # Capture et log les erreurs
#         print(f"Error in get_data: {e}")  # Affiche l'erreur dans la console
#         return jsonify({"error": "Internal server error"}), 500


