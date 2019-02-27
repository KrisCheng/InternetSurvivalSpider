#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/26

import requests
import math
import pandas as pd
import time
from config.config import *
from util.util import *

def init_cookies():
    """
    return the cookies after your first visit
    """
    my_headers = {
        'Host': 'www.lagou.com',
        'Connection': 'keep-alive',
        'Content-Length': '23',
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Anit-Forge-Token': 'None',
        'Referer': 'https://www.lagou.com/jobs/list_java?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
    }
    url = 'https://www.lagou.com'
    response = requests.get(url, headers=my_headers, timeout=REQUEST_TIMEOUT, proxies=PROXIES)
    return response.cookies


def get_json(url,num):
   '''''从网页获取JSON,使用POST请求,加上头部信息'''
   my_headers = {
       'Host': 'www.lagou.com',
       'Connection': 'keep-alive',
       'Content-Length': '23',
       'Origin': 'https://www.lagou.com',
       'X-Anit-Forge-Code': '0',
       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
       'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
       'Accept': 'application/json, text/javascript, */*; q=0.01',
       'X-Requested-With': 'XMLHttpRequest',
       'X-Anit-Forge-Token': 'None',
       'Referer': 'https://www.lagou.com/jobs/list_java?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
           }

   my_data = {
           'first': 'true',
           'pn':num,
           'kd':'数据分析'}

   res = requests.post(url, headers = my_headers, cookies=init_cookies(), data = my_data, proxies=PROXIES)
   res.raise_for_status()
   res.encoding = 'utf-8'
   # 得到包含职位信息的字典
   page = res.json()
   return page


def get_page_num(count):
   '''''计算要抓取的页数'''
   # 每页15个职位,向上取整
   res = math.ceil(count/15)
   # 拉勾网最多显示30页结果
   if res > 30:
       return 30
   else:
       return res

def get_page_info(jobs_list):
   '''''对一个网页的职位信息进行解析,返回列表'''
   page_info_list = []
   for i in jobs_list:
       job_info = []
       job_info.append(i['companyFullName'])
       job_info.append(i['companyShortName'])
       job_info.append(i['companySize'])
       job_info.append(i['financeStage'])
       job_info.append(i['district'])
       job_info.append(i['positionName'])
       job_info.append(i['workYear'])
       job_info.append(i['education'])
       job_info.append(i['salary'])
       job_info.append(i['positionAdvantage'])
       page_info_list.append(job_info)
   return page_info_list

def main_task():
   url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
    # 先设定页数为1,获取总的职位数
   page_1 = get_json(url,1)
   total_count = page_1['content']['positionResult']['totalCount']
   num = get_page_num(total_count)
   total_info = []
   time.sleep(20)
   print('职位总数:{},页数:{}'.format(total_count,num))

   for n in range(1,num+1):
       # 对每个网页读取JSON, 获取每页数据
       page = get_json(url,n)
       jobs_list = page['content']['positionResult']['result']
       page_info = get_page_info(jobs_list)
       total_info += page_info
       print('已经抓取第{}页, 职位总数:{}'.format(n, len(total_info)))
       # 每次抓取完成后,暂停一会,防止被服务器拉黑
       time.sleep(30)
   #将总数据转化为data frame再输出
   df = pd.DataFrame(data = total_info,columns = ['公司全名','公司简称','公司规模','融资阶段','区域','职位名称','工作经验','学历要求','工资','职位福利'])
   df.to_csv('lagou_jobs.csv',index = False)
   print('已保存为csv文件.')