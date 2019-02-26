#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/16

import datetime
import os
import re
import sys
import time
import pandas as pd
import requests
from config.config import *
from urllib import parse as parse
from random import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

def mkdirs_if_not_exists(directory_):
    """
    create a new folder if it does not exist
    """
    if not os.path.exists(directory_) or not os.path.isdir(directory_):
        os.makedirs(directory_)


def get_max_pageNo(positionName, cityName):
    """
    return the max page number of a specific city_job
    """
    request_url = 'https://m.lagou.com/search.json?city='+parse.quote(cityName)+'&positionName=' + parse.quote(
        positionName) + '&pageNo=1&pageSize=15'

    response = requests.get(request_url, proxies=proxies, headers=MLAGOU_HEADERS, cookies=init_cookies(), timeout=10)

    print("Getting data from %s successfully. URL: " % positionName + request_url)

    if response.status_code == 200:
        max_page_no = int(int(response.json()['content']['data']['page']['totalCount']) / 15 + 1)
        return max_page_no
    elif response.status_code == 403:
        print('request is forbidden by the server...')
        return 0
    else:
        print(response.status_code)
        return 0


def init_cookies():
    """
    return the cookies after your first visit
    """
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'Host': 'm.lagou.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'DNT': '1',
        'Cache-Control': 'max-age=0',
        'Referrer Policy': 'no-referrer-when-downgrade',
    }
    url = 'https://m.lagou.com/search.html'

    response = requests.get(url, headers=headers, timeout=10, proxies=proxies)
    return response.cookies


def crawl_jobs(positionName, cityName):
    """
    crawl the job info from lagou H5 web pages
    """
    JOB_DATA = list()

    max_page_number = get_max_pageNo(positionName, cityName)

    print("%s, %s. There are %s pages, approximately %s records in total."%(positionName, cityName, max_page_number, max_page_number * 15))

    for i in range(1, max_page_number+1):
        request_url = 'https://m.lagou.com/search.json?city='+parse.quote(cityName)+'&positionName='+parse.quote(
            positionName)+'&pageNo=' + str(i)+'&pageSize=15'

        response = requests.get(request_url, cookies=init_cookies(), headers=MLAGOU_HEADERS, proxies=proxies)

        if response.status_code == 200:
            try:
                items = response.json()['content']['data']['page']['result']
                if len(items) > 0:
                    for each_item in items:
                        if "今天" in each_item['createTime']:
                            each_item['createTime'] = re.sub("今天.*", str(datetime.date.today()),
                                                             each_item['createTime'])
                        elif "昨天" in each_item['createTime']:
                            today = datetime.date.today()
                            oneday = datetime.timedelta(days=1)
                            yesterday = today - oneday
                            each_item['createTime'] = re.sub("昨天.*", str(yesterday), each_item['createTime'])

                        JOB_DATA.append([each_item['positionId'], each_item['positionName'], each_item['city'],
                                         each_item['createTime'], each_item['salary'], each_item['companyId'],
                                         each_item['companyName'], each_item['companyFullName']])
                        print('crawling page %d done...' % i)
                        time.sleep(random.randint(SLEEP_TIME, SLEEP_TIME+1))
            except:
                print('Invalid request is found by Lagou...')
                pass
        elif response.status_code == 403:
            print('request is forbidden by the server...')
        else:
            print(response.status_code)

    return JOB_DATA


def main_task():
    craw_job_list = JOB_LIST
    craw_city_list = CITY_LIST
    for job in craw_job_list:
        for city in craw_city_list:
            joblist = crawl_jobs(job, city)
            col = [
                u'职位编码',
                u'职位名称',
                u'所在城市',
                u'发布日期',
                u'薪资待遇',
                u'公司编码',
                u'公司名称',
                u'公司全称']
            df = pd.DataFrame(joblist, columns=col)
            dir = "./data/"
            mkdirs_if_not_exists(dir)
            df.to_excel(os.path.join(dir, city+"_"+job+"_mlagou.xlsx"), sheet_name=city+"_"+job, index=False)