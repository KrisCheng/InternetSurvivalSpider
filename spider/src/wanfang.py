#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 24/12/2018

# TODO

import requests
import urllib.request
from selenium import webdriver

def get_html(url):
    try:
          header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331', }
          r=requests.get(url,headers = header,verify=False)
          r.raise_for_status
          r.encoding=r.apparent_encoding
          #print(r.text)
          return r
    except Exception as e:
        print("has error:"+str(e))

def getFile(url):
    file_name = "1.pdf"
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)


def main_task():
    # url = "http://www.wanfangdata.com.cn/local/toFullText.do?item_id=1226135&item_num=002&gazetteers_id=FZ001108"
    # url = "http://www.wanfangdata.com.cn/pay/downloadliterature.do?type=local+chronicles&title=%E5%A4%A9%E6%B4%A5%E6%B0%B4%E5%88%A9%E5%BF%97%C2%B7%E5%8D%B7%E5%8D%81%E4%BA%8C%C2%B7%E5%8C%97%E8%BE%B0%E5%8C%BA%E6%B0%B4%E5%88%A9%E5%BF%97&id=1545393&isresult=false&transaction=%7B%22id%22%3Anull%2C%22transferOutAccountsStatus%22%3Anull%2C%22transaction%22%3A%7B%22id%22%3A%221077423534843650048%22%2C%22status%22%3A1%2C%22createDateTime%22%3Anull%2C%22payDateTime%22%3A1545712762925%2C%22authToken%22%3A%22TGT-2587037-DqFaf10Nch9OcSYYzyCVssUxacnBBRZEXRDlL32reus5RqIRCj-my.wanfangdata.com.cn%22%2C%22user%22%3A%7B%22accountType%22%3A%22Group%22%2C%22key%22%3A%22tjdxtsg%22%7D%2C%22transferIn%22%3A%7B%22accountType%22%3A%22Income%22%2C%22key%22%3A%22LocalChronicleItemFulltext%22%7D%2C%22transferOut%22%3A%7B%22GTimeLimit.tjdxtsg%22%3A0.5%7D%2C%22turnover%22%3A0.5%2C%22orderTurnover%22%3A0.5%2C%22productDetail%22%3A%22local+chronicles_1545393%22%2C%22productTitle%22%3Anull%2C%22userIP%22%3A%22111.187.51.93%22%2C%22organName%22%3Anull%2C%22memo%22%3Anull%2C%22orderUser%22%3A%22tjdxtsg%22%2C%22orderChannel%22%3A%22pc%22%2C%22payTag%22%3Anull%2C%22webTransactionRequest%22%3Anull%2C%22signature%22%3A%22DqmiXkghmHA51nn7ixRmwgS6lKg6tgRN8j8oVU6cnQkIM9vV57ApyshdS7zsZo6izyHqWx1aGCYC%5CnwN3bD1vXsQm2CeIDSUoI52jJqX5jCu0I0VMJHDZXXnUkpEcsB%2B5FUmmYsXZP5b3FfXzH3pbb86hK%5Cn6K4DplUGQ5Sb2exrt90%3D%22%2C%22delete%22%3Afalse%7D%2C%22isCache%22%3Afalse%7D"
    # r = requests.get(url)
    # # print(r.content)
    # with open('./test.pdf', 'wb') as f:
    #     f.write(r.content)
    # print(r.status_code)
    browser = webdriver.Chrome()
    browser.get('http://www.baidu.com/')