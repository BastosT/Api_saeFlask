# app/routes/main_routes.py
from flask import Blueprint, jsonify , current_app
from influxdb_client import InfluxDBClient
# from app.services.influx_service import latest_dat


main_bp = Blueprint('main', __name__)


# Connexion InfluxDB
client = InfluxDBClient(url="http://10.103.1.44:5003/", token="IHZveuksmZNqpWjiUPELnbZFkjrkdOWLbTRgv4nS6zl43KRPUQvfVR_vw_yMV-vUL6O4Ckz2o1PI5mCcSaNE3A==", org="DomoCorp")  #token du groupe4 orga soit de l'iut ou du groupe4
query_api = client.query_api()


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


@main_bp.route('/data', methods=['GET'])
def get_data():
    try:
        # Requête pour récupérer les données
        query = 'from(bucket:"HA_Bucket") |> range(start: -7d)'
        result = query_api.query(query)
        data = [{"time": record.get_time(), "value": record.get_value()} for table in result for record in table.records]
        return jsonify(data)
    except Exception as e:
        # Log de l'erreur pour déboguer
        current_app.logger.error(f"Erreur lors de la récupération des données : {e}")
        return jsonify({"error": "Erreur interne du serveur"}), 500
    

@main_bp.route('/data20', methods=['GET'])
def get_all_data():
    try:
        # Requête pour récupérer toutes les données disponibles
        query = 'from(bucket:"HA_Bucket") |> range(start: -7d)'
        result = query_api.query(query)
        
        data = []
        
        # Parcours des résultats et ajout de toutes les colonnes disponibles
        for table in result:
            for record in table.records:
                # `record.values` contient toutes les colonnes
                record_data = dict(record.values)
                # Ajoute également le champ `time`
                record_data["time"] = record.get_time()
                data.append(record_data)
        
        return jsonify(data)
    except Exception as e:
        # Log de l'erreur pour déboguer
        current_app.logger.error(f"Erreur lors de la récupération des données : {e}")
        return jsonify({"error": "Erreur interne du serveur"}), 500


# @app.route('/latest', methods=['GET'])
# def get_latest():
#     query = 'from(bucket:"votre_bucket") |> range(start: -1h)'
#     result = query_api.query(query)
#     data = [{"time": record.get_time(), "value": record.get_value()} for table in result for record in table.records]
#     return jsonify(data)












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


