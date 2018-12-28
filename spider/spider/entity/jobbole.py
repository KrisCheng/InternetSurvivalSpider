#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 28/12/2018

from sqlalchemy import Column, String, Integer, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class JobboleArticle(Base):

    __tablename__ = 'jobbole_article'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    tags = Column(String)

    def __init__(self, title, tags):
        self.title = title
        self.tags = tags