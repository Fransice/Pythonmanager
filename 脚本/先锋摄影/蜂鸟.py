import io
import json
import os
import re
import threading
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
    'Cache-Control':
    'max-age=0',
    'Connection':
    'keep-alive',
    'Cookie':
    'Hm_lvt_916ddc034db3aa7261c5d56a3001e7c5=1522199377,1522288512',
    'Host':
    'bbs.fengniao.com',
    'Upgrade-Insecure-Requests':
    '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
dow_headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36Name'
}


def select_url():
    url_all_list = [
        'http://bbs.fengniao.com/ajax/ajaxJinghua.php?page={0}&forumid=1',      #手机摄影
        'http://bbs.fengniao.com/ajax/ajaxJinghua.php?page={0}&forumid=476',    #鸟类
        'http://bbs.fengniao.com/ajax/ajaxJinghua.php?page={0}&forumid=30',     #宠物
        'http://bbs.fengniao.com/ajax/ajaxJinghua.php?page={0}&forumid=20',     #纪实
        'http://bbs.fengniao.com/ajax/ajaxJinghua.php?page={0}&forumid=15',     #旅行
        'http://bbs.fengniao.com/ajax/ajaxJinghua.php?page={0}&forumid=125',    #风光
        'http://bbs.fengniao.com/ajax/ajaxJinghua.php?page={0}&forumid=297',    #儿童
        'http://bbs.fengniao.com/ajax/ajaxJinghua.php?page={0}&forumid=27',     #新手
        'http://bbs.fengniao.com/ajax/ajaxJinghua.php?page={0}&forumid=115',    #生活
        'http://bbs.fengniao.com/ajax/ajaxJinghua.php?page={0}&forumid=101',    #人像
        'http://bbs.fengniao.com/ajax/ajaxJinghua.php?page={0}&forumid=16',     #生态
    ]
    print('请输入指定数字选择下载图片类型:  ')
    print(
        '           1.手机摄影   2.鸟类   3.宠物   4.纪实   5.旅行   6.风光   7.儿童   8.新手   9.生活   10.人像   11.生态'
    )
    input_get_url_num = input()
    if input_get_url_num == '1':
        collection_get_url(url_all_list[0], '手机摄影')
    elif input_get_url_num == '2':
        collection_get_url(url_all_list[1], '鸟类')
    elif input_get_url_num == '3':
        collection_get_url(url_all_list[2], '宠物')
    elif input_get_url_num == '4':
        collection_get_url(url_all_list[3], '纪实')
    elif input_get_url_num == '5':
        collection_get_url(url_all_list[4], '旅行')
    elif input_get_url_num == '6':
        collection_get_url(url_all_list[5], '风光')
    elif input_get_url_num == '7':
        collection_get_url(url_all_list[6], '儿童')
    elif input_get_url_num == '8':
        collection_get_url(url_all_list[7], '新手')
    elif input_get_url_num == '9':
        collection_get_url(url_all_list[8], '生活')
    elif input_get_url_num == '10':
        collection_get_url(url_all_list[9], '人像')
    elif input_get_url_num == '11':
        collection_get_url(url_all_list[10], '生态')
    else:
        print('输入错误,请重新输入!')
        select_url()

def collection_get_url(all_url, sort_folder):
    for url_count in range(1, 999999):
        #第一界面
        collection_url = all_url.format(url_count)
        print('☞   ' + '正在获取 ' + collection_url)
        collection_json_text = requests.get(
            collection_url, headers=headers).text
        json_python = json.loads(collection_json_text)
        content = json_python["content"]
        leagth = len(content)
        #第二界面
        for eage in range(leagth):
            folder_title = json_python["content"][eage]["title"]
            atlas = json_python["content"][eage]["picUrl"]
            dow_atlas = requests.get(atlas, headers=dow_headers)
            #第三界面
            soup = BeautifulSoup(dow_atlas.text, 'lxml')
            re_json = re.compile('<script>.*?var picList =(.*?);', re.S)
            json_url = re.findall(re_json, str(soup))
            count = len(json_url)
            try:
                json_url_list = json_url[count - 1]
                Writer(str(json_url_list))
                Made(folder_title, json_url_list, sort_folder)  
            except:
                print('☺   ' + '该帖子已被删除')
                pass


def dow_img(path, img_json):
    img_json_json = json.loads(img_json)
    img_count = len(img_json_json)
    for img_count_get in range(img_count):
        img_url = img_json_json[img_count_get]["downloadPic"]
        img_name = img_json_json[img_count_get]["pid"]
        isExists = os.path.exists(path + '\\' + img_name + '.jpg')
        #图片判断
        if not isExists:
            img_content = requests.get(img_url, headers=dow_headers)
            with open(path + '\\' + img_name + '.jpg', 'wb') as fp:
                print('※  ' + '正在下载: ' + img_name + '.jpg')
                fp.write(img_content.content)
                fp.close()
        else:
            print('卐  ' + img_name + '.jpg' + '图片已经存在,不再下载')


def Writer(content):
    with open('text.txt', 'w') as fp:
        fp.write(content)
        fp.close()


def Made(folder, url_json, sort_folder):
    path = 'D:\\Python图片下载专属文件夹\\' + sort_folder + '\\' + folder
    #创建文件夹
    isExists = os.path.exists(path)
    if not isExists:
        print('※  ' + '正在创建文件夹:{0}'.format(path))
        os.makedirs(path)
        dow_img(path, url_json)
    else:
        print('卐  ' + path + ' 目录已存在')
        dow_img(path, url_json)


if __name__ == '__main__':
    select_url()