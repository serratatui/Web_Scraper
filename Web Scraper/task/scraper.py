import json
import requests
from bs4 import BeautifulSoup
import html
import string
import os

# stage 2/5
# class Request:
#     def __init__(self, url):
#         self.url = url
#         self.r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
#         self.soup = BeautifulSoup(self.r.content, 'html.parser')
#
#     def get_page(self, name):
#         return html.unescape(json.loads(self.soup.find('script', type='application/ld+json').string)[name])
#
#
# url_in = input('Input the URL:')
# try:
#     req = Request(url_in)
#     if 'title' in url_in:
#         print({'title': req.get_page('name'), 'description': req.get_page('description')})
#     else:
#         raise Exception
# except:
#     print('Invalid movie page!')
# stage 3/5
# inp_url = input('Input the URL:')
#
# if requests.get(inp_url).status_code == 200:
#     page_content = requests.get(inp_url).content
#     with open('source.html', 'wb') as f:
#         f.write(page_content)
#     print('Content saved.')
# else:
#     print(f'The URL returned {requests.get(inp_url).status_code}')
# stage 4/5
# r = requests.get("https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3", headers={'Accept-Language': 'en-US,en;q=0.5'})
# soup = BeautifulSoup(r.content, 'html.parser')
# page_blocks = soup.find_all("div", {"class": "u-full-height"})
# news_blocks = [el for el in page_blocks if '<span class="c-meta__type">News</span>' in str(el)]
# # second parse
# piece_soup = BeautifulSoup(str(news_blocks), 'html.parser')
# title_href = piece_soup.find_all("a", {"class": "c-card__link u-link-inherit"})
# title_href = ["https://www.nature.com" + el.get("href") for el in title_href]
# # get json
# for href in title_href:
#     r = requests.get(href, headers={'Accept-Language': 'en-US,en;q=0.5'})
#     soup = BeautifulSoup(r.content, 'html.parser')
#     title = html.unescape(json.loads(soup.find('script', type='application/ld+json').string)["mainEntity"]["headline"])
#     valid_title = "".join([letter for letter in title if letter not in string.punctuation+"\n"]).replace(" ", "_")
#
#     with open(f'{valid_title}.txt', 'wb') as f:
#         f.write(soup.find("div", {"class": "c-article-body u-clearfix"}).get_text().strip().encode('utf-8'))

# stage 5/5
num = input()
type = input()

def get_page(num, type):
    r = requests.get(f"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={num}", headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(r.content, 'html.parser')
    page_blocks = soup.find_all("div", {"class": "u-full-height"})
    news_blocks = [el for el in page_blocks if f'<span class="c-meta__type">{type}</span>' in str(el)]
    # second parse
    piece_soup = BeautifulSoup(str(news_blocks), 'html.parser')
    title_href = piece_soup.find_all("a", {"class": "c-card__link u-link-inherit"})
    title_href = ["https://www.nature.com" + el.get("href") for el in title_href]
    # get json
    for href in title_href:
        r = requests.get(href, headers={'Accept-Language': 'en-US,en;q=0.5'})
        soup = BeautifulSoup(r.content, 'html.parser')
        title = html.unescape(json.loads(soup.find('script', type='application/ld+json').string)["mainEntity"]["headline"])
        valid_title = "".join([letter for letter in title if letter not in string.punctuation+"\n"]).replace(" ", "_")

        with open(f'Page_{num}//{valid_title}.txt', 'wb') as f:
            f.write(soup.find("div", {"class": "c-article-body u-clearfix"}).get_text().strip().encode('utf-8'))


for i in range(1, int(num) + 1):
    os.mkdir(f"Page_{str(i)}")
    get_page(str(i), type)

