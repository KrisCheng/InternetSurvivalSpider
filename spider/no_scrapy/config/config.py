#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 23/12/2018

# JOB_LIST = ["产品实习生", "算法实习生", "前端实习生", "后端实习生", "数据挖掘实习生", "机器学习实习生", "量化", "中间件"]

JOB_LIST = ["研发"]
CITY_LIST = ["上海"]

MIN_SLEEP_TIME = 40
MAX_SLEEP_TIME = 50
REQUEST_TIMEOUT = 20

M_JOB_LAGOU_HEADERS = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Host': 'm.lagou.com',
    'DNT': '1',
    'Referer': 'https://m.lagou.com/search.html',
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 '
                  'Mobile/13B143 Safari/601.1',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referrer Policy': 'no-referrer-when-downgrade',
}

M_COMPANY_LAGOU_HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'm.lagou.com',
    'Referer': 'https://www.lagou.com/gongsi/0-0-0?havemark=0',
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 '
                  'Mobile/13B143 Safari/601.1',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referrer Policy': 'no-referrer-when-downgrade',
}

MYSQL_DATABASE_URI = "mysql+pymysql://root:pengcheng00@localhost:3306/web_spider?charset=utf8"

DATA_BASE_PATH = "./data"

# 阿布云代理ip
proxyHost = "http-pro.abuyun.com"
proxyPort = "9010"

# 代理隧道验证信息
proxyUser = "H2A639621I80T86P"
proxyPass = "E9EB6E34BAD7C44A"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
  "host" : proxyHost,
  "port" : proxyPort,
  "user" : proxyUser,
  "pass" : proxyPass,
}

PROXIES = {
    "http"  : proxyMeta,
    "https" : proxyMeta,
}

# PROXIES = None
