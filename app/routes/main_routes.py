# app/routes/main_routes.py
from flask import Blueprint, jsonify


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


# # Route pour récupérer les données du capteur
# @main_bp.route('/sensor-data', methods=['GET'])
# def get_sensor_data():
#     try:
#         # Ici, ajoutez votre code pour lire les données du capteur
#         # Par exemple:
#         temperature = 25.5  # Remplacez par votre lecture réelle
#         humidity = 60      # Remplacez par votre lecture réelle
        
#         # Création du point de données pour InfluxDB
#         point = Point("raspberry_sensors") \
#             .field("temperature", temperature) \
#             .field("humidity", humidity) \
#             .time(datetime.utcnow())
        
#         # Écriture dans InfluxDB
#         write_api.write(bucket=app.config['INFLUXDB_BUCKET'], record=point)
        
#         return jsonify({
#             "status": "success",
#             "data": {
#                 "temperature": temperature,
#                 "humidity": humidity
#             }
#         })
    
#     except Exception as e:
#         return jsonify({
#             "status": "error",
#             "message": str(e)
#         }), 500
