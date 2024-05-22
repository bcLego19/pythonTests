import requests

class ApiError(Exception):
  pass

def fetch_weather_data(city, api_key, units):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ApiError(f"Error retrieving weather data for {city} (Status Code: {response.status_code})")

class Weather:
    def __init__(self, city, api_key, units="metric"):
        self.city = city
        self.api_key = api_key
        self.data = None
        self.units = units

    def set_units(self, newUnits):
        self.units = newUnits

    def get_weather(self):
        try:
            self.data = fetch_weather_data(self.city, self.api_key, self.units)
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
        lat = self.data["coord"]["lat"]
        lon = self.data["coord"]["lon"]
        units_symbol = "C"

        if (self.units == "imperial"):
            units_symbol = "F"
        print(f"City: {self.city}")
        print(f"Temperature: {temperature:.2f} °{units_symbol}")
        print(f"Feels Like: {feels_like:.2f} °{units_symbol}")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
        print(f"lat: {lat}, lon: {lon}")

    def get_temperature(self):
        if self.data is None:
            return None
        return self.data["main"]["temp"]

    # Add similar methods to access other weather data (feels_like, humidity, etc.)

def getWeatherForCity(city_name, api_key, units):
    weather = Weather(city_name, api_key, units)
    weather.get_weather()
    weather.display_weather()

# Usage with improved error handling
try:
    getWeatherForCity("Vancouver", "YOUR_API_KEY", "imperial")
except ApiError as e:
    print(f"An error occurred: {e}")

