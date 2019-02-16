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
    content = Column(String)
    url = Column(String)
    create_date = Column(DateTime)
    tags = Column(String)
    fav_nums = Column(String)
    praise_nums = Column(String)
    comment_nums = Column(String)

    def __init__(self, title, content, url, create_date, tags, fav_nums, praise_nums, comment_nums):
        self.title = title
        self.content = content
        self.url = url
        self.create_date = create_date
        self.tags = tags
        self.fav_nums = fav_nums
        self.praise_nums = praise_nums
        self.comment_nums = comment_nums