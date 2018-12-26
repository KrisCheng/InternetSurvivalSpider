#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 23/12/2018

from util.https import Http
from util.parse import Parse
from config.config import LAGOU_HEADERS, LAGOU_COOKIES
import time
import logging
import codecs

# log file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - Process - %(process)d : %(thread)d %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='lagou_diary.log',
                    filemode='a')


def getInfo(url, para):
    generalHttp = Http()
    htmlCode = generalHttp.post(url, para=para, headers=LAGOU_HEADERS, cookies=LAGOU_COOKIES)
    generalParse = Parse(htmlCode)
    pageCount = generalParse.parsePage()
    info = []
    for i in range(1, pageCount + 1):
        print('Page: %s' % i)
        para['pn'] = str(i)
        htmlCode = generalHttp.post(url, para=para, headers=LAGOU_HEADERS, cookies=LAGOU_COOKIES)
        generalParse = Parse(htmlCode)
        info = info + getInfoDetail(generalParse)
        time.sleep(5)
    return info


def getInfoDetail(generalParse):
    info = generalParse.parseInfo()
    return info

def processInfo(info, para):
    logging.info('Process start')

    try:
        file = codecs.open('%s_%s.xlsx' % (para['city'], para['kd']), 'w', 'utf-8')
        title = ''
        for key in info[0].keys():
            title = title + '\t' + str(key)
        title = title + '\n'
        file.write(title)
        for p in info:
            line = ''
            for value in p.values():
                line = line + '\t' + str(value)
            line = line + '\n'
            file.write(line)
        file.close()
        return True

    except Exception as e:
        print(str(e) + " not exist.")
        return False

def main(url, para):
    logging.error('Main start')
    if url:
        info = getInfo(url, para)  # 获取信息
        flag = processInfo(info, para)  # 信息储存
        return flag
    else:
        return None

def main_task():
    kdList = [u'算法工程师', u'前端工程师', u'后端工程师', u"深度学习", u"产品经理", u"全栈工程师"]
    cityList = [u'上海']
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    for city in cityList:
        print('Crawling: %s' % city)
        for pos in kdList:
            para = {'first': 'true', 'pn': '1', 'kd': pos, 'city': city}
            flag = main(url, para)
            if flag:
                print('%s_%s Crawling Success' % (city, pos))
            else:
                print('%s_%s Crawling Fail' % (city, pos))