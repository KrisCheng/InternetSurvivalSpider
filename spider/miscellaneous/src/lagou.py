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

SLEEP_TIME = 3

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
        time.sleep(SLEEP_TIME)
    return info

def getInfoDetail(generalParse):
    info = generalParse.parseInfo()
    return info

def processInfo(info, para):
    logging.info('Process start')

    try:
        file = codecs.open('%s_%s.xlsx' % (para['city'], para['kd']), 'w', 'utf-8')
        title = 'city' + '\t' + 'companyFullName' + '\t' + 'companyShortName' + '\t' + 'companyLabelList' + '\t' + 'companySize' + '\t' + \
                'district' + '\t' + 'education' + '\t' + 'salary' + '\t'  + 'workYear' + '\t' + 'jobNature' + '\t' + 'firstType' + '\t' + 'secondType' + '\t' + 'thirdType' + '\t' + \
                'financeStage' + '\t' + 'hitags' + '\t' + 'industryField' + '\t' + 'industryLables' + '\t' + \
                'positionAdvantage' + '\t' + 'positionLables' + '\t' + 'stationname' + '\t' + 'subwayline' + '\n'
        file.write(title)
        for result in info:
            item = str(result['city']) + '\t' + \
            str(result['companyFullName']) + '\t' + \
            str(result['companyShortName']) + '\t' + \
            str(result['companyLabelList']) + '\t' + \
            str(result['companySize']) + '\t' + \
            str(result['district']) + '\t' + \
            str(result['education']) + '\t' + \
            str(result['salary']) + '\t' + \
            str(result['workYear']) + '\t' + \
            str(result['jobNature']) + '\t' + \
            str(result['firstType']) + '\t' + \
            str(result['secondType']) + '\t' + \
            str(result['thirdType']) + '\t' + \
            str(result['financeStage']) + '\t' + \
            str(result['hitags']) + '\t' + \
            str(result['industryField']) + '\t' + \
            str(result['industryLables']) + '\t' + \
            str(result['positionAdvantage']) + '\t' + \
            str(result['positionLables']) + '\t' + \
            str(result['stationname']) + '\t' + \
            str(result['subwayline']) + '\n'
            file.write(item)
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
    kdList = [u'机器学习算法', u"深度学习", u'前端工程师', u'后端工程师', u"全栈工程师", u"架构师", u"产品经理"]
    # kdList = [u'算法工程师']
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