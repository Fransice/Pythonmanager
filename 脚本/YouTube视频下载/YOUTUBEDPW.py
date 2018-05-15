import requests
import json
import re
import lxml
from lxml import etree

url = "https://www.youtube.com/watch?v=Dm6-EOVz57c&list=PLO5e_-yXpYLAgYbukePjfL-aamW0HWMtk"
res = requests.get(url).text
# print(res)
move_title_Json = re.compile('.*?data-video-title="(.*?)".*?<a href="(.*?)" class=" spf-link  playlist-video clearfix  yt-uix-sessionlink      spf-link ".*?', re.S)
move_title_re = re.findall(move_title_Json, res)
print(move_title_re[0])
for target_list in move_title_re:
    print(target_list)