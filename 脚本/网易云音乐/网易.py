import requests
from bs4 import BeautifulSoup
url = 'https://music.163.com/#/song?id=414586202'
headers = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':
    'gzip, deflate, br',
    'Accept-Language':
    'zh-CN,zh;q=0.9',
    'Connection':
    'keep-alive',
    'Cookie':
    '_ntes_nuid=82bd4771f5c0f3261b5e1316033a4c0b; _ntes_nnid=c7103e6f3ce6b6007f36a5300fdb6b1c,1511945798927; mail_psc_fingerprint=39820923da03a3636a0f5b1141bb251d; usertrack=ezq0plpgb2lBT9KzAy8XAg==; __f_=1517291552974; vjuids=-32270483c.161d13cc7ce.0.90f9732ecf64c; vjlast=1519633877.1519633877.30; vinfo_n_f_l_n3=97ddd6403fa06eda.1.2.1517467578559.1517557701068.1519634314112; P_INFO=m17703768649@163.com|1521189119|0|game|00&99|US&1518157364&game#shh&null#10#0#0|177649&1||17703768649@163.com; _ga=GA1.2.469977262.1516269417; JSESSIONID-WYYY=FC3UOinOseo%2FqoQ%5CJndcPSOUwnMM1m1AWga9Wm01hUMTO8p45vvtXtQTB5tyhsf%5CrHoUQrTO8UuPo%5C%5CnnchV03VSS5chGMoY67TFXp3o%5CxsgQ7X%2BqdRGZfzkMA84VVdM2elKje7CpaAHMhjwRt4GjxGTSEGPionxJaZKDkNCoowIy7V%5C%3A1522663173154; _iuqxldmzr_=32; MUSIC_U=8cc1885f5f22df584f4469bd6666e931a84690103e841567b03a54e744472e56536c6d02cb64de3ca9a39641f8ff10a1702bedc37193d5b8b5f4d51ed0099ed7ddb3a88936067446bf122d59fa1ed6a2; __remember_me=true; __csrf=8bb694139400ebb2a59be9c128bcb42d; __utma=94650624.469977262.1516269417.1522659634.1522661917.23; __utmb=94650624.3.10.1522661917; __utmc=94650624; __utmz=94650624.1522661917.23.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'Host':
    'music.163.com',
    'Referer':
    'https://music.163.com/',
    'Upgrade-Insecure-Requests':
    '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
re = requests.get(url, headers=headers).text
soup = BeautifulSoup(re,'lxml')
fall = soup.find_all('div',{'class':'itm'})
print(fall)