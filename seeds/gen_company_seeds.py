import json
import random
import string

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

company_with_search_hit_list = []
for i in range(1,250001):
    row = {}
    row['model'] = "search.company"
    row['pk'] = i
    # gen for fields
    random_str = random_string(15)
    fields = {}
    fields['slug'] = random_str
    fields['name'] = random_str
    fields['pinyin'] = random_str
    fields['isPremiumOnly'] = False
    row['fields'] = fields

    hit = {}
    hit['model'] = "search.search"
    hit['pk'] = i

    fields = {}
    fields['company_id'] = i
    fields['week'] = "20190702"
    fields['search_hit'] = random.randrange(2000)

    hit['fields'] = fields
    
    company_with_search_hit_list.append(row)
    company_with_search_hit_list.append(hit)

with open('fake_companies.json','w') as f:
    json.dump(company_with_search_hit_list,f)
