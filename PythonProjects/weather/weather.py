import requests

class Weather:
  def __init__(self, city, api_key):
    self.city = city
    self.api_key = api_key
    self.temperature = None

  def get_weather(self):
    # Build the API request URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
    # Make the API request using requests library (assumed installed)
    response = requests.get(url)

    # Check for successful response
    if response.status_code == 200:
      # Parse the JSON data
      data = response.json()
      # Extract temperature in Kelvin
      self.temperature = data["main"]["temp"]
    else:
      print(f"Error retrieving weather data for {self.city}")

  def convert_to_fahrenheit(self):
    # Check if temperature is retrieved first
    if self.temperature is None:
      print("Weather data not available. Please call get_weather() first.")
      return
    # Conversion formula: Fahrenheit = (Celsius x 9/5) + 32
    fahrenheit = (self.temperature * 9/5) + 32
    return fahrenheit

  def display_weather(self):
    # Check if temperature is retrieved first
    if self.temperature is None:
      print("Weather data not available. Please call get_weather() first.")
      return
    # Display city, temperature in Celsius and Fahrenheit with f-strings
    print(f"City: {self.city}")
    print(f"Temperature: {self.temperature:.2f} °C")
    print(f"Temperature: {self.convert_to_fahrenheit():.2f} °F")

# Replace with your desired city
city = "Vancouver"
# Update with the provided API key
api_key = "YOUR_API_KEY"

# Create a Weather object
weather = Weather(city, api_key)

# Call get_weather() to retrieve data
weather.get_weather()

# Display the weather information
weather.display_weather()
