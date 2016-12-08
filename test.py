import requests
from bs4 import BeautifulSoup
from SoupRefiner import SoupRefiner
from config import headers, proxies

response = requests.get('https://www.zhihu.com', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
print(soup.prettify())
sr = SoupRefiner(soup, response.url)

print('-----------------------External Links-----------------------')
external_links = sr.get_external_links()
for link in external_links:
    print(link)

print('-----------------------Internal Links-----------------------')
internal_links = sr.get_internal_links()
for link in internal_links:
    print(link)
