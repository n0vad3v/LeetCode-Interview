## LeetCode InterView Official

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

***

## LeetCode-Interview

### Company Search

对于公司的搜索，支持模糊搜索（关键词为：名称，slug 和 拼音（通过 pinyin 库生成）），搜索的 Query 为：

```json
query interviewCardSuggestions ($query: String!){
  company(query:$query){
    id
    name
  }
}
```

其中，需要传入的 Variable 为：

```json
{
  "query": "le"
}
```

示例返回：

```json
{
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
```

其中，「咕果科技」由于其 slug 为「google」，包含了 「le」，还有不少优化的地方。

### Top Search

完成对于某一周被搜索次数最多的公司的查询。

```json
query interviewCardSuggestions ($week: String!,$count:Int){
  hotSearchCompanies(week:$week,topCount:$count){
    id
    name
    isPremiumOnly
  }
}
```

其中，需要传入的 Variable 为，其中，`week` 为必须项（避免忘了写（或者被估计攻击） `week` 被一瞬查询出所有结果），`count` 为非必须项，留空则查询所有公司（个人感觉公司不会非常非常多，所以这里允许留空）。

```json
{
  "week": "20190702",
  "count": 2
}
```

返回示例：

```json
{
  "data": {
    "hotSearchCompanies": [
      {
        "id": "6",
        "name": "咕果科技",
        "isPremiumOnly": true
      },
      {
        "id": "4",
        "name": "诺华网络",
        "isPremiumOnly": true
      }
    ]
  }
}
```

对于没有数据的查询，比如 Variable 改为上一周：

```json
{
  "week": "20190701",
  "count": 2
}
```

返回结果为空：

```json
{
  "data": {
    "hotSearchCompanies": []
  }
}
```

