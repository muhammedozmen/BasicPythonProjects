import requests
from bs4 import BeautifulSoup

url = "https://alant1.itch.io/"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
title = soup.find_all('div', {'class': 'user_profile formatted'})

for t in title:
    print(t.getText())