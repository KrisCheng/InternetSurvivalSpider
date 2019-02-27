# Internet Survival Spider

### Introduction

a spider project to collect, analysis Internet related information (jobs, articles, questions), including the spider, data analysis and web visualization with basic search engine.

### Usage

* create virtual environment

```shell
virtualenv spider_venv
```

* start virtual environment

```shell
source spider_venv/bin/activate
```

* install dependencies

```shell
pip install -r requirements.txt
```

* exit virtual environment

```shell
deactivate
```

### Catalog

```
.
├── README.md                                       Please READ ME FIRST!!!
├── requirements.txt                                package dependencies.
├── web-search                                      web visulization(including search engine).
├── analysis                                        data analysis.
└── spider           
    ├── scrapy                                      spider with scrapy.
    └── no scrapy                                   spider without scrapy.
```

### Todo

[] 拉勾公司以及面试信息
[] 数据分析和可视化展示


### Reference

* [LagouSpider](https://github.com/nnngu/LagouSpider)
* [LagouJob](https://github.com/lucasxlu/LagouJob)
* [Python分布式爬虫打造搜索引擎](http://coding.imooc.com/class/92.html)

