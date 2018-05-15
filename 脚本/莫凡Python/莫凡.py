import requests
from bs4 import BeautifulSoup
import lxml
import re

ip_data = "47.94.230.42"
#端口
port_data = "9999"
#固定IP格式
new_data = {"http": ip_data + ":" + port_data}
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36Name'
}


def start():
    url = "https://morvanzhou.github.io/"
    res = requests.get(url, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    url = soup.find_all('ul', {'class', 'tut-course-thumbnail'})
    for url_list in url:
        re_s = re.compile('.*?href="(.*?)">.*?<img', re.S)
        url_s = re.findall(re_s, str(url_list))
        for u in url_s:
            neibu("https://morvanzhou.github.io" + u)


def neibu(url):
    re_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(re_text, 'lxml')
    url_Mo = soup.find_all('li', {'class', 'content-li'})
    # print(url_Mo)
    for url_try in url_Mo:
        re_s = re.compile('.*?href="(.*?)">', re.S)
        url_s = re.findall(re_s, str(url_try))
        title_re = re.compile('<a.*?>(.*?)</a>', re.S)
        title = re.findall(title_re, str(url_try))
        for u in range(len(title)):
            with open('莫凡Python.txt', 'a', encoding='utf-8') as fp:
                fp.write("https://morvanzhou.github.io" + url_s[u] +
                         "           " + title[u])
            print("https://morvanzhou.github.io" + url_s[u] + "           " +
                  title[u])


if __name__ == '__main__':
    start()