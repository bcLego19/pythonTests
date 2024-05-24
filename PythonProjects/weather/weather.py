import requests # This line imports the requests library for making HTTP requests

class ApiError(Exception):
  pass  # This class defines a custom exception for API errors

def fetch_weather_data(city, api_key, units):
    """Fetches weather data for a given city using OpenWeatherMap API.

    Args:
        city (str): The name of the city.
        api_key (str): Your OpenWeatherMap API key.
        units (str): The desired temperature units ("metric" or "imperial").

    Returns:
        dict: The weather data in JSON format, or None if an error occurs.

    Raises:
        ApiError: If an error occurs while fetching the weather data.
    """

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"  # Builds the API URL
    response = requests.get(url)  # Sends a GET request to the API
    if response.status_code == 200:  # Checks if the request was successful
        return response.json()  # Returns the JSON data from the response
    else:
        raise ApiError(f"Error retrieving weather data for {city} (Status Code: {response.status_code})")  # Raises an exception with an error message

def fetch_weather_data_coords(lat, lon, api_key, units):
    """Fetches weather data for a given latitude and longitude using OpenWeatherMap API.

    Args:
        lat (float): The latitude coordinate.
        lon (float): The longitude coordinate.
        api_key (str): Your OpenWeatherMap API key.
        units (str): The desired temperature units ("metric" or "imperial").

    Returns:
        dict: The weather data in JSON format, or None if an error occurs.

    Raises:
        ApiError: If an error occurs while fetching the weather data.
    """

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}"  # Builds the API URL with lat/lon
    response = requests.get(url)  # Sends a GET request to the API
    if response.status_code == 200:  # Checks if the request was successful
        return response.json()  # Returns the JSON data from the response
    else:
        raise ApiError(f"Error retrieving weather data for lat ({lat}) and lon({lon}) (Status Code: {response.status_code})")  # Raises an exception with an error message

