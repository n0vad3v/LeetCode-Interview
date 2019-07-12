官方搜索：

```json
{
  "operationName": "interviewCardSuggestions",
  "variables": {
    "query": "Te"
  },
  "query": "query interviewCardSuggestions($query: String!) {\n  interviewCardSuggestions(query: $query) {\n    id\n    isFavorite\n    isPremiumOnly\n    company {\n      slug\n      name\n      __typename\n    }\n    __typename\n  }\n}\n"
}
```

官方 Response：

```json
{
  "data": {
    "interviewCardSuggestions": [
      {
        "id": "28",
        "isFavorite": null,
        "isPremiumOnly": true,
        "company": {
          "slug": "tencent",
          "name": "腾讯 (Tencent)",
          "__typename": "InterviewCompanyNode"
        },
        "__typename": "InterviewCardNode"
      },
      {
        "id": "188",
        "isFavorite": null,
        "isPremiumOnly": true,
        "company": {
          "slug": "teambition",
          "name": "Teambition",
          "__typename": "InterviewCompanyNode"
        },
        "__typename": "InterviewCardNode"
      }
    ]
  }
}
```

## 