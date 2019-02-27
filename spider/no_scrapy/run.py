#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 23/12/2018

from src import m_job_lagou, company_lagou, m_job_details_lagou
from db import job_relation_db
from analysis import job_count

if __name__ == '__main__':

    # m_job_lagou.main_task() # 移动端拉勾职位基本信息

    # m_job_details_lagou.main_task()  # 移动端拉勾职位详情信息

    # company_lagou.main_task()

    # job_relation_db.main_task()

    job_count.main_task()