import pymongo
import json
import tushare as ts

df=ts.get_hist_data('601688')#获取华泰的日线数据
print("数据获取完成")
data=json.loads(df.to_json(orient='records'))#json格式顺序为records
print("正在连接数据库...")
client=pymongo.MongoClient('localhost',27017)#创建客户端，ip为本地，端口为默认端口27017
db=client['Huatai']#创建数据库名字
collection=db['collectionname']#创建集合名字
print("正在写入数据...")
collection.insert(data)#将数据插入数据库
print("数据处理完成")