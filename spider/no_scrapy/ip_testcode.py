#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/26

# IP测试代码。

import requests
from config.config import *

# 要访问的目标页面
targetUrl = "https://m.lagou.com/search.html"
resp = requests.get(targetUrl, proxies=proxies)

print(resp.status_code)
# print(resp.text)