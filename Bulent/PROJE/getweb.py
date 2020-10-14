import requests
from bs4 import BeautifulSoup as BSP
import time

r = requests.get("https://www.nasa.gov/centers/armstrong/home/index.html")
time.sleep(3)

kaynak = BSP(r.content,"lxml")
kaynak.
print(kaynak.title)
print(kaynak.find("div").text)