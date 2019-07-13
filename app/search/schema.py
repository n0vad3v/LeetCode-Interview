import graphene
from django.db.models import Q
from graphene import Node
from graphene_django.types import DjangoObjectType

from .models import Company,Search
from .tasks import *
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

# For getting statistic year-month-week_of_month
import numpy as np
import datetime
import calendar

def get_current_week_of_month():
    now = datetime.datetime.now()
    x = np.array(calendar.monthcalendar(now.year,now.month))
    week_of_month = np.where(x==now.day)[0][0] + 1
    # Padding with zero
    month = f'{now.month:02}'
    week_of_month = f'{week_of_month:02}'
    query_week = str(now.year)+month+str(week_of_month)
    return query_week

class CompanyNode(DjangoObjectType):
    class Meta:
        model = Company

class Query(object):
    company = graphene.List(CompanyNode,
                             query=graphene.String(required=True))
    hot_search_companies = graphene.List(CompanyNode,
                            week=graphene.String(required=True),
                            top_count=graphene.Int())
    all_companies = graphene.List(CompanyNode)

    def resolve_company(self,info,**kwargs):
        query = kwargs.get('query')

        cache_name = "resolve_company_"+query

        if query is not None:
            if cache_name in cache:
                companies = cache.get_many([cache_name])
                companies = companies[cache_name]
                print("from cache")
            else:
                companies = Company.objects.filter(Q(name__contains = query) | Q(slug__contains = query) | Q(pinyin__contains = query))
                print("not from cache")
                cache.set(cache_name,companies)

            # Search Hit increment
            company_ids = []
            for company in companies:
                company_ids.append(company.id)
            update_search_hit_count.delay(company_ids,get_current_week_of_month())

            return companies

        return None

    def resolve_hot_search_companies(self,info,**kwargs):
        week = kwargs.get('week')
        top_count = kwargs.get('top_count')

        cache_name = "hot_search_"+week+"_"+"top_count"

        if week is not None:
            if cache_name in cache:
                print("from cache")
                top_companies = cache.get_many([cache_name])
                top_companies = top_companies[cache_name]
            else:
                print("not from cache")
                top_companies = Search.objects.order_by('-search_hit').filter(week=week)[:top_count]
                cache.set(cache_name,top_companies)
        else:
            top_companies = Search.objects.order_by('-search_hit').all()[:top_count]

        companies_with_search_hit = []
        for company_search in top_companies:
            company = company_search.company_id
            companies_with_search_hit.append(company)
        return companies_with_search_hit
    
    def resolve_all_companies(self,info,**kwargs):
        return Company.objects.all()
