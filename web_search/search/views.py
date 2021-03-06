import json
from django.shortcuts import render
from django.views.generic.base import View
from search.models import ArticleType
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from datetime import datetime

client = Elasticsearch(hosts=["127.0.0.1"])

class SearchSuggest(View):
    def get(self, request):
        key_words = request.GET.get('s', '')
        re_datas = []
        if key_words:
            s = ArticleType.search()
            s = s.suggest('my_suggest', key_words, completion={
                "field": "suggest", "fuzzy":{
                    "fuzziness": 2
                },
                "size": 10
            })
            suggestions = s.execute_suggest()
            for match in suggestions.my_suggest[0].options:
                source = match._source
                re_datas.append(source["title"])
        return HttpResponse(json.dumps(re_datas), content_type="application/json")

class SearchView(View):

    def get(self, request):
        key_words = request.GET.get('q','')
        page = request.GET.get("p", "1")
        try:
            page = int(page)
        except:
            page = 1

        start_time = datetime.now()
        response = client.search(
            index = "jobbole",
            body = {
                "query":{
                    "multi_match":{
                        "query": key_words,
                        "fields": ["tags", "title", "content"]
                    }
                },
                "from": (page-1)*10,
                "size": 10,
                "highlight": {
                    "pre_tags": ['<span class="keyWord">'],
                    "post_tags": ['</span>'],
                    "fields": {
                        "title": {},
                        "content": {},
                    }
                }
            }
        )

        end_time = datetime.now()
        last_second = (end_time - start_time).total_seconds()
        total_nums = response["hits"]["total"]
        hit_list = []

        for hit in response["hits"]["hits"]:
            hit_dict = {}
            if "title" in hit["highlight"]:
                hit_dict["title"] = "".join(hit["highlight"]["title"])
            else:
                hit_dict["title"] = hit["_source"]["title"]

            # TODO 内容快照显示
            # if "content" in hit["highlight"]:
            #     hit_dict["content"] = "".join(hit["highlight"]["content"])[:600]
            # else:
            # hit_dict["content"] = hit["_source"]["content"][:300]
            # reg = re.compile('<[^>]*>')
            # hit_dict["content"] = reg.sub('', hit_dict["content"]).replace('\n', '').replace(' ', '')
            hit_dict["content"] = ""
            hit_dict["create_date"] = hit["_source"]["create_date"]
            hit_dict["url"] = hit["_source"]["url"]
            hit_dict["score"] = hit["_score"]
            hit_list.append(hit_dict)

            if(total_nums%10) > 0:
                page_nums = int(total_nums/10) + 1
            else:
                page_nums = total_nums / 10

        return render(request, "result.html", {"page":  page,
                                               "all_hits": hit_list,
                                               "key_words": key_words,
                                               "total_nums": total_nums,
                                               "page_nums": page_nums,
                                               "last_second": last_second})