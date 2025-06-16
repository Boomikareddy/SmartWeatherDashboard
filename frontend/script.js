let weatherChart; // Global chart instance

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

            // Show the chart canvas
            document.getElementById('weatherChart').style.display = 'block';

            // Create chart
            renderWeatherChart(data);
        })
        .catch(error => {
            alert("City not found or server error!");
            console.error(error);
        });
}

function renderWeatherChart(data) {
    const ctx = document.getElementById('weatherChart').getContext('2d');

    // Destroy previous chart if it exists
    if (weatherChart) {
        weatherChart.destroy();
    }

    // Create a new bar chart
    weatherChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)'],
            datasets: [{
                label: `Weather Stats for ${data.city}`,
                data: [data.temperature, data.humidity, data.wind_speed],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
