#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/26

# IP测试代码。

import requests
from config.config import *

# 要访问的目标页面
request_url = 'https://m.lagou.com/search.json?city=上海&positionName=JAVA工程师&pageNo=1&pageSize=15'
request_url = 'https://m.lagou.com/jobs/1327140.html'

response = requests.get(request_url, headers=M_JOB_LAGOU_HEADERS, timeout=10, proxies=PROXIES)
response = requests.post(request_url, proxies=PROXIES, headers=M_JOB_LAGOU_HEADERS, cookies=response.cookies, timeout=10)

print(response.text)
print(response.status_code)