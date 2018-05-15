import requests
from bs4 import BeautifulSoup
import lxml

url = 'http://www.pythonscraping.com//pages/warandpeace.html'
re = requests.get(url)
suop = BeautifulSoup(re.text,'lxml')
# print(suop)
fall = suop.find_all('span',{'class':'green'})
print(fall)
for T in fall:
    print(T.get_text())