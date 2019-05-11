#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/3/7

from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Company(Base):

    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    company_code = Column(String)
    industry = Column(String)
    finance_stage = Column(String)
    headcount = Column(Integer)
    data_source = Column(String)
    extra_params = Column(String)
    create_time = Column(Date)

    def __init__(self, company_code, industry, finance_stage, headcount, data_source):
        self.company_code = company_code
        self.industry = industry
        self.finance_stage = finance_stage
        self.headcount = headcount
        self.data_source = data_source
        self.create_time = datetime.now()