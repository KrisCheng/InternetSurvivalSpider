#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/16

import random
import time
import os
import requests
from bs4 import BeautifulSoup
from src import m_job_lagou
from config.config import *
from util.util import *
import pandas as pd


def crawl_company(havemark=0):
    """
    crawl company's info 
    :param havemark: 0 for not showing interviewees' remark; 1 for showing interviewees' remark; the default value is 0 
    :return: 
    """
    COMPANY_LIST = list()

    req_url = 'https://www.lagou.com/gongsi/0-0-0.json?havemark=%d' % havemark

    for pn in range(20):
        params = {
            'first': 'false',
            'pn': str(pn),
            'sortField': '0',
            'havemark': str(havemark)
        }

        response = requests.post(req_url, headers=M_COMPANY_LAGOU_HEADERS, params=params, cookies=m_job_lagou.init_cookies(),
                                 timeout=REQUEST_TIMEOUT, proxies=PROXIES)
        print(response.url)
        if response.status_code == 200:
            company_list_per_page = response.json()['result']
            for company in company_list_per_page:
                COMPANY_LIST.append([company['companyId'], company['companyShortName'],
                                     company['city'], company['companyFeatures'],
                                     company['companyFullName'], company['financeStage'], company['industryField'],
                                     company['interviewRemarkNum'], company['positionNum'], company['processRate']])
            print('page %d has been crawled down~' % (pn + 1))
        elif response.status_code == 403:
            print('403 forbidden...')
        else:
            print(response.status_code)
        time.sleep(random.randint(5, 7))

    return COMPANY_LIST


def crawl_company_stage(company_id):

    req_url = 'https://m.lagou.com/gongsi/%s.html' % str(company_id)

    response = requests.get(req_url, headers=M_COMPANY_LAGOU_HEADERS, cookies=m_lagou.init_cookies(), proxies=PROXIES, timeout=REQUEST_TIMEOUT)

    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html5lib')
        company_desc = soup.find_all(class_="desc")[0].get_text().strip()
        industryField = company_desc.split('/')[0].strip()
        financeStage = company_desc.split('/')[1].strip()
        staffNum = company_desc.split('/')[2].strip()

    elif response.status_code == 403:
        print('403 forbidden...')
    else:
        print(response.status_code)
    time.sleep(random.randint(2, 5))

    return [company_id, industryField, financeStage, staffNum]


def main_task():

    company_level_list = list()
    visited_company_id_list = list()
    count = 0
    for job in os.listdir('./data'):
        for company_id in pd.read_excel(os.path.join('./data', job))['公司编码']:
            if not company_id in visited_company_id_list and count < 3:
                try:
                    count = count + 1
                    print(count)
                    company = crawl_company_stage(company_id)
                    company_level_list.append(company)
                    visited_company_id_list.append(company_id)
                except:
                    pass
                finally:
                    cols = [u'公司编码', u'所属行业', u'融资阶段', u'员工数量']
                    df = pd.DataFrame(company_level_list, columns=cols)
                    df.to_excel('./company.xlsx', 'Company', index=False)
            else:
                print('%d has been visited before...' % company_id)
    print('Processing done!')
