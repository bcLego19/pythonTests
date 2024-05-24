import requests, random

url = "https://pixelford.com/blog"
random_num = random.randint(1,999999)
response = requests.get(url, headers={'user-agent': f'Hello{random_num}'})
print(response.content)