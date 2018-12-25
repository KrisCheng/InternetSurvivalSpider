#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 23/12/2018

from util.https import Http
from util.parse import Parse
from config.config import LAGOU_HEADERS
from config.config import LAGOU_COOKIES
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
    """
    获取信息
    """
    generalHttp = Http()
    htmlCode = generalHttp.post(url, para=para, headers=LAGOU_HEADERS, cookies=LAGOU_COOKIES)
    generalParse = Parse(htmlCode)
    pageCount = generalParse.parsePage()
    info = []
    # for i in range(1, pageCount + 1):
    for i in range(1, 2):
        print('第%s页' % i)
        para['pn'] = str(i)
        htmlCode = generalHttp.post(url, para=para, headers=LAGOU_HEADERS, cookies=LAGOU_COOKIES)
        generalParse = Parse(htmlCode)
        info = info + getInfoDetail(generalParse)
        time.sleep(2)
    return info


def getInfoDetail(generalParse):
    """
    信息解析
    """
    info = generalParse.parseInfo()
    return info


def processInfo(info, para):
    """
    信息存储
    """
    logging.info('Process start')

    try:
        file = codecs.open('%s_职位.xls' % para['city'], 'w', 'utf-8')

        title = '公司城市 \t 公司名称 \t 公司类型 \t 融资阶段 \t 标签 \t 公司规模 \t 公司所在地 \t 职位类型 \t 学历要求 \t 福利 \t 薪资 \t 工作经验 \n'
        file.write(title)
        for p in info:
            line = str(p['city']) + '\t' + str(p['companyFullName']) + '\t' + str(p['industryField']) + '\t' + str(p['financeStage']) + '\t' + \
                   str(p['companyLabelList']) + '\t' + str(p['companySize']) + '\t' + str(p['district']) + '\t' + \
                   str(p['firstType']) + '\t' + str(p['education']) + '\t' + str(p['positionAdvantage']) + '\t' + \
                   str(p['salary']) + '\t' + str(p['workYear']) + '\n'
            file.write(line)
        file.close()
        return True

    except Exception as e:
        print(str(e) + " not exist.")
        return False

def main(url, para):
    """
    主函数逻辑
    """
    logging.error('Main start')
    if url:
        info = getInfo(url, para)  # 获取信息
        flag = processInfo(info, para)  # 信息储存
        return flag
    else:
        return None

def main_task():
    kdList = [u'算法工程师']
    cityList = [u'上海']
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    for city in cityList:
        print('爬取 %s' % city)
        para = {'first': 'true', 'pn': '1', 'kd': kdList[0], 'city': city}
        flag = main(url, para)
        if flag:
            print('%s 爬取成功' % city)
        else:
            print('%s 爬取失败' % city)


    
    
