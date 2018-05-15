import requests
import pymongo
import time
client = pymongo.MongoClient("localhost", 27017)
stu = client["hero"]
message = stu["sheet_tab"]
for messag in message.find():
    text = messag["title"]
    name = messag["name"]
    tags = messag["tags"]
    story = messag["story"]
    desp = name + '\n\n' + tags + '\n\n' + story
    ##@@作业通道
    api = 'https://pushbear.ftqq.com/sub'
    sky = '3169-3654ed02dcdc5efcd94204c0eb3d4a66'
    http = 'https://pushbear.ftqq.com/sub?sendkey=' + sky + '&text=' + text + '&desp=' + desp
    re = requests.get(http)
    print(re.text)
    print('发送完成')
    break