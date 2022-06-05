import json
import requests
from bs4 import BeautifulSoup
# https://web.archive.org/web/20220310110507/https://www.imdb.com/title/tt0080684/
url = input()
r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
soup = BeautifulSoup(r.content, 'html.parser')
html_j = json.loads(soup.find('script', type='application/ld+json').string)
print(html_j['alternateName'])

# dict_tags = {"title": f"{title}", "description": f"{description}"}

