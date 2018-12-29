#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 27/12/2018

import codecs
import json

from scrapy.exporters import JsonItemExporter
from spider.settings import *
from spider.entity.jobbole import *

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

class MySQLExporterPipleline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):

        engine = create_engine(MYSQL_DATABASE_URI)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        try:
            print("CTEESAADA: ", item["create_date"] )
            data_result = JobboleArticle(
                title = item["title"],
                content=item["content"],
                create_date=item["create_date"],
                url=item["url"],
                tags=item["tags"],
                fav_nums=item["fav_nums"],
                praise_nums=item["praise_nums"],
                comment_nums=item["comment_nums"])
            session.add(data_result)
        except:
            print("ERROR.")
        finally:
            session.commit()
            session.close()
            return item
