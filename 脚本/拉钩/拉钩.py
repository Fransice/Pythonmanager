from bs4 import BeautifulSoup
import requests
import lxml
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36Name'
}
url = 'https://www.lagou.com/jobs/list_unity3d?px=default&city=%E5%85%A8%E5%9B%BD#filterBox'
re = requests.get(url,headers = headers)
soup = BeautifulSoup(re.text,'lxml')
print(soup.select())