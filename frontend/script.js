function getWeather() {
    const city = document.getElementById('cityInput').value;
    const apiUrl = `http://127.0.0.1:5000/api/weather?city=${city}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            document.getElementById('weatherResult').style.display = 'block';
            document.getElementById('cityName').textContent = data.city;
            document.getElementById('description').textContent = data.description;
            document.getElementById('temperature').textContent = `Temperature: ${data.temperature}°C`;
            document.getElementById('humidity').textContent = `Humidity: ${data.humidity}%`;
            document.getElementById('windSpeed').textContent = `Wind Speed: ${data.wind_speed} m/s`;
        })
        .catch(error => {
            alert("City not found or server error!");
            console.error(error);
        });
}