class Weather:
    """A class to represent weather data and perform operations on it.

    Attributes:
        city (str): The city name (New York by default).
        lat (float): The latitude coordinate (if provided).
        lon (float): The longitude coordinate (if provided).
        api_key (str): Your OpenWeatherMap API key.
        data (dict): The weather data in JSON format (None if not fetched).
        units (str): The temperature units ("metric" or "imperial").
        temperature (float): The current temperature (cached value).
    """
    city = None
    lat = None
    lon = None
    def __init__(self, api_key, city="New York", units="metric"):
        """Initializes a Weather object.

        Args:
            city (str): The city name (optional).
            api_key (str): Your OpenWeatherMap API key.
            units (str, optional): The desired temperature units ("metric" or "imperial"). Defaults to "metric".
        """
        self.city = city
        self.lat = 0
        self.lon = 0
        self.api_key = api_key
        self.data = None
        self.units = units
        self.temperature = None

    def get_weather(self):
        """Fetches weather data for the city (if set) using the API key and units.

        Raises:
            ApiError: If an error occurs while fetching the weather data.
        """
        if self.get_city is None:
            print("city not set.")
            self.data = None
            return
        
        try:
            self.data = fetch_weather_data(self.city, self.api_key, self.units)
        except ApiError as e:
            print(e)
    
    def get_weather_coords(self):
        """Fetches weather data for the latitude and longitude (if set) using the API key and units.

        Raises:
            ApiError: If an error occurs while fetching the weather data.
        """
        if (self.get_lon is None):
            print("longitude not set.")
            self.data = None
            return
        if (self.get_lat is None):
            print("latitude not set.")
            self.data = None
            return
        
        try:
            self.data = fetch_weather_data_coords(self.lat, self.lon, self.api_key, self.units)
        except ApiError as e:
            print(e)

    def display_weather(self):
        """Displays the weather data in a user-friendly format, checking for data availability first.

        Prints weather information including city, temperature, feels like, humidity, description, latitude, and longitude.
        """
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
        """Retrieves the current temperature from the weather data (if available).

        Checks for data availability before returning the temperature.
        """
        if self.data is None:
            return None
        self.set_temperature(self.data["main"]["temp"])
        return self.data["main"]["temp"]
    
    def get_feels_like(self):
        """Retrieves the feels-like temperature from the weather data (if available).

        Checks for data availability before returning the feels-like temperature.
        """
        if self.data is None:
            return None
        return self.data["main"]["feels_like"]
    
    def get_humidity(self):
        """Retrieves the humidity level from the weather data (if available).

        Checks for data availability before returning the humidity level.
        """
        if self.data is None:
            return None
        return self.data["main"]["humidity"]
    
    def get_description(self):
        """Retrieves the weather description from the weather data (if available).

        Checks for data availability before returning the weather description.
        """
        if self.data is None:
            return None
        return self.data["weather"][0]["description"]
    
    def get_lat(self):
        """Retrieves the latitude coordinate from the weather data (if available).

        Checks for data availability before returning the latitude.
        """
        if self.data is None:
            return None
        self.set_lat(self.data["coord"]["lat"])
        return self.data["coord"]["lat"]
    
    def get_lon(self):
        """Retrieves the longitude coordinate from the weather data (if available).

        Checks for data availability before returning the longitude.
        """
        if self.data is None:
            return None
        self.set_lon(self.data["coord"]["lon"])
        return self.data["coord"]["lon"]
    
    def get_city(self):
        """Retrieves the city name (if provided) or None.

        Returns the city name if it was set during initialization, otherwise None.
        """
        if self.data is None:
            return None
        if self.city is None:
            return None
        return self.city
    
    def get_units(self):
        """Returns the current temperature units ("metric" or "imperial")."""
        return self.units
    
    def set_units(self, newunits):
        """Sets the temperature units ("metric" or "imperial")."""
        self.units = newunits
        return
    
    def set_city(self, newcity):
        """Sets the city name."""
        self.city = newcity
        return

    def set_coords(self, newlat, newlon):
        """Sets the latitude and longitude coordinates."""
        self.set_lat(newlat)
        self.set_lon(newlon)
        return
    
    def set_lat(self, newlat):
        """Sets the latitude coordinate."""
        self.lat = newlat
        return
    
    def set_lon(self, newlon):
        """Sets the longitude coordinate."""
        self.lon = newlon
        return
    
    def set_temperature(self, temperature):
        """Sets the current temperature (for internal caching)."""
        self.temperature = temperature
        return
    
    def celsius_to_fahrenheit(self, temp_celsius):
        """Converts a temperature from Celsius to Fahrenheit."""
        if temp_celsius is None:
            return None
        newtemp = (temp_celsius * (9/5)) + 32
        self.set_temperature(newtemp)
        return newtemp

    def fahrenheit_to_celsius(self, temp_fahrenheit):
        """Converts a temperature from Fahrenheit to Celsius."""
        if temp_fahrenheit is None:
            return None
        newtemp = (temp_fahrenheit - 32) * (5/9)
        self.set_temperature(newtemp)
        return newtemp

def getWeatherForCity(city_name, api_key, units):
    """Fetches and displays weather data for a given city.

    Args:
        city_name (str): The name of the city.
        api_key (str): Your OpenWeatherMap API key.
        units (str): The desired temperature units ("metric" or "imperial").
    """
    weather = Weather(api_key, city_name, units)
    weather.get_weather()
    weather.display_weather()
    temp = weather.get_temperature()
    if temp is not None: 
        print(f"Current temp: {temp}")
    newtemp = None
    weather_units = weather.get_units()
    if (weather_units == "imperial"):
        newtemp = weather.fahrenheit_to_celsius(temp)
    elif (weather_units == "metric"):
        newtemp = weather.celsius_to_fahrenheit(temp)
    else:
        newtemp = temp
    
    if newtemp is not None:
        print(f"Converted temp: {newtemp:.2f}")
    print(f"Current Units: {weather.get_units()}")

# Usage with improved error handling
YOUR_API_KEY = "YOUR_API_KEY"

try:
    getWeatherForCity("Vancouver", YOUR_API_KEY, "imperial")
except ApiError as e:
    print(f"An error occurred: {e}")
