import requests
url = 'https://tieba.baidu.com/ '
hraders = {
    'Accept':
    'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':
    'gzip, deflate, br',
    'Accept-Language':
    'zh-CN,zh;q=0.9',
    'Connection':
    'keep-alive',
    'Cookie':
    'BAIDUID=A9F9F85BD6B0A2BA85D9BD85B4CC9AB2:FG=1; BIDUPSID=A9F9F85BD6B0A2BA85D9BD85B4CC9AB2; PSTM=1511774301; TIEBAUID=91d2c8f7ed33eab2ceecd637; TIEBA_USERTYPE=2c5edaeff0ad6982299fdec4; bdshare_firstime=1511774223747; MCITY=-289%3A; pgv_pvi=645565440; _ck_uName=1521790743318464937879; FP_UID=21d00416d0d4fcb89bf4b7139e2a57de; last_login_type=2; AuthInfo=eyJ1c2VyaWQiOiI1Njc0ODc3IiwidXNlcm5hbWUiOiIxNzkxNjQ1MzY1QGF1dG9iYWlkdS5jb20iLCJuaWNrbmFtZSI6Ilx1NGUwM1x1OTZmZWkiLCJoYXNoIjoiNTg2Y2Q5NjhkMjNlNjM2YTJmYTg2YmY5OGIyYTg2MTEifQ%3D%3D; BDUSS=lhMVB0VERWWXUyWmtSYjhYSHJkWWZNZGtnakt6Wk1sLVhxMUYxSFFVWjJHLUJhQVFBQUFBJCQAAAAAAAAAAAEAAAC1VspqtrpnZGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHaOuFp2jrhaNk; STOKEN=4373e645e8908cea72032fb7167b950670b6ed8dafc52b9301a7122de8259c24; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1520999271,1521183959,1521602296,1522485171; cflag=15%3A3',
    'Host':
    'tieba.baidu.com',
    'Referer':
    'https://tieba.baidu.com/',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
re = requests.get(url,headers = hraders).text
print(re)