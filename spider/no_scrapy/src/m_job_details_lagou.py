#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/26

import os
import random

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from config.config import *
from util.util import *
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

JOB_DETAIL_DIR = './data/job_detail/'


def init_cookies():
    """
    return the cookies after your first visit
    """
    url = 'https://m.lagou.com/search.html'
    response = requests.get(url, headers=M_JOB_LAGOU_HEADERS, timeout=REQUEST_TIMEOUT, proxies=PROXIES)
    return response.cookies

def crawl_job_detail(positionId, positionName):
    """
    get the detailed job description of the position
    """
    request_url = 'https://m.lagou.com/jobs/' + str(positionId) + '.html'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Host': 'm.lagou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4'
    }

    response = requests.get(request_url, headers=headers, timeout=10, cookies=init_cookies(), proxies=PROXIES)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html5lib')
        items = soup.find('div', class_='items')
        jobnature = items.find('span', class_='item jobnature').span.text.strip()
        workyear = items.find('span', class_='item workyear').span.text.strip()
        education = items.find('span', class_='item education').span.text.strip()
        jd = soup.find_all('div', class_='content')[0].get_text().strip().replace('\n', '').replace('&nbps;', '')  # jd

    elif response.status_code == 403:
        print('request is forbidden by the server...')
    else:
        print(response.status_code)
    return [positionId, positionName, jobnature, workyear, education, jd]


def write_job_details_to_txt(positionId, text, parent_dir_name):
    """
    write the job details text into text file
    """
    details_dir = JOB_DETAIL_DIR + parent_dir_name + os.path.sep
    mkdirs_if_not_exists(details_dir)
    try:
        f = open(details_dir + str(positionId) + '.txt', mode='w', encoding='UTF-8')
    except:
        import io
        f = io.open(details_dir + str(positionId) + '.txt', mode='w', encoding='UTF-8')
    finally:
        f.write(text)
        f.flush()
        f.close()

def main_task():

    engine = create_engine(MYSQL_DATABASE_URI)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    all_job_relation = fetch_all_jobrelation(session=session)
    jobrelation_list = []
    for job_relation in all_job_relation:
        dict = {}
        dict["id"] = job_relation.id
        dict["job_code"] = job_relation.job_code
        dict["job_name"] = job_relation.job_name
        jobrelation_list.append(dict)
    session.close()
    print('Total: %s ' % len(jobrelation_list))
    jd_item_list = []
    invalid_count = 0
    count = 0
    for jobrelation in jobrelation_list:

        if invalid_count < 200:
            positionId = jobrelation["job_code"]
            positionName = jobrelation["job_name"]
            count = count + 1
            print('%s / %s' % (count, len(jobrelation_list)))
            try:
                jd_item = crawl_job_detail(positionId, positionName)
                jd_item_list.append(jd_item)
                print('%s has been written successfully...' % positionId)
            except:
                invalid_count = invalid_count + 1
                time.sleep(random.randint(30, 60))
                print('%s failed.' % positionId)
    col = [
        u'职位编码',
        u'职位类型',
        u'工作性质',
        u'工作经验',
        u'教育程度',
        u'详情描述']
    df = pd.DataFrame(jd_item_list, columns=col)
    mkdirs_if_not_exists(JOB_DETAIL_DIR)
    df.to_excel(os.path.join(JOB_DETAIL_DIR, datetime.now().strftime("%Y-%m-%d")+"_job_details.xlsx"), sheet_name="job_details", index=False,
                encoding='UTF-8')