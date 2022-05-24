import requests
import re
from bs4 import BeautifulSoup

res = requests.get('https://www.portofoakland.com/')
res.raise_for_status()

soup = BeautifulSoup(res.text,'html.parser')


for link in soup.find_all('a'):
    s = re.match('^https://.*Supplemental-Board-Agenda.pdf$',link.get('href'))
    if s:
        break

res = requests.get(s.string)
res.raise_for_status

playFile = open('board-Agenda.pdf','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
