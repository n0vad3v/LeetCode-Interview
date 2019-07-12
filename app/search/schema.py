import graphene
from django.db.models import Q
from graphene import Node
from graphene_django.types import DjangoObjectType

from .models import Company,Search

# For getting statistic year-month-week_of_month
import numpy as np
import datetime
import calendar

class CompanyNode(DjangoObjectType):
    class Meta:
        model = Company

class Query(object):
    company = graphene.List(CompanyNode,
                             pinyin=graphene.String(),
                             query=graphene.String())
    hot_search_companies = graphene.List(CompanyNode,
                            week=graphene.String(),
                            top_count=graphene.Int())
    all_companies = graphene.List(CompanyNode)

    def resolve_company(self,info,**kwargs):
        id = kwargs.get('id')
        query = kwargs.get('query')

        if id is not None:
            return Company.objects.get(pk=id)
        
        if query is not None:
            return Company.objects.filter(Q(name__contains = query) | Q(slug__contains = query) | Q(pinyin__contains = query))

        return None

    def get_week_of_month(year, month, day):
        x = np.array(calendar.monthcalendar(year, month))
        week_of_month = np.where(x==day)[0][0] + 1
        return(week_of_month)

    def resolve_hot_search_companies(self,info,**kwargs):
        week = kwargs.get('week')
        top_count = kwargs.get('top_count')

        now = datetime.datetime.now()
        x = np.array(calendar.monthcalendar(now.year,now.month))
        week_of_month = np.where(x==now.day)[0][0] + 1
        # Padding with zero
        month = f'{now.month:02}'
        week_of_month = f'{week_of_month:02}'
        query_week = str(now.year)+month+str(week_of_month)
        # Now should be 20190702 (the second week on July,2019)
        #print("Querying "+ query_week)
        top_5_companies = Search.objects.order_by('-search_hit').all()[:top_count]
        companies_with_search_hit = []
        for company_search in top_5_companies:
            company = company_search.slug 
            companies_with_search_hit.append(company)
        return companies_with_search_hit
        #return Company.objects.order_by('-searchHitCount').all()[:5]
    
    def resolve_all_companies(self,info,**kwargs):
        return Company.objects.all()
