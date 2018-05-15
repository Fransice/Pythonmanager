import requests
import pymongo
import time
client = pymongo.MongoClient("localhost", 27017)
stu = client["hero"]
message = stu["sheet_tab"]
# message = message.find_and_modify()
messag = message.find()
print(messag)
# title = messag["title"]
# name = messag["name"]
# tags = messag["tags"]
# story = messag["story"]
# text = title + '\n' + name + '\n\n' + tags + '\n\n' + story
# html = 'https://sc.ftqq.com/SCU23618T95a82ecb6f52f232377c936cb993fe4c5ab4755bdde27.send?text=' + text
# # re = requests.get(html)
# # print(re.text)
# print('发送成功')
# break
