import requests
import re
import lxml
from lxml import etree
from bs4 import BeautifulSoup

url = "http://www.acg.fi/zhifu"
re_Test = requests.get(url).text  
soup = BeautifulSoup(re_Test,'lxml')
url_Test = soup.find_all('a', class_="link-block")
re_U = re.compile("<a class=.*?href=(.*?)>.*?",re.S)
# for target_list in url_Test:
re_T = re.findall(re_U,re_U)
for target_list in re_T:
    print(target_list)
print(re_T)
    # print(target_list)
# print(url_Test)
# re_Url = re.compile("class="preview thumb-in"></div><a href="",re.S)

html = """<a class="link-block" href="http://www.acg.fi/zhifu/45888.htm"></a>"""
re_U = re.compile("<a class=.*?href=(.*?)>.*?",re.S)
re_T = re.findall(re_U,html)
print(re_T)