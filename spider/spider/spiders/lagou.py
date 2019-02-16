#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/15

import scrapy
import json
from spider.items import LagouJobItem
from bs4 import BeautifulSoup

class LagouSpider(scrapy.Spider):

    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com']

    curpage = 1
    totalPageCount = 6
    keyword = "DBA"
    cururl = "https://www.lagou.com/zhaopin/%s/%s/?filterOption=3" % (keyword, curpage)

    def start_requests(self):
        return [scrapy.http.FormRequest(self.cururl, callback=self.parse)]

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser', from_encoding='utf-8')
        body_ul = soup.find_all("li", class_="con_list_item default_list")
        for li in body_ul:
            item = LagouJobItem()
            arg1 = li.find("div", class_="position").find("div", class_="p_top").find("em").get_text(strip=True)
            arg2 = li.find("div", class_="position").find("div", class_="li_b_l").get_text(" / ", strip=True)
            arg3 = li.find("div", class_="company").find("div", class_="industry").get_text(strip=True)
            arg4 = li.find("div", class_="list_item_bot").find("div", class_="li_b_r").get_text(strip=True)
            item['company_fullname'] = li.find("div", class_="company").find("div", class_="company_name").find(
                "a").get_text(strip=True)
            item['position_name'] = li.find("div", class_="position").find("div", class_="p_top").find(
                "h3").get_text(strip=True)
            item['salary'] = ((arg2 + "/").split('/')[0]).strip()
            item['work_year'] = ((arg2 + "/").split('/')[1]).strip()
            item['education'] = ((arg2 + "/").split('/')[2]).strip()
            item['city'] = (arg1 + '·' + arg1).split('·')[0]
            item['district'] = (arg1 + '·' + arg1).split('·')[1]
            item['industry_field'] = ((arg3 + "/").split('/')[0]).strip()
            item['finance_stage'] = ((arg3 + "/").split('/')[1]).strip()
            item['position_lables'] = arg4.strip('“').strip('”')
            item['first_type'] = li.find("div", class_="list_item_bot").find("div", class_="li_b_l").get_text(",",strip=True)
            yield item

        if self.curpage < self.totalPageCount:
            self.curpage += 1
            self.cururl = "https://www.lagou.com/zhaopin/%s/%s/?filterOption=3" % (self.keyword, self.curpage)
