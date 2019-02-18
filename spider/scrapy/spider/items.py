#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 27/12/2018

import scrapy
import re
import datetime
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.loader import ItemLoader
from models.es_types import ArticleType


# 日期特殊处理 YYYY/MM/DD

def date_convert(value):
    try:
        date_match = re.match("\d{4}/\d{2}/\d{2}", value.strip())
        value = date_match.group()
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date


def return_value(value):
    return value

def remove_comment_tags(value):

    # 去掉tag中提取的评论

    if "评论" in value:
        return ""
    else:
        return value


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums

# 伯乐在线文章
class JobBoleArticleItem(scrapy.Item):

    title = scrapy.Field()
    # MapCompose 用于预处理
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert)
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(",")
    )
    content = scrapy.Field()

    def save_to_es(self):

        article = ArticleType()
        article.title = self['title']
        article.create_date = self['create_date']
        article.content = self['content']
        article.url = self['url']
        article.tags = self['tags']
        article.fav_nums = self['fav_nums']
        article.praise_nums = self['praise_nums']
        article.comment_nums = self['comment_nums']
        article.save()


class ArticleItemLoader(ItemLoader):
    # 自定义itemloader, 仅取第一个
    default_output_processor = TakeFirst()


# 拉勾网职位
class LagouJobItem(scrapy.Item):

    company_fullname = scrapy.Field()
    position_name = scrapy.Field()
    salary = scrapy.Field()
    work_years = scrapy.Field()
    education = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    finance_stage = scrapy.Field()
    industry_field = scrapy.Field()
    first_type = scrapy.Field()
    position_labels = scrapy.Field()

class LagouJobItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

