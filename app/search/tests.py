from django.test import TestCase
from django.test import Client
from .models import Company,Search
import json

import search.schema
# Create your tests here.
class GraphQLTestCase(TestCase):

    def setUp(self):
        self._client = Client()
        company_leetcode = Company.objects.create(name="LeetCode（力扣）",slug="leetcode",pinyin="likou",isPremiumOnly=True)
        company_google = Company.objects.create(name="咕果",slug="google",pinyin="guguo",isPremiumOnly=True)

        Search.objects.create(company_id=company_leetcode,week="20190702",search_hit=233)
        Search.objects.create(company_id=company_google,week="20190702",search_hit=114514)

    def query(self, query: str, op_name: str = None, variables: dict = None):
        body = {'query': query}
        if op_name:
            body['operation_name'] = op_name
        if input:
            body['variables'] = variables

        resp = self._client.post('/graphql/', json.dumps(body),
                                 content_type='application/json')
        jresp = json.loads(resp.content.decode())
        return jresp

    def assertResponseNoErrors(self, resp: dict, expected: dict):
        self.assertNotIn('errors', resp, 'Response had errors')
        self.assertEqual(resp['data'], expected, 'Response has correct data')

    def test_search(self):
        query = """
        query interviewCardSuggestions ($query:String!){
          company(query:$query){
            id
            name
          }
        }
        """
        variables = {"query":"go"}
        resp = self.query(query,None,variables)
        self.assertResponseNoErrors(resp,{'company': [{'id': '2', 'name': '咕果'}]})

    def test_search(self):
        query = """
        query interviewCardSuggestions ($week: String!,$count:Int){
          hotSearchCompanies(week:$week,topCount:$count){
            id
            name
            isPremiumOnly
          }
        }
        """
        variables = {"week":"20190702","count":2}
        resp = self.query(query,None,variables)
        self.assertResponseNoErrors(resp,{'hotSearchCompanies': [{'id': '2', 'name': '咕果', 'isPremiumOnly': True}, {'id': '1', 'name': 'LeetCode（力扣）', 'isPremiumOnly': True}]})
