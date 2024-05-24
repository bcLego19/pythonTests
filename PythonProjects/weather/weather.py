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
        self.temperature = None

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
        self.set_temperature(self.data["main"]["temp"])
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
        self.set_lat(self.data["coord"]["lat"])
        return self.data["coord"]["lat"]
    
    def get_lon(self):
        if self.data is None:
            return None
        self.set_lon(self.data["coord"]["lon"])
        return self.data["coord"]["lon"]
    
    def get_city(self):
        if self.data is None:
            return None
        if self.city is None:
            return None
        return self.city
    
    def get_units(self):
        return self.units
    
    def set_units(self, newunits):
        self.units = newunits
        return
    
    def set_city(self, newcity):
        self.city = newcity
        return

    def set_coords(self, newlat, newlon):
        self.lat = newlat
        self.lon = newlon
        return
    
    def set_lat(self, newlat):
        self.lat = newlat
        return
    
    def set_lon(self, newlon):
        self.lon = newlon
        return
    
    def set_temperature(self, temperature):
        self.temperature = temperature
        return
    
    def celsius_to_fahrenheit(self, temp_celsius):
        newtemp = (temp_celsius * (9/5)) + 32
        self.set_temperature(newtemp)
        return newtemp

    def fahrenheit_to_celsius(self, temp_fahrenheit):
        newtemp = (temp_fahrenheit - 32) * (5/9)
        self.set_temperature(newtemp)
        return newtemp

def getWeatherForCity(city_name, api_key, units):
    weather = Weather(city_name, api_key, units)
    weather.get_weather()
    weather.display_weather()
    temp = weather.get_temperature()
    print(temp)
    newtemp = None
    if (weather.get_units() == "imperial"):
        newtemp = weather.fahrenheit_to_celsius(temp)
    elif (weather.get_units() == "metric"):
        newtemp = weather.celsius_to_fahrenheit(temp)
    else:
        newtemp = temp
    
    print(newtemp)
    print(weather.get_units())

# Usage with improved error handling
YOUR_API_KEY = "YOUR_API_KEY"

try:
    getWeatherForCity("Vancouver", YOUR_API_KEY, "imperial")
except ApiError as e:
    print(f"An error occurred: {e}")

