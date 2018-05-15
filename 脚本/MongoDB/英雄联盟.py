import pymongo
import requests
from bs4 import BeautifulSoup

#建立于MongoClient 的连接
client = pymongo.MongoClient('localhost', 27017)
#得到数据库
hero = client['hero']
#得到一个数据集合
sheet_tab = hero['sheet_tab']
url = 'http://lol.duowan.com/hero/'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
links = soup.find(id="champion_list").find_all('a')
for link in links:
    link = link['href']
    requ = requests.get(link)
    sop = BeautifulSoup(requ.text, 'html.parser')
    data = {
        'title':
        sop.find('h2', class_="hero-title").get_text(),
        'name':
        sop.find('h1', class_="hero-name").get_text(),
        'tags':
        sop.find('div',
                 class_="hero-box ext-attr").find_all('span')[1].get_text(),
        'story':
        sop.find('div', class_="hero-popup").find_all('p')[0].get_text(),
    }
    sheet_tab.insert_one(data)