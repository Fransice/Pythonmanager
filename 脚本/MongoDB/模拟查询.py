import pymongo
import requests
import os
# 建立与mongodb的连接
client = pymongo.MongoClient('localhost', 27017)
# 得到数据库
stu = client['bilibili']
# 得到一个数据集合
message = stu['move']
#计算表中数据条数
print(message.count())
#满足条件的表的数据
print(message.find({"title": "【催泪向/治愈/毕业向】我是否还能在你身边？！"}).count())
path = 'D:/PythonManager/B站视频标题图片/'
for num in message.find():
    title = num["title"]
    img_url = num["pic"]
    isExists = os.path.exists(path + '/' + img_url[32:])
    #图片判断
    if not isExists:
        re = requests.get(img_url)
        print("正在下载:  " + title)
        with open(path + img_url[32:], 'wb') as fp:
            fp.write(re.content)
    else:
        print("已下载: " + title)
#     print(title)
#     try:
#         with open("bilibili.txt", 'a', encoding='utf-8') as fp:
#             fp.write(num["title"] + "\n")
#             fp.write("视频地址:https://www.bilibili.com/video/av" +
#                      str(num["aid"]) + "\n")
#             fp.write("标题图片地址:" + num["pic"] + "\n\n")
#             print("正在导入..." + num["title"])
#     except:
#         print("c")
# print("导入完成")

#查找一条数据
# print(message.find_one())
#查找指定数据
# data = message.find_one({'title': '【催泪向/治愈/毕业向】我是否还能在你身边？！'})
# print(data['title'])
# print(data['desc'])
# print(data["dynamic"])