from __future__ import unicode_literals
from celery import shared_task
from celery.decorators import task

from .models import Search,Company

@task(name='search.tasks.update_search_hit_count_by_id')
def update_search_hit_count_by_id(company_id,query_week):
    company = Company.objects.get(pk=company_id)
    print(company.name)
    search_log_row = Search.objects.get(slug__id=company_id,week=query_week)
    print(search_log_row.search_hit)
    new_search_hit = search_log_row.search_hit + 1
    search_log_row.search_hit = new_search_hit
    search_log_row.save()
