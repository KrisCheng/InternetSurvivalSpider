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
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def init_cookies():
    """
    return the cookies after your first visit
    """
    url = 'https://m.lagou.com/search.html'
    response = requests.get(url, headers=M_JOB_LAGOU_HEADERS, timeout=REQUEST_TIMEOUT, proxies=PROXIES)
    return response.cookies

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

        response = requests.post(req_url, headers=M_JOB_LAGOU_HEADERS, params=params, cookies=init_cookies(),
                                 timeout=REQUEST_TIMEOUT, proxies=PROXIES)
        print(response.url)
        if response.status_code == 200:
            company_list_per_page = response.json()['result']
            for company in company_list_per_page:
                COMPANY_LIST.append([company['companyId'], company['companyShortName'],
                                     company['city'], company['companyFeatures'],
                                     company['companyFullName'], company['financeStage'], company['industryField'],
                                     company['interviewRemarkNum'], company['positionNum'], company['processRate']])
            print('page %d has been crawled down.' % (pn + 1))
        elif response.status_code == 403:
            print('403 forbidden...')
        else:
            print(response.status_code)
        # time.sleep(random.randint(5, 7))

    return COMPANY_LIST


def crawl_company_stage(company_id):

    req_url = 'https://m.lagou.com/gongsi/%s.html' % str(company_id)
    response = requests.get(req_url, headers=M_JOB_LAGOU_HEADERS, cookies=init_cookies(), proxies=PROXIES, timeout=REQUEST_TIMEOUT)
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
    # time.sleep(random.randint(2, 5))

    return [company_id, industryField, financeStage, staffNum]


def main_task():

    engine = create_engine(MYSQL_DATABASE_URI)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    all_job_relation = fetch_all_jobrelation(session=session)

    jobrelation_list = []
    for job_relation in all_job_relation:
        dict = {}
        dict["id"] = job_relation.id
        dict["company_code"] = job_relation.company_code
        jobrelation_list.append(dict)

    company_level_list = list()
    visited_company_id_list = list()

    count = 0
    for jobrelation in jobrelation_list:
        count = count + 1
        if not jobrelation["company_code"] in visited_company_id_list:
            try:
                company = crawl_company_stage(jobrelation["company_code"])
                company_level_list.append(company)
                visited_company_id_list.append(jobrelation["company_code"])
                print('%d / %d . %s has been written successfully...' % (count, len(jobrelation_list), jobrelation["company_code"]))
            except:
                print('%d / %d . %s failed.' % (count, len(jobrelation_list), jobrelation["company_code"]))
        else:
            print('%d / %d . %s has been visited before...' % (count, len(jobrelation_list), jobrelation["company_code"]))

    cols = [u'公司编码', u'所属行业', u'融资阶段', u'员工数量']
    df = pd.DataFrame(company_level_list, columns=cols)
    df.to_excel('./data/company.xlsx', 'Company', index=False)

    print('Processing done!')
