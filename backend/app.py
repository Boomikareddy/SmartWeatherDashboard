from flask import Flask, request, jsonify
from flask_cors import CORS
import requests, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY") or "f7ab3f9c15502f1a86889dafe67af0ef"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/api/weather')

def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        res = requests.get(BASE_URL, params=params)
        data = res.json()
        if res.status_code != 200 or 'main' not in data:
            return jsonify({"error": "City not found"}), 404

        return jsonify({
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
