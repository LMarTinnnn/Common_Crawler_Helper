import requests
from bs4 import BeautifulSoup
from SoupRefiner import SoupRefiner
from config import headers

response = requests.get('https://github.com/LMarTinnnn', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
sr = SoupRefiner(soup, response.url)

print('-----------------------External Links-----------------------')
external_links = sr.get_external_links()
for link in external_links:
    print(link)

print('-----------------------Internal Links-----------------------')
internal_links = sr.get_internal_links()
for link in internal_links:
    print(link)

print('-----------------------  Images -----------------------')
imgs = sr.get_all_imgs()
for url in imgs:
    print(url)
