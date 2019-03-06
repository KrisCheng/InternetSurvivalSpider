#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 23/12/2018

from src import m_job_lagou, company_lagou, m_job_details_lagou
from db import job_relation_db, job_requirement_db
from analysis import job_count

if __name__ == '__main__':

    # 数据爬取
    # m_job_lagou.main_task() # h5拉勾职位基本信息
    # m_job_details_lagou.main_task()  # h5拉勾职位详情信息
    # company_lagou.main_task()


    # 数据入库
    # job_relation_db.main_task()
    job_requirement_db.main_task()


    # 数据分析
    # job_count.main_task()