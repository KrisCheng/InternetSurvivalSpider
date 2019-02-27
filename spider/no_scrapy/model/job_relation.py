#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/27

from sqlalchemy import Column, String, Integer, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class JobRelation(Base):

    __tablename__ = 'job_relation'

    id = Column(Integer, primary_key=True)
    job_code = Column(String)
    job_name = Column(String)
    city = Column(String)
    salary = Column(String)
    publish_date = Column(Date)
    company_code = Column(String)
    company_name = Column(String)
    company_full_name = Column(String)
    data_source = Column(String)
    extra_params = Column(String)
    create_time = Column(Date)

    def __init__(self, job_code, job_name, city, salary, publish_date, company_code, company_name, company_full_name, data_source):
        self.job_code = job_code
        self.job_name = job_name
        self.city = city
        self.salary = salary
        self.publish_date = publish_date
        self.company_code = company_code
        self.company_name = company_name
        self.company_full_name = company_full_name
        self.data_source = data_source
        self.create_time = datetime.now()