#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 27/12/2018

import codecs
import json

from scrapy.exporters import JsonItemExporter
from spider.settings import *
from spider.entity.jobbole_article import *
from spider.entity.lagou_job import *

from sqlalchemy import Column, String,Integer,DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item

# class JsonWithEncodingPipeline(object):
#
#     # 自定义json文件的导出
#     def __init__(self):
#         self.file = codecs.open('article.json', 'w', encoding="utf-8")
#
#     def process_item(self, item):
#         lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(lines)
#         return item
#
#     def spider_closed(self, spider):
#         self.file.close()
#
# class JsonExporterPipleline(object):
#
#     # 调用scrapy提供的json export导出json文件
#
#     def __init__(self):
#         self.file = open('articleexport.json', 'wb')
#         self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
#         self.exporter.start_exporting()
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.file.close()
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item

# 同步写入

class JobbolePipleline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):

        engine = create_engine(MYSQL_DATABASE_URI)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        try:
            data_result = JobboleArticle(
                title = item["title"],
                content = item["content"],
                create_date = item["create_date"],
                url = item["url"],
                tags = item["tags"],
                fav_nums = item["fav_nums"],
                praise_nums = item["praise_nums"],
                comment_nums = item["comment_nums"])
            session.add(data_result)
        except:
            print("Jobbole Import ERROR.")
        finally:
            session.commit()
            session.close()
            return item

class LagouPipleline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):

        engine = create_engine(MYSQL_DATABASE_URI)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        try:
            data_result = LagouJob(
                company_fullname = item["company_fullname"],
                position_name = item["position_name"],
                salary = item["salary"],
                work_year = item["work_year"],
                education = item["education"],
                city = item["city"],
                district = item["district"],
                finance_stage = item["finance_stage"],
                industry_field = item["industry_field"],
                first_type = item["first_type"],
                position_lables = item["position_lables"])
            session.add(data_result)
        except:
            print("Lagou Import ERROR.")
        finally:
            session.commit()
            session.close()
            return item