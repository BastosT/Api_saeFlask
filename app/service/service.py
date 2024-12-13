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
