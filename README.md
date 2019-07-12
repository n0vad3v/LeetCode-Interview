你需要在这个项目中实现[LeetCode面试](https://leetcode-cn.com/interview)部分功能扩展

目标：实现热门企业搜索功能，记录一周内用户搜索最多的前五企业供前端调用。

你需要自己分析此业务场景，实现合理的后端支持，防范恶意请求，在数据量巨大的时候设计机制依然能保证查询性能。

要求：使用Django2.x，Mysql，Graphql（https://github.com/graphql-python/graphene， https://github.com/graphql-python/graphene-django），Celery，Redis实现以下接口，

\- SaveCompanySearchResult -> 用以统计搜索

\- HotSearchCompanies -> 用以获取热搜企业

***

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

## 思路

### 数据持久化

* MySQL 数据库 + Django loaddata 加入测试数据

### 用户搜索

* Agolia Search

### 缓存

* Redis

通过 MySQL 对数据进行持久化，数据的搜索使用 Agolia 完成，由于需要针对大量的搜索请求，每次搜索的结果不应该直接写入 MySQL，而应该丢入 redis 缓存。（建立 `公司-搜索数` 键值对完成 Cache，并通过计划任务每天凌晨同步进数据库。



## 测试数据

手动复制了一些并 dump 出来的：

```json
[
  {
    "model": "search.company",
    "pk": 1,
    "fields": {
      "slug": "tencent",
      "name": "腾讯 (Tencent)",
      "isPremiumOnly": true,
      "searchHitCount": 0
    }
  },
  {
    "model": "search.company",
    "pk": 2,
    "fields": {
      "slug": "teambition",
      "name": "Teambition",
      "isPremiumOnly": true,
      "searchHitCount": 1
    }
  },
  {
    "model": "search.company",
    "pk": 3,
    "fields": {
      "slug": "leetcode",
      "name": "LeetCode（力扣）",
      "isPremiumOnly": true,
      "searchHitCount": 1
    }
  },
  {
    "model": "search.company",
    "pk": 4,
    "fields": {
      "slug": "microsoft",
      "name": "Microsoft（微软）",
      "isPremiumOnly": true,
      "searchHitCount": 1
    }
  }
]
```

