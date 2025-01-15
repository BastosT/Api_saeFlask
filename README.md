# IoT Data Collector API

## 📝 Description
API Flask pour la collecte et l'exposition de données IoT depuis des capteurs multiples (température, humidité, qualité de l'air) stockées dans InfluxDB.

## 🛠️ Technologies
- Python 3.8+
- Flask
- InfluxDB
- Docker (optionnel)

## ⚙️ Installation

1. Installer les dépendances
```bash
pip install -r requirements.txt
```

## 🚀 Démarrage

```bash
flask run --port 5000
```

## 📚 API Endpoints

### Données de Température
```http
GET /temperature_data
```

Retourne les données de température des capteurs.

#### Réponse
```json
{
    "sensors": [
        "multisensor_7_2_boitier_salle_11_temperature",
        "multisensor_7_2_fenetre_salle_14_air_temperature"
    ],
    "data_by_sensor": {
        "multisensor_7_2_boitier_salle_11_temperature": [
            {
                "temperature": 18.8,
                "time": 1705261025.359663,
                "sensor_id": "multisensor_7_2_boitier_salle_11_temperature"
            }
        ]
    }
}
```

### Toutes les Données
```http
GET /data20
```

Retourne toutes les données des capteurs.


## 🔄 Utilisation avec Docker

1. Build de l'image
```bash
docker build -t iot-collector .
```

2. Lancement du container
```bash
docker run -p 5000:5000 iot-collector
```


