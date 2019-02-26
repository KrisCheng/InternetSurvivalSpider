#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/26

# IP测试代码。

import requests
from config.config import *

# 要访问的目标页面
request_url = "https://m.lagou.com/search.html"
request_url = 'https://m.lagou.com/search.json?city=%E4%B8%8A%E6%B5%B7&positionName=%E4%BA%A7%E5%93%81%E5%AE%9E%E4%B9%A0%E7%94%9F&pageNo=1&pageSize=15'
request_url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}

my_data = {
    'first': 'true',
    'pn': 1,
    'kd': '数据分析'}

response = requests.post(request_url, headers=my_headers,  proxies=PROXIES)
response = requests.get(request_url, headers=M_JOB_LAGOU_HEADERS, timeout=10, proxies=PROXIES)
# response = requests.post(request_url, data=my_data, proxies=PROXIES, headers=M_JOB_LAGOU_HEADERS, cookies=response.cookies, timeout=10)

print(response.text)
print(response.status_code)