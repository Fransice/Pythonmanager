import requests

url = 'http://www.weather.com.cn/weathern/101180111.shtml?from=map'
re = requests.get(url).text
print(re)