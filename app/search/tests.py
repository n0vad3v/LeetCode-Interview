from django.test import TestCase
import pytest

import search.schema
# Create your tests here.
def test_basic_search():
    # Search for 'le'
    query = """
    query interviewCardSuggestions ($query: String){
      company(query:"le"){
        id
        name
      }
    }
    """
    expected = {
      "data": {
        "company": [
          {
            "id": "1",
            "name": "力扣（LeetCode）"
          },
          {
            "id": "6",
            "name": "咕果科技"
          }
        ]
      }
    }

    result = schema.excute(query)
    assert not result.errors
    assert result.data == expected
