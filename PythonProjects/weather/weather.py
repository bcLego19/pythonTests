import requests

class ApiError(Exception):
  pass

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ApiError(f"Error retrieving weather data for {city} (Status Code: {response.status_code})")

class Weather:
    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key
        self.data = None

    def get_weather(self):
        try:
            self.data = fetch_weather_data(self.city, self.api_key)
        except ApiError as e:
            print(e)

    def display_weather(self):
        if self.data is None:
            print("Weather data not available. Please call get_weather() first.")
            return
        # Extract specific data using dictionary keys
        temperature = self.data["main"]["temp"]
        feels_like = self.data["main"]["feels_like"]
        humidity = self.data["main"]["humidity"]
        description = self.data["weather"][0]["description"]

        print(f"City: {self.city}")
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Feels Like: {feels_like:.2f} °C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")

    def get_temperature(self):
        if self.data is None:
            return None
        return self.data["main"]["temp"]

    # Add similar methods to access other weather data (feels_like, humidity, etc.)

def getWeatherForCity(city_name, api_key):
    weather = Weather(city_name, api_key)
    weather.get_weather()
    weather.display_weather()

# Usage with improved error handling
try:
    getWeatherForCity("Woodland", "db97951a4214b613f1ab9a0aa90d2709")
except ApiError as e:
    print(f"An error occurred: {e}")

