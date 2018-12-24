#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 24/12/2018

# TODO

import requests

def download_file(url):
    local_filename = "test.pdf"
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

def main_task():
    url = "http://www.wanfangdata.com.cn/local/toFullText.do?item_id=1226135&item_num=002&gazetteers_id=FZ001108"
    url = "http://common.wanfangdata.com.cn/download/download.do?type=local+chronicles&resourceId=1226135&firstpublish=null&resourceTitle=%E5%8C%97%E4%BA%AC%E5%B8%82%E5%B4%87%E6%96%87%E5%8C%BA%E9%A5%AE%E9%A3%9F%E4%B8%9A%E8%B5%84%E6%96%99%E6%B1%87%E7%BC%96&transaction=%7B%22id%22%3Anull%2C%22transferOutAccountsStatus%22%3Anull%2C%22transaction%22%3A%7B%22id%22%3A%221077189967635042304%22%2C%22status%22%3A1%2C%22createDateTime%22%3Anull%2C%22payDateTime%22%3A1545657076163%2C%22authToken%22%3A%22TGT-2170957-EarDw4kYMtJHl61FtqYyhHyvPREsIaDe9q7l2jLb9OIfUypsWs-my.wanfangdata.com.cn%22%2C%22user%22%3A%7B%22accountType%22%3A%22Group%22%2C%22key%22%3A%22tjdxtsg%22%7D%2C%22transferIn%22%3A%7B%22accountType%22%3A%22Income%22%2C%22key%22%3A%22LocalChronicleItemFulltext%22%7D%2C%22transferOut%22%3A%7B%22GTimeLimit.tjdxtsg%22%3A0.5%7D%2C%22turnover%22%3A0.5%2C%22orderTurnover%22%3A0.5%2C%22productDetail%22%3A%22local+chronicles_1226135%22%2C%22productTitle%22%3Anull%2C%22userIP%22%3A%22111.187.51.93%22%2C%22organName%22%3Anull%2C%22memo%22%3Anull%2C%22orderUser%22%3A%22tjdxtsg%22%2C%22orderChannel%22%3A%22pc%22%2C%22payTag%22%3Anull%2C%22webTransactionRequest%22%3Anull%2C%22signature%22%3A%22OeHAPl1RrD0TbaIyexTk1PRMmwJOOnvAIcEtyE2R5aVwGHldTaekZcODYf%2FRN4ev%2Bn8viYp6S2jJ%5CnzVf3%2BW7yo1g%2BRcAYXfUdtSWu1Ro65jT6LbxhpSQR0ihl%2B%2BomO1DaHFonURmsMzjiLXsNbT5r%2FmVi%5Cnj%2BsPPkYjuI7MnpUIBIw%3D%22%2C%22delete%22%3Afalse%7D%2C%22isCache%22%3Afalse%7D"
    r = requests.get(url)
    download_file(url)
    print(r.url)