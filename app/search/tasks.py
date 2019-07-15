from __future__ import unicode_literals
from celery import shared_task
from celery.decorators import task

from .models import Search,Company

@task(name='search.tasks.update_search_hit_count')
def update_search_hit_count(company_ids,query_week):
    for company_id in company_ids:
        company = Company.objects.get(pk=company_id)
        print(company.name)
        print(company_id)
        # TODO: Optimize with bulk update: https://docs.djangoproject.com/en/2.1/topics/db/queries/#updating-multiple-objects-at-once
        try:
            search_log_row = Search.objects.get(company_id__id=company_id,week=query_week)
        except:
            print("Not exist,creating")
            search_lot_row = Search.objects.create(company_id = company,week=query_week,search_hit=1)
            search_log_row = Search.objects.get(company_id__id=company_id,week=query_week)
        new_search_hit = search_log_row.search_hit + 1
        search_log_row.search_hit = new_search_hit
        search_log_row.save()
