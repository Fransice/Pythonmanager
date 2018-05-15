import io
import requests
import json

url = 'https://wallions.com/api/feed'
with open('data.txt', 'r', encoding='utf-8') as trye:
    print(trye.read() + "读取")
    data = trye.read()
    trye.close()
headers = {
    'accept-language':
    'zh-CN,zh;q=0.9 ',
    'content-type':
    'application/x-www-form-urlencoded; charset=UTF-8 ',
    'cookie':
    '__cfduid=d2fc18ad774180ffa7fed6e6b695ede9a1515735177; _ga=GA1.2.556657307.1522033187; _gid=GA1.2.2100614066.1522033187; _gat=1 ',
    'user-agent ':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
#json数据格式化
r = requests.post(url, data=data,headers = headers).text
# print(r)
x = json.loads(r)
print(x["feed"]["last"])
x = x["posts"]
print(x)
print(x[-1]["_id"])

print(x[-2]["_id"])

print(x[-3]["_id"])

print(x[-4]["_id"])
# print(x["feed"]["last"] + '    x["feed"]["last"]写入')
# print(x["posts"][19]["_id"])
# Fdata = '"last:":"{0}"'.format(x["feed"]["last"])
# print(Fdata)
