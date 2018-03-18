#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Desc: a basic spider for get urls from Baidubaike, based on Python3.
Author: Kris Peng
Copyright (c) 2018 - Kris Peng <kris.dacpc@gmail.com>
'''
import url_manager, html_downloader, html_parser, html_output

class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                # get url
                new_url = self.urls.get_new_url()
                # save url content and save
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                print("craw %d : %s" % (count, new_url))
                if count == 10:
                    break
                count = count + 1
            except:
                print("craw failed!!!")

        self.output.output_html()

if __name__ == "__main__":
    # entrance, the item of "Python".
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
