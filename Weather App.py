import requests

def get_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Received response code {response.status_code}")
        print(f"Response: {response.text}")
        return None

def display_weather(data):
    if data:
        city = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("Error: Unable to fetch weather data. Please check the location or try again later.")

def main():
    api_key = "7189b3c78c569491fa532634d2d7d0d1"

    location = input("Enter a city name or ZIP code to get the current weather: ").strip()
    
    if location:
        weather_data = get_weather_data(api_key, location)
        display_weather(weather_data)
    else:
        print("You must enter a location.")

if __name__ == "__main__":
    main()