#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/26

# IP测试代码。

import requests
from config.config import *

# 要访问的目标页面
request_url = "https://m.lagou.com/search.html"
response = requests.get(request_url, headers=MLAGOU_HEADERS, timeout=10, proxies=proxies)
response = requests.get(request_url, proxies=proxies, headers=MLAGOU_HEADERS, cookies=response.cookies, timeout=10)
print(response.status_code)

# print(resp.text)