#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 24/12/2018

from config.config import IP, UA
import requests, random

# http请求相关的操作

class Http:
    def __init__(self):
        pass

    def get(self, url, headers=None, cookies=None, proxy=None, timeOut=5, timeOutRetry=5):
        '''
        获取网页源码
        url: 网页链接
        headers: headers
        cookies: cookies
        proxy: 代理
        timeOut: 请求超时时间
        timeOutRetry: 超时重试次数
        return: 源码
        '''
        if not url:
            return 'None'
        try:
            if not headers: headers = {'User-Agent': UA[random.randint(0, len(UA) - 1)]}

            response = requests.get(url, headers=headers, cookies=cookies, proxies=proxy, timeout=timeOut)
            if response.status_code == 200 or response.status_code == 302:
                htmlCode = response.text
            else:
                htmlCode = 'None'
        except Exception as e:
            if timeOutRetry > 0:
                htmlCode = self.get(url=url, timeOutRetry=(timeOutRetry - 1))
            else:
                htmlCode = 'None'
        return htmlCode

    def post(self, url, para, headers=None, cookies=None, proxy=None, timeOut=5, timeOutRetry=5):
        '''
        post获取响应
        url: 目标链接
        para: 参数
        headers: headers
        cookies: cookies
        proxy: 代理
        timeOut: 请求超时时间
        timeOutRetry: 超时重试次数
        return: 响应
        '''

        if not url or not para:
            return None

        try:
            if not headers:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3'}
            response = requests.post(url, data=para, headers=headers, cookies=cookies, proxies=proxy, timeout=timeOut)

            if response.status_code == 200 or response.status_code == 302:
                htmlCode = response.text

            else:
                htmlCode = None

        except Exception as e:
            if timeOutRetry > 0:
                htmlCode = self.post(url=url, para=para, timeOutRetry=(timeOutRetry - 1))
            else:
                htmlCode = None
        return htmlCode