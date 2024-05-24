import requests

url = "https://linkedin.com"
response = requests.get(url)
print(response.content)