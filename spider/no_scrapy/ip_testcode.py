#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/26

# IP测试代码。

import requests
from config.config import *

# 要访问的目标页面
request_url = 'https://m.lagou.com/search.json?city=上海&positionName=JAVA工程师&pageNo=1&pageSize=15'

# request_url = 'https://m.lagou.com/search.json?city=%E4%B8%8A%E6%B5%B7&positionName=%E4%BA%A7%E5%93%81%E5%AE%9E%E4%B9%A0%E7%94%9F&pageNo=1&pageSize=15'
# request_url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"

response = requests.get(request_url, headers=M_JOB_LAGOU_HEADERS, timeout=10, proxies=PROXIES)
response = requests.post(request_url, proxies=PROXIES, headers=M_JOB_LAGOU_HEADERS, cookies=response.cookies, timeout=10)

print(response.text)
print(response.status_code)