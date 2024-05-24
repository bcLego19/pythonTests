import requests, random
from bs4 import BeautifulSoup
import datetime

url = "https://pixelford.com/blog"
random_num = random.randint(1,999999)
response = requests.get(url, headers={'user-agent': f'Hello{random_num}'})
html = response.content
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('a', class_="entry-title-link")

print("\n== loop through a_tags ==\n")
for a_tag in a_tags:
    print(a_tag.get_text())

titles = list(map(lambda a_tag: a_tag.get_text(), a_tags))

print("\n== titles map with a_tags ==\n")
print(titles)

print("\n== get article tags and drill deeper ==\n")

blogs = soup.find_all('article')
for blog in blogs:
    title = blog.find('a', class_="entry-title-link").get_text()

    blog_datetime_string = blog.find('time', class_="entry-time").get('datetime')
    blog_datetime = datetime.datetime.fromisoformat(blog_datetime_string)
    pretty_date = blog_datetime.strftime("%A, %B %m %Y")

    print(f"{pretty_date} - {title}")