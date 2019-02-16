#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 27/12/2018

from scrapy.cmdline import execute

if __name__ == "__main__":

    # execute(["scrapy", "crawl", "jobbole"])
    # execute(["scrapy", "crawl", "zhihu"])
    execute(["scrapy", "crawl", "lagou_v2"])