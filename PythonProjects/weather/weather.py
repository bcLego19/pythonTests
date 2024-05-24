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
    
def fetch_weather_data_coords(lat, lon, api_key, units):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ApiError(f"Error retrieving weather data for lat ({lat}) and lon({lon}) (Status Code: {response.status_code})")

class Weather:
    city = None
    lat = None
    lon = None
    def __init__(self, city, api_key, units="metric"):
        self.city = city
        self.lat = 0
        self.lon = 0
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
    
    def get_weather_coords(self):
        try:
            self.data = fetch_weather_data_coords(self.lat, self.lon, self.api_key, self.units)
        except ApiError as e:
            print(e)

    def display_weather(self):
        if self.data is None:
            print("Weather data not available. Please call get_weather() first.")
            return
        
        units_symbol = "C"

        if (self.units == "imperial"):
            units_symbol = "F"
        print(f"City: {self.get_city()}")
        print(f"Temperature: {self.get_temperature():.2f} °{units_symbol}")
        print(f"Feels Like: {self.get_feels_like():.2f} °{units_symbol}")
        print(f"Humidity: {self.get_humidity()}%")
        print(f"Description: {self.get_description()}")
        print(f"lat: {self.get_lat()}, lon: {self.get_lon()}")

    # Extract specific data using dictionary keys in unique getters
    def get_temperature(self):
        if self.data is None:
            return None
        return self.data["main"]["temp"]
    
    def get_feels_like(self):
        if self.data is None:
            return None
        return self.data["main"]["feels_like"]
    
    def get_humidity(self):
        if self.data is None:
            return None
        return self.data["main"]["humidity"]
    
    def get_description(self):
        if self.data is None:
            return None
        return self.data["weather"][0]["description"]
    
    def get_lat(self):
        if self.data is None:
            return None
        return self.data["coord"]["lat"]
    
    def get_lon(self):
        if self.data is None:
            return None
        return self.data["coord"]["lon"]
    
    def get_city(self):
        if self.data is None:
            return None
        return self.city
    
    def set_city(self, newcity):
        self.city = newcity
        return

    def set_coords(self, newlat, newlon):
        self.lat = newlat
        self.lon = newlon
        return

    # Add similar methods to access other weather data (feels_like, humidity, etc.)

def getWeatherForCity(city_name, api_key, units):
    weather = Weather(city_name, api_key, units)
    weather.get_weather()
    weather.display_weather()

# Usage with improved error handling
YOUR_API_KEY = "YOUR_API_KEY"

try:
    getWeatherForCity("Vancouver", YOUR_API_KEY, "imperial")
except ApiError as e:
    print(f"An error occurred: {e}")

