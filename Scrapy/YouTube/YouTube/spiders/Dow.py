# -*- coding: utf-8 -*-
import scrapy
import json
import requests
import re
import urllib.parse as urlParse


class DowSpider(scrapy.Spider):
    name = 'Dow'
    allowed_domains = ['youtube.com']

    def start_requests(self):
        dow_url = [
            "/watch?v=T5UIySP9Owc",
            "/watch?v=RddEKFTVpwE&t",
            "/watch?v=Y2t68jDwfhc&t",
            "/watch?v=fPVpMai99gA&t",
            "/watch?v=4DHcOPSfC4c&t",
            "/watch?v=6HGbKdB4kVY",
            "/watch?v=hF-dJj559ug",
            "/watch?v=kYSxf1V-VV4",
            "/watch?v=sy3RBqeDNoY",
            "/watch?v=dcvTM4O0wiM",
            "/watch?v=lXEGO2OoL34",
            "/watch?v=wZ48Gjb-k2U",
            "/watch?v=jV6eHoLzD2E",
            "/watch?v=xd_1rn89W2k",
            "/watch?v=31DZfkYRvI4",
            "/watch?v=uS1HYKHMuDQ",
            "/watch?v=8wo9ckJCTsw",
            "/watch?v=Y9w95eREzxs",
            "/watch?v=Wbk9hxntMjY&t",
            "/watch?v=C4JUEKNkJlc",
            "/watch?v=-c5rrzjsN34&t",
            "/watch?v=HeXKNCI-CWc",
            "/watch?v=vOjRcxTLUEI",
            "/watch?v=dxnIyBeVhws",
            "/watch?v=EGnAxXmQC6Y",
            "/watch?v=3A1Q3_IPNkA",
            "/watch?v=gCd3Fh9w3Do",
            "/watch?v=49Mwqbu2cMo",
            "/watch?v=2xjAArPnOH8",
            "/watch?v=KSA12AKDr_o",
            "/watch?v=Xq4yRuePSdk",
            "/watch?v=Me9SpR0SE08",
            "/watch?v=w4PPlkJFzCo",
            "/watch?v=fnwvYAtCFko",
            "/watch?v=0pWJHy_fNWA",
            "/watch?v=h2hYbl8Mg8o",
            "/watch?v=czPBBKO_JQY",
            "/watch?v=OLw1elIl0HA",
            "/watch?v=vVBAHXBQets",
            "/watch?v=Fef68FgfAbU",
            "/watch?v=Da0LuZeeILI",
            "/watch?v=4bBtE8ZIDKk&t",
            "/watch?v=9unqUH0PYCI",
            "/watch?v=MQH4Rau_F_A",
            "/watch?v=DF47h_hhGZw",
            "/watch?v=oSVCSFBcE4U",
            "/watch?v=4NFHIW43GAY",
            "/watch?v=hdNdGolUy6o",
            "/watch?v=PYy5C9IIgp8",
            "/watch?v=oG0HZogxEUc",
            "/watch?v=x-1buhvY4T4",
            "/watch?v=qkRpQJwsa6Q",
            "/watch?v=G5MDpnGsE-k",
            "/watch?v=DXkSHN1zqI0",
            "/watch?v=jtgfCgctWOw",
            "/watch?v=A9aEBXH0AwE",
            "/watch?v=g49HtnX3SOo",
            "/watch?v=zmHVG6c_kFo",
            "/watch?v=KESG8I9C3oA",
            "/watch?v=ZE9cAXpfHAU",
            "/watch?v=k2JqyTA1B2I",
            "/watch?v=xWICyTVSIQs",
            "/watch?v=Y5Cqws3v1Ck",
            "/watch?v=kmaLelILvb8",
            "/watch?v=N1Ypt77GbF4",
            "/watch?v=fX3dmNmxMCw",
            "/watch?v=mmNNmbxzSLA",
            "/watch?v=zzMRbrOHlrk",
            "/watch?v=_0WTohwhPHk",
            "/watch?v=pudl3-BzFok",
            "/watch?v=CDwUsqpgYpU",
            "/watch?v=YvR39jTbcRc",
            "/watch?v=6f2O4LEU058",
            "/watch?v=Ef0kh6NPiBE",
            "/watch?v=PzCP8cenOEc",
            "/watch?v=ceUhb2-gYOU",
            "/watch?v=woJ2ZpQ1Q9I",
        ]
        for dow in dow_url:
            yield scrapy.Request(
                url="https://www.youtube.com" + dow, callback=self.parse)

    def parse(self, response):
        # print(response + "response")
        print("response")
        re_text = requests.get(response).text
        print(re_text)
        move_url = re.compile('.*?config = (.*?);ytplayer.load.*?', re.S)
        move_url_re = re.findall(move_url, re_text)
        move_url_re_json = json.loads(move_url_re[0])
        # title_old = move_url_re_json["args"]["title"]
        # title = title_old.replace('?', '')
        url_dow = urlParse.parse_qs(
            move_url_re_json["args"]["url_encoded_fmt_stream_map"])
        re_move_url = url_dow["url"][0]
        print(re_move_url)
        yield re_move_url
