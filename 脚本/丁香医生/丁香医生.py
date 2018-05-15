import requests
import json
import pymongo

headers = {
    'accept':
    'application/json, text/javascript, */*; q=0.01',
    'accept-encoding':
    'gzip, deflate, br',
    'accept-language':
    'zh-CN,zh;q=0.9',
    'content-type':
    'application/x-www-form-urlencoded',
    'cookie':
    'DOTCOM_SESSIONID=563acfc7-3fa9-48b8-9ec6-4fb52b235e55; DOTCOM_CSRFTOKEN=1e3974d4-433b-44b6-b67f-fb3ad4cfd063; __utmt=1; JSESSIONID=4804AC7A928BE99DBEDB28757494F819; DXY_USER_GROUP=41; __utma=160913314.2073635583.1523328578.1523328578.1523328578.1; __utmb=160913314.9.10.1523328578; __utmc=160913314; __utmz=160913314.1523328578.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __asc=a9f64fd0162ad7575eeea3b4c78; __auc=a9f64fd0162ad7575eeea3b4c78',
    'referer':
    'https://dxy.com/column/new',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
}

client = pymongo.MongoClient('localhost', 27017)  #创建客户端，ip为本地，端口为默认端口27017
db = client['Dingxiang']  #创建数据库名字
collection = db['Zhishi']  #创建集合名字
for num_tage in range(1, 999):
    url = 'https://dxy.com/view/i/columns/article/list?page_index=' + str(
        num_tage) + '&items_per_page=12'
    re = requests.get(url, headers=headers).text
    js = json.loads(re)
    collection.insert(js)  #将数据插入数据库
    for url in js["data"]["items"]:
        try:
            print(url["url"] + "    " + url["title"] + "    " +
                  url["content_brief"])
        except:
            print("跳过")
