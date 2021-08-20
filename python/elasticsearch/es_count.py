#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 18:35
# @Author  : hzy
# @File    : es_count.py
# @Software: PyCharm

from datetime import datetime, timedelta
from collections import namedtuple

from elasticsearch_dsl import Search, AttrDict, MultiSearch
from elasticsearch import Elasticsearch

es_index = 'bees_articles_stcn'

DateCount = namedtuple('DateCount', ['date', 'count'])
TeamArticleStatsModel = namedtuple('TeamArticleStatsModel',
                                   ['today_article_count', 'today_publish_count', 'total_article_count',
                                    'folder_article_count', 'recent_article_count', 'recent_publish_count'])


def format_es_hits_total(value):
    """
    兼容es版本
    :param value:
    :return:
    """
    if isinstance(value, AttrDict):
        print(value)
        return value.value
    return value


es_search_client = Search(using=Elasticsearch("http://elasticsearch.kube-system:9200"),
                          extra={'track_total_hits': True})
multi_search_client = MultiSearch(using=Elasticsearch("http://elasticsearch.kube-system:9200"))


def get_article_status_count_by_es(folder_id=None, is_user=False, is_create_user=False):
    base_query: Search = es_search_client.source(['id']).filter("term", is_deleted=False).filter("term", team_id=7)
    multi_search = multi_search_client.index('bees_articles_stcn')
    # multi_search = multi_search_client.index("bees_articles_prod")
    total = base_query._clone()
    editing = base_query.filter('term', check_status=1)
    review = base_query.filter('terms', check_status=[2, 3])
    queue = base_query.filter('term', publish_status=1)
    reject = base_query.filter('term', check_status=0)
    published = base_query.filter('terms', publish_status=[0, 2, 3])
    for x in [total, editing, review, queue, reject, published]:
        multi_search = multi_search.add(x)
    res = multi_search.execute()
    res_1 = base_query.filter("range", create_time={"gte": '2021-07-01 00:00:00', "lte": '2021-08-05 00:00:00'}).sort(
        '-update_time', 'id').execute()
    print(res_1.hits.total)
    total, editing, reviewing, queue, reject, published = (format_es_hits_total(x.hits.total) for x in res)
    return total, editing, reviewing, queue, reject, published


def get_today_zero_datetime():
    dt = datetime.today()
    return datetime(dt.year, dt.month, dt.day)


class TestModel:
    count_query_map = {'total_editing_article',
                       'total_pass_article',
                       'total_checking_article',
                       'total_to_publish_article',
                       'total_rejected_article',
                       'total_published_article'
                       }

    def __init__(self):
        for key in self.count_query_map:
            self.__setattr__(key, None)

    def _as_dict(self):
        return {x: self.__getattribute__(x) for x in self.count_query_map}


def get_team_article_stats_from_es(org_id, team_id):
    today = get_today_zero_datetime()

    base_query: Search = es_search_client.source(['id']).filter("term",
                                                                is_deleted=False).filter(
        "term", team_id=team_id)
    multi_search = multi_search_client.index(es_index)

    # 每日 文章数
    date_count_qs = {}
    for day in range(8):
        date = today - timedelta(days=day)
        date_count_query: Search = base_query.filter("range",
                                                     create_time={"gte": date.strftime("%Y-%m-%d %H:%M:%S"),
                                                                  "lte": (date + timedelta(days=1)).strftime(
                                                                      "%Y-%m-%d %H:%M:%S")})
        date_count_qs[date_count_query.query] = date

        multi_search = multi_search.add(date_count_query)

    # 每日 发布数
    date_published_qs = {}
    for day in range(8):
        date = today - timedelta(days=day)
        date_published_query = base_query.filter("range",
                                                 last_publish_time={"gte": date.strftime("%Y-%m-%d %H:%M:%S"),
                                                                    "lte": (date + timedelta(days=1)).strftime(
                                                                        "%Y-%m-%d %H:%M:%S")})
        date_published_qs[date_published_query.query] = date
        multi_search = multi_search.add(date_published_query)

    # 总数
    total_article_count_query = base_query._clone()
    multi_search = multi_search.add(total_article_count_query)

    # 文件夹group count
    folder_count_qs = {}

    folder_group_count_query = base_query._clone()[0:0]
    folder_group_count_query.aggs.bucket("folder_atc_count", "terms", field='folder_id')
    multi_search = multi_search.add(folder_group_count_query)

    editing = base_query.filter('term', check_status=1)
    review = base_query.filter('terms', check_status=[2, 3])
    review_pass = base_query.filter('term', check_status=4)
    queue = base_query.filter('term', publish_status=1)
    reject = base_query.filter('term', check_status=0)
    published = base_query.filter('terms', publish_status=[0, 2, 3])

    test_model = TestModel()
    query_list = [editing, review_pass, review, queue, reject, published]
    count_query_map = {0: 'total_editing_article',
                       1: 'total_pass_article',
                       2: 'total_checking_article',
                       3: 'total_to_publish_article',
                       4: 'total_rejected_article',
                       5: 'total_published_article'
                       }
    search_query_list = list(x.query for x in query_list)

    for _query in query_list:
        multi_search = multi_search.add(_query)

    ress = multi_search.execute()

    date_count_res = []
    date_published_res = []
    for res in ress:
        query = res._search.query
        if query in date_count_qs:
            date = date_count_qs[query]
            date_count_res.append(DateCount(date=date, count=format_es_hits_total(res.hits.total)))
        elif query in date_published_qs:
            date = date_published_qs[query]
            date_published_res.append(
                DateCount(date=date, count=format_es_hits_total(res.hits.total)))
        elif query is total_article_count_query.query:
            total_article_count = format_es_hits_total(res.hits.total)
        elif query is folder_group_count_query.query:
            buckets = res.aggregations['folder_atc_count'].buckets
            folder_id_counts = {b['key']: b['doc_count'] for b in buckets}
            # folders = Folder.query.filter(Folder.id.in_(folder_id_counts.keys())).all()
            folder_article_count = folder_id_counts
            # [FolderArticleCount(folder_id=folder.id, folder_name=folder.name,
            #                                                    article_count=folder_id_counts[folder.id]) for
            #                                 folder in folders]
        elif query in search_query_list:
            test_model.__setattr__(count_query_map[search_query_list.index(query)], format_es_hits_total(res.hits.total))
        else:
            print(query in search_query_list)
    recent_article_count = sorted(date_count_res, key=lambda k: k.date)
    recent_publish_count = sorted(date_published_res, key=lambda k: k.date)
    today_article_count = recent_article_count[-1].count
    today_publish_count = recent_publish_count[-1].count
    stats_model = TeamArticleStatsModel(today_article_count=today_article_count,
                                        today_publish_count=today_publish_count,
                                        recent_publish_count=recent_publish_count,
                                        recent_article_count=recent_article_count,
                                        total_article_count=total_article_count,
                                        folder_article_count=folder_article_count)

    print(test_model)
    return stats_model


if __name__ == '__main__':
    query = Search(using=Elasticsearch("http://elasticsearch.kube-system:9200"))
    res = query.index('bees_articles_stcn').execute()
    print(isinstance(res.hits.total, AttrDict))
    print(get_article_status_count_by_es())
    print(get_team_article_stats_from_es(2, 7))
