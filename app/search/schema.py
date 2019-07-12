import graphene
from django.db.models import Q
from graphene import Node

from graphene_django.types import DjangoObjectType

from .models import Company

class CompanyNode(DjangoObjectType):
    class Meta:
        model = Company

class Query(object):
    company = graphene.List(CompanyNode,
                             name=graphene.String(),
                             pinyin=graphene.String(),
                             query=graphene.String(),
                             slug=graphene.String())
    hot_search_companies = graphene.List(CompanyNode)
    all_companies = graphene.List(CompanyNode)

    def resolve_company(self,info,**kwargs):
        name = kwargs.get('name')
        id = kwargs.get('id')
        slug = kwargs.get('slug')
        pinyin = kwargs.get('pinyin')
        query = kwargs.get('query')


        if id is not None:
            return Company.objects.get(pk=id)
        
        if query is not None:
            return Company.objects.filter(Q(name__contains = query) | Q(slug__contains = query) | Q(pinyin__contains = query))

        if name is not None:
            return Company.objects.filter(name__contains = name)

        if slug is not None:
            return Company.objects.filter(slug__contains = slug)

        if pinyin is not None:
            return Company.objects.filter(pinyin__contains = pinyin)

        return None

    def resolve_hot_search_companies(self,info,**kwargs):
        return Company.objects.order_by('-searchHitCount').all()[:5]
    
    def resolve_all_companies(self,info,**kwargs):
        return Company.objects.all()
