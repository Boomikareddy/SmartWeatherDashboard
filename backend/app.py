from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app)

# --- Config ---
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY") or "f7ab3f9c15502f1a86889dafe67af0ef"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# --- SQLite Database Setup ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Database Model ---
class WeatherHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100))
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Integer)
    wind_speed = db.Column(db.Float)
    description = db.Column(db.String(100))

# --- Routes ---
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

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

        # Save search to DB
        weather_entry = WeatherHistory(
            city=data["name"],
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
            description=data["weather"][0]["description"]
        )
        db.session.add(weather_entry)
        db.session.commit()

        return jsonify({
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Run Server & Create DB ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
