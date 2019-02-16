#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/16

from sqlalchemy import Column, String, Integer, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class LagouJob(Base):

    __tablename__ = 'lagou_job'

    id = Column(Integer, primary_key=True)
    company_fullname = Column(String)
    position_name = Column(String)
    salary = Column(String)
    work_years = Column(DateTime)
    education = Column(String)
    city = Column(String)
    district = Column(String)
    finance_stage = Column(String)
    industry_field = Column(String)
    first_type = Column(String)
    position_labels = Column(String)
    create_time = Column(Date)

    def __init__(self, company_fullname, position_name, salary, work_years, education, city, district, finance_stage,
                 industry_field, first_type, position_labels):
        self.company_fullname = company_fullname
        self.position_name = position_name
        self.salary = salary
        self.work_years = work_years
        self.education = education
        self.city = city
        self.district = district
        self.finance_stage = finance_stage
        self.industry_field = industry_field
        self.first_type = first_type
        self.position_labels = position_labels
        self.create_time = datetime.now()