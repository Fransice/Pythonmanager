import re

import lxml
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9',
    'Cookie':
    'UM_distinctid=16188c6eab83b5-0445f4eb19f4e8-5b44271d-1fa400-16188c6eab92e7; Hm_lvt_797989aab9eddb7974bca5b800e7d2a9=1519870291,1519891432,1519953134,1519966079; CNZZDATA1273011690=1179581255-1520209849-null%7C1520209849; CNZZDATA1256195895=975798138-1522643957-%7C1522643957; Hm_lvt_dcb5060fba0123ff56d253331f28db6a=1521507037,1521789235,1522372329,1522631545; Hm_lpvt_dcb5060fba0123ff56d253331f28db6a=1522647152',
    'Host':
    'www.gamersky.com',
    'Proxy-Connection':
    'keep-alive',
    'Referer':
    'http://www.gamersky.com/ent/201804/1031628_9.shtml',
    'Upgrade-Insecure-Requests':
    '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
headers_dow = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9',
    'Cache-Control':
    'max-age=0',
    'Host':
    'wx2.sinaimg.cn',
    'If-Modified-Since':
    'Mon, 08 Jul 2013 18:06:40 GMT',
    'Proxy-Connection':
    'keep-alive',
    'Upgrade-Insecure-Requests':
    '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
headers_text = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9',
    'Cache-Control':
    'max-age=0',
    'Cookie':
    '__cfduid=d0c12a100b9068a467e7d2d99bc0fc03b1522650780; foreign_referer=http%3A%2F%2Faccount.fir.im%2Fusers%2Fvalid_real_name; Hm_lvt_11417a0de2093ccfc6a808f3fbf8113a=1522651678; Hm_lpvt_11417a0de2093ccfc6a808f3fbf8113a=1522651720; mp_4fb7314d7432f6c41d795199438b703d_mixpanel=%7B%22distinct_id%22%3A%20%225ac1cf3730c0617e038f3f49%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Ffir.im%2F%22%2C%22%24initial_referring_domain%22%3A%20%22fir.im%22%7D; _ga=GA1.2.1180636450.1522650616; mp_mixpanel__c=36\'Host:firicon.fir.im',
    'If-Modified-Since':
    'Mon, 02 Apr 2018 06:50:36 GMT',
    'If-None-Match':
    '"FldwFgm9zoXhIaQQ_bn3pWLza2VL"',
    'Proxy-Connection':
    'keep-alive',
    'Upgrade-Insecure-Requests':
    '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
url = 'http://www.gamersky.com/ent/201804/1031628.shtml'
url1 = 'http://www.gamersky.com/ent/201804/1031573.shtml'
re = requests.get(url, headers=headers)
suop = BeautifulSoup(re.text, 'lxml')
img_url = suop.find_all('img', {'class': 'picact'})
for img in img_url:
    print(img.attrs['src'])
    re_url = img.attrs['src']
    re_img = requests.get(
        'http://firicon.fir.im/5d00e628a27606619f68071dd7e7fe84f4bd68bb?e=1522653094&token=LOvmia8oXF4xnLh0IdH05XMYpH6ENHNpARlmPc-T:MpeBEGXV9U0wQfEx2XbBOJPgSaM=',
        headers=headers_text)
    with open('1.jpg', 'wb') as fp:
        fp.write(re_img.content)
        fp.close()