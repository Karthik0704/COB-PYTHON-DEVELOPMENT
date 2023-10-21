import requests

def fetch_weather_data(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change units to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        return None

def display_weather_data(data):
    if data:
        city = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
    else:
        print("City not found or an error occurred.")

if __name__ == "__main__":
    api_key = '7f5147057e2cb89f981c6ffb03c7f29a'  # Replace with your OpenWeatherMap API key
    city = input("Enter a city name: ")

    weather_data = fetch_weather_data(api_key, city)

    display_weather_data(weather_data)
