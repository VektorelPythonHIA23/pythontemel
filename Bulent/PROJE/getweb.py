import requests
from bs4 import BeautifulSoup as BSP
import time
headers = {'user-agent': 'my-app/0.0.1'}

sayfa = requests.get("https://www.sahibinden.com/kiralik-daire/ankara-cankaya",timeout=100,headers=headers)
time.sleep(3)

soup = BSP(sayfa.content,"html.parser")

# liste1= soup.find_all("div")
liste1 = soup.findAll("div",class_="action-wrapper")
for s in liste1:
    print ''.join(s['class']).strip(), s.text
#liste1= soup.findAll("td",class_="searchResultsAttributeValue")

#print(len(liste1))
#print(liste1)