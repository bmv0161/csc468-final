import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://ramconnect.wcupa.edu/events')

soup = BeautifulSoup(page.content, 'html.parser')
html = list(soup.children)[3]
ultag = soup.find('ul', {'class': 'list-group'})
print(ultag)
litag = ultag.find_all('li', {'class': 'list-group-item'})
print(list(litag))
