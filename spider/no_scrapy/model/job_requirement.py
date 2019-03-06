#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/3/06

from sqlalchemy import Column, String, Integer, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class JobRequirement(Base):

    __tablename__ = 'job_requirement'

    id = Column(Integer, primary_key=True)
    job_code = Column(String)
    title = Column(String)
    experience = Column(String)
    property = Column(String)
    education = Column(String)
    description = Column(String)
    data_source = Column(String)
    extra_params = Column(String)
    create_time = Column(Date)

    def __init__(self, job_code, title, experience, education, description, property, data_source):
        self.job_code = job_code
        self.title = title
        self.experience = experience
        self.education = education
        self.description = description
        self.property = property
        self.data_source = data_source
        self.create_time = datetime.now()