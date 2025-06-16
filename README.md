# 🌦️ Smart Weather Dashboard

A Real-Time Smart Weather Dashboard built using **Flask** (Backend) and **HTML/CSS/JS** (Frontend). The app fetches live weather data from the **OpenWeatherMap API** and displays current temperature, humidity, wind speed, and other parameters for any searched city.

## 🚀 Live Demo

🔗 [Click Here to View Live Dashboard](https://smartweatherdashboard-2.onrender.com)

---

## 💻 Features

- 🔍 Search weather by city name  
- 🌡️ Displays temperature, humidity, wind speed, and weather condition  
- 📊 Shows chart for temperature and humidity trends  
- 🕒 Displays date and time  
- 📖 Maintains search history  
- 📱 Responsive user interface  

---

## 📸 Screenshots

### Homepage

![Dashboard Screenshot](![Screenshot of Wheather Report](https://github.com/user-attachments/assets/3c9e6bb9-8555-4835-b82c-80990438e598)
)


---

## ⚙️ How It Works

### Backend (Flask)

1. The Flask server runs an API endpoint:  
   `GET /api/weather?city=CityName`  
2. This fetches data from **OpenWeatherMap** API using the provided city name.
3. JSON response is sent back with temperature, humidity, wind, etc.

### Frontend (HTML + JS)

1. `index.html` contains a search bar and dynamic card layout.
2. `script.js` handles:
   - Sending request to `/api/weather`
   - Rendering data into DOM
   - Chart plotting using Chart.js
   - LocalStorage for search history

---

## 🧠 Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript, Chart.js  
- **Backend**: Python Flask  
- **API**: [OpenWeatherMap API](https://openweathermap.org/api)  
- **Deployment**: Render  

---

## 🏃‍♀️ Getting Started Locally

```bash
# Clone the repo
git clone https://github.com/Boomikareddy/SmartWeatherDashboard.git
cd SmartWeatherDashboard

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
