import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# --- Configuration ---
API_KEY = '613c133072b9f7514e1f4f69a6d6ba6a'
CITY = 'London'  # Change to any city

# --- Part 1: API Integration - Fetching Data ---
print(f"Fetching 5-day weather forecast for {CITY}...")

try:
    # Correct API endpoint for forecast
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    if data['cod'] != '200':
        print(f"Error: Could not find city '{CITY}'.")
        exit()

    print("Data fetched successfully.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API request: {e}")
    exit()

# --- Part 2: Data Processing ---
dates = []
temperatures = []
humidities = []
wind_speeds = []

for item in data['list']:
    dt_txt = item['dt_txt']
    dates.append(datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S'))
    temperatures.append(item['main']['temp'])
    humidities.append(item['main']['humidity'])
    wind_speeds.append(item['wind']['speed'])

# --- Part 3: Visualization Dashboard ---
print("Generating the visualization dashboard...")

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 10), sharex=True)
fig.suptitle(f'5-Day Weather Forecast Dashboard for {CITY}', fontsize=16)

# Temperature plot
ax1.plot(dates, temperatures, marker='o', linestyle='-', color='red', label='Temperature (°C)')
ax1.set_title('Temperature Forecast')
ax1.set_ylabel('Temperature (°C)')
ax1.grid(True)
ax1.legend()

# Humidity plot
ax2.plot(dates, humidities, marker='o', linestyle='-', color='blue', label='Humidity (%)')
ax2.set_title('Humidity Forecast')
ax2.set_ylabel('Humidity (%)')
ax2.grid(True)
ax2.legend()

# Wind speed plot
ax3.plot(dates, wind_speeds, marker='o', linestyle='-', color='green', label='Wind Speed (m/s)')
ax3.set_title('Wind Speed Forecast')
ax3.set_ylabel('Wind Speed (m/s)')
ax3.set_xlabel('Date and Time')
ax3.grid(True)
ax3.legend()

# Format date on x-axis
formatter = mdates.DateFormatter('%m-%d %H:%M')
ax3.xaxis.set_major_formatter(formatter)
plt.xticks(rotation=45)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

print("Dashboard display complete.")
