#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 23/12/2018

JOB_LIST = ["机器学习实习生"]
CITY_LIST = ["上海"]

# JOB_LIST_TODO = ["CTO","技术总监", "算法工程师", "数据挖掘", "自然语言处理", "区块链", "后端工程师"]

SLEEP_TIME = 5

MLAGOU_HEADERS = {
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

MYSQL_DATABASE_URI = "mysql+pymysql://root:pengcheng00@localhost:3306/spider?charset=utf8" 

# 阿布云代理ip
proxyHost = "http-pro.abuyun.com"
proxyPort = "9010"

# 代理隧道验证信息
proxyUser = "H8J2L7T1K1E1522P"
proxyPass = "2D0DD039ACBF6D0F"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
  "host" : proxyHost,
  "port" : proxyPort,
  "user" : proxyUser,
  "pass" : proxyPass,
}

proxies = {
    "http"  : proxyMeta,
    "https" : proxyMeta,
}

# proxies = None # 不使用代理
