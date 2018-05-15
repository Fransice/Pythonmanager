import io
import json

import requests

import _thread

#照片下载地址
#初始标记
handers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
Once = 0


def Get_url():
    url = 'https://wallions.com/api/feed'
    #第一次运行读取文件的data值
    with open('data.txt', 'r', encoding='utf-8') as trye:
        print(trye.read() + "读取")
        data = trye.read()
        trye.close()
    #json数据格式化
    r = requests.post(url, data=data).text
    x = json.loads(r)

    print(x["feed"]["last"] + '    x["feed"]["last"]写入')
    Fdata = '"last:":"{0}"'.format(x["feed"]["last"])
    print(Fdata)
    with open('data.txt', 'w', encoding='utf-8') as fp:
        fp.write(Fdata)
        fp.close()
    with open('data.txt', 'r', encoding='utf-8') as trye:
        data = trye.read()
        trye.close()
    # print(r)
    #头信息
    # datalast = {'last': '{0}'.format(x["feed"]["last"])}
    # print(datalast)
    print("头信息" + x["feed"]["last"])
    #刷新一次图片的个数
    lens = len(x["posts"])
    #依次取出图片并下载
    for id in range(lens):
        postid = x["posts"][id]["postId"]
        http = ('https://wallions.com/uploads/post-thumbs/w1920/{0}.jpg'.
                format(postid))
        photo = requests.get(http, headers=handers)
        with open('D:/PythonManager/wallions图片下载/图片/{0}.jpg'.format(postid), 'wb') as f:
            print("正在下载:" + str(postid) + ".jpg")
            f.write(photo.content)
            f.close()
    print("#####################")


if __name__ == '__main__':
    var = 1
    while var == 1:
        Get_url()
