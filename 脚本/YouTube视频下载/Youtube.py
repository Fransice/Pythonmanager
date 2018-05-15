import json
import re
import time
import urllib.parse as urlParse
import os
import io
import requests
from bs4 import BeautifulSoup
from langconv import *
def Traditional2Simplified(sentence):
    ''' 将sentence中的繁体字转为简体字 :param sentence: 待转换的句子 :return: 将句子中繁体字转换为简体字之后的句子 '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence


def Get_dow(file_dow):
    move_dow_url = input("请输入需要下载的视频地址:   ")
    print("正在抓取网页...")
    res = requests.get(move_dow_url).text
    print("正在解析网页...")
    move_url = re.compile('.*?config = (.*?);ytplayer.load.*?', re.S)
    print("正在查找元素...")
    move_url_re = re.findall(move_url, res)
    move_url_re_json = json.loads(move_url_re[0])
    title_old = move_url_re_json["args"]["title"]
    title = title_old.replace('?', '').replace('|', '')
    simplified = Traditional2Simplified(title)  #繁体转简体
    isExists = os.path.exists(file_dow + '\\' + simplified + '.mp4')
    if not isExists:
        url_dow = urlParse.parse_qs(
            move_url_re_json["args"]["url_encoded_fmt_stream_map"])
        re_move_url = url_dow["url"][0]
        re_move = requests.get(re_move_url)
        print("正在下载数据...    " + simplified)
        with open(file_dow + '\\' + simplified + '.mp4', 'wb') as fp:
            fp.write(re_move.content)
            fp.close()
            print("下载完成...")
    else:
        print(simplified + "   已经存在...")


def start():
    num = input("请输入需求编号: ①:单次下载  ②:多次下载   ")
    if num == 1:
        file_dow = input("请输入下载视频的存放地址:   ")
        Get_dow(file_dow)
    else:
        file_dow = input("请输入下载视频的存放地址:   ")
        while True:
            Get_dow(file_dow)


if __name__ == '__main__':
    start()