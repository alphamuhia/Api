import requests
import csv

locations = []
api_key = "a24219dc3bf1312f6886a09f9795eb8b"  
units = "metric"  


user_input = input("Input city or country name: ").strip()

if user_input:
    locations = [location.strip() for location in user_input.split(',')]

with open("weather.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(['City', 'Temperature (°C)', 'Humidity (%) '])  

    if user_input:
        locations.append(user_input)

    for location in locations:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units={units}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            city = data['name']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

            writer.writerow([city, temperature, humidity])

            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print("Data has been saved to weather.csv.\n")
        else:       
            print(f"Failed to retrieve weather data for '{location}'. HTTP Status code: {response.status_code}")
