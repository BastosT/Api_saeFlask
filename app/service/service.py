# from influxdb_client import InfluxDBClient
# import time

# # Paramètres InfluxDB locale
# local_url = "http://localhost:8086"
# local_token = "Votre_Token_Local"
# local_org = "Votre_Organisation_Local"
# local_bucket = "Votre_Bucket_Local"

# # Paramètres InfluxDB OVH (distante)
# remote_url = "https://eu-west-1-1.aws.cloud2.influxdata.com"
# remote_token = "Votre_Token_OVH"
# remote_org = "Votre_Organisation_OVH"
# remote_bucket = "Votre_Bucket_OVH"

# latest_data = []

# # Récupérer les données de l'InfluxDB locale
# def fetch_influx_data():
#     global latest_data
#     client = InfluxDBClient(url=local_url, token=local_token, org=local_org)
#     query = f'''
#     from(bucket: "{local_bucket}")
#       |> range(start: -1h)
#     '''
#     while True:
#         result = client.query_api().query(query, org=local_org)
#         latest_data = [
#             {"time": record.get_time(), "value": record.get_value()}
#             for table in result
#             for record in table.records
#         ]
#         print(f"Data fetched locally: {len(latest_data)} points")
#         time.sleep(60)

# # Transférer les données vers l'InfluxDB OVH
# def transfer_data():
#     local_client = InfluxDBClient(url=local_url, token=local_token, org=local_org)
#     remote_client = InfluxDBClient(url=remote_url, token=remote_token, org=remote_org)

#     query = f'''
#     from(bucket: "{local_bucket}")
#       |> range(start: -1h)
#     '''
#     result = local_client.query_api().query(query, org=local_org)

#     # Écrire directement les résultats récupérés dans l'InfluxDB OVH
#     write_api = remote_client.write_api()
#     write_api.write(bucket=remote_bucket, org=remote_org, record=result)
#     print(f"Data transferred to remote InfluxDB: {len(result)} points")









# logique pour recupere les donnees pour l'ia 











# import requests
# from flask import Flask, request, jsonify
# from tensorflow.keras.models import load_model
# import numpy as np

# app = Flask(__name__)

# # Charger le modèle IA
# model = load_model("mon_modele.h5")

# # URL de l'API InfluxDB
# INFLUXDB_API_URL = "http://localhost:5000/data"

# @app.route('/predict', methods=['GET'])
# def predict():
#     # Étape 1 : Récupérer les données depuis l'API InfluxDB
#     response = requests.get(INFLUXDB_API_URL)
#     if response.status_code != 200:
#         return jsonify({"error": "Erreur lors de la récupération des données"}), 500

#     # Étape 2 : Préparer les données pour le modèle
#     data = response.json()
#     temps = [entry["value"] for entry in data]  # Extraire les valeurs de température
#     seq_length = 10  # Longueur de la séquence pour la prédiction
#     if len(temps) < seq_length:
#         return jsonify({"error": "Pas assez de données pour la prédiction"}), 400

#     input_data = np.array(temps[-seq_length:]).reshape((1, seq_length, 1))  # Préparation pour LSTM

#     # Étape 3 : Faire la prédiction
#     prediction = model.predict(input_data).tolist()

#     # Étape 4 : Retourner les prédictions
#     return jsonify({"prediction": prediction})

# if __name__ == '__main__':
#     app.run(port=5001)
