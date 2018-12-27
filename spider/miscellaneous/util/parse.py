#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 24/12/2018

import re
import demjson


class Parse:

    # 解析网页信息
    def __init__(self, htmlCode):
        self.htmlCode = htmlCode
        self.json = demjson.decode(htmlCode)

    def parseTool(self, content):
        # 清除html标签
        if type(content) != str: return content
        sublist = ['<p.*?>', '</p.*?>', '<b.*?>', '</b.*?>', '<div.*?>', '</div.*?>',
                   '</br>', '<br />', '<ul>', '</ul>', '<li>', '</li>', '<strong>',
                   '</strong>', '<table.*?>', '<tr.*?>', '</tr>', '<td.*?>', '</td>',
                   '\r', '\n', '&.*?;', '&', '#.*?;', '<em>', '</em>']
        try:
            for substring in [re.compile(string, re.S) for string in sublist]:
                content = re.sub(substring, "", content).strip()
        except:
            raise Exception('Error ' + str(substring.pattern))
        return content

    def parsePage(self):
        # 解析并计算页面数量, 返回页面数量
        totalCount = self.json['content']['positionResult']['totalCount']  # 职位总数量
        print ("Total Positions: ", totalCount)
        resultSize = self.json['content']['positionResult']['resultSize']  # 每一页显示的数量
        pageCount = int(totalCount) // int(resultSize) + 1  # 页面数量
        print ("Total Pages: ", pageCount)
        return pageCount

    def parseInfo(self):
        # 解析信息，提取必要的字段
        info = []
        for result in self.json['content']['positionResult']['result']:
            dict = {}
            dict["city"] = result['city']
            dict["companyFullName"] = result['companyFullName']
            dict["companyShortName"] = result['companyShortName']
            dict["companyLabelList"] = result['companyLabelList']
            dict["companySize"] = result['companySize']
            dict["district"] = result['district']
            dict["education"] = result['education']
            dict["salary"] = result['salary']
            dict["workYear"] = result['workYear']
            dict["jobNature"] = result['jobNature']
            dict["firstType"] = result['firstType']
            dict["secondType"] = result['secondType']
            dict["thirdType"] = result['thirdType']
            dict["financeStage"] = result['financeStage']
            dict["hitags"] = result['hitags']
            dict["industryField"] = result['industryField']
            dict["industryLables"] = result['industryLables']
            dict["positionAdvantage"] = result['positionAdvantage']
            dict["positionLables"] = result['positionLables']
            dict["stationname"] = result['stationname']
            dict["subwayline"] = result['subwayline']
            info.append(dict)
        return info