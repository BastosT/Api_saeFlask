# app/routes/main_routes.py
from flask import Blueprint, jsonify , current_app
from influxdb_client import InfluxDBClient
# from app.services.influx_service import latest_dat


main_bp = Blueprint('main', __name__)


# Connexion InfluxDB
# client = InfluxDBClient(url="http://10.103.1.44:5003/", token="IHZveuksmZNqpWjiUPELnbZFkjrkdOWLbTRgv4nS6zl43KRPUQvfVR_vw_yMV-vUL6O4Ckz2o1PI5mCcSaNE3A==", org="DomoCorp")  #token du groupe4 orga soit de l'iut ou du groupe4
# query_api = client.query_api()

# connexion influxDB ovh 
client = InfluxDBClient(url="http://51.83.36.122:8086", token="V5_uV4fxRIfcTbkek-HqftjwxxYsbh76t8p_j9_9b6bL0DYTv4rqoxOfj7Ng3gfnmkuYIk3in1pAbDUjomvzAw==", org="IUT-INFO")  #token du groupe4 orga soit de l'iut ou du groupe4
query_api = client.query_api()

@main_bp.route('/')
def home():
    return jsonify({
        "message": "Bienvenue sur l'API",
        "routes_disponibles": {
            "test": "/test",
            "data" : "/data",
            "data20" : "/data20"
        }
    })

@main_bp.route('/test')
def test():
    return jsonify({"message": "Hello World!"})



@main_bp.route('/data_1d', methods=['GET'])
def get_all_data():
    try:
        query = '''
        from(bucket:"groupe4")
            |> range(start: -1d)
            |> filter(fn: (r) => r._field == "value")  // On ne prend que les champs "value"
            |> last()  // On prend la dernière valeur
        '''
        result = query_api.query(query)
        
        data = []
        for table in result:
            for record in table.records:
                data.append({
                    "sensor": record.values.get("entity_id"),
                    "measurement": record.values.get("_measurement"),
                    "value": record.get_value(),
                    "time": record.get_time().strftime("%Y-%m-%d %H:%M:%S")
                })
        
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Erreur lors de la récupération des données : {e}")
        return jsonify({"error": "Erreur interne du serveur"}), 500



@main_bp.route('/data_7d', methods=['GET'])
def get_humidity_values():
    try:
        query = '''
        from(bucket:"groupe4")
            |> range(start: -7d)
            |> filter(fn: (r) => r._field == "value")  // On ne prend que les champs "value"
            |> last()  // On prend la dernière valeur
        '''
        result = query_api.query(query)
        
        data = []
        for table in result:
            for record in table.records:
                data.append({
                    "sensor": record.values.get("entity_id"),
                    "measurement": record.values.get("_measurement"),
                    "value": record.get_value(),
                    "time": record.get_time().strftime("%Y-%m-%d %H:%M:%S")
                })
        
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Erreur lors de la récupération des données : {e}")
        return jsonify({"error": "Erreur interne du serveur"}), 500














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


