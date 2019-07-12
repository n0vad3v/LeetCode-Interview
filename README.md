你需要在这个项目中实现[LeetCode面试](https://leetcode-cn.com/interview)部分功能扩展

目标：实现热门企业搜索功能，记录一周内用户搜索最多的前五企业供前端调用。

你需要自己分析此业务场景，实现合理的后端支持，防范恶意请求，在数据量巨大的时候设计机制依然能保证查询性能。

要求：使用Django2.x，Mysql，Graphql（https://github.com/graphql-python/graphene， https://github.com/graphql-python/graphene-django），Celery，Redis实现以下接口，

\- SaveCompanySearchResult -> 用以统计搜索

\- HotSearchCompanies -> 用以获取热搜企业

***

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
      "slug": "leetcode",
      "name": "力扣（LeetCode）",
      "pinyin": "likou（LeetCode）",
      "isPremiumOnly": true
    }
  },
  {
    "model": "search.company",
    "pk": 2,
    "fields": {
      "slug": "tencent",
      "name": "腾讯",
      "pinyin": "tengxun",
      "isPremiumOnly": true
    }
  },
  {
    "model": "search.company",
    "pk": 3,
    "fields": {
      "slug": "cqjtu",
      "name": "重庆交通大学",
      "pinyin": "zhongqingjiaotongdaxue",
      "isPremiumOnly": true
    }
  },
  {
    "model": "search.company",
    "pk": 4,
    "fields": {
      "slug": "novanetwork",
      "name": "诺华网络",
      "pinyin": "nuohuawangluo",
      "isPremiumOnly": true
    }
  },
  {
    "model": "search.company",
    "pk": 5,
    "fields": {
      "slug": "minecraft",
      "name": "我的世界",
      "pinyin": "wodeshijie",
      "isPremiumOnly": true
    }
  },
  {
    "model": "search.company",
    "pk": 6,
    "fields": {
      "slug": "google",
      "name": "咕果科技",
      "pinyin": "guguokeji",
      "isPremiumOnly": true
    }
  },
  {
    "model": "search.search",
    "pk": 1,
    "fields": {
      "slug": 1,
      "week": "20190702",
      "search_hit": 20
    }
  },
  {
    "model": "search.search",
    "pk": 2,
    "fields": {
      "slug": 6,
      "week": "20190702",
      "search_hit": 200
    }
  },
  {
    "model": "search.search",
    "pk": 3,
    "fields": {
      "slug": 4,
      "week": "20190702",
      "search_hit": 180
    }
  },
  {
    "model": "search.search",
    "pk": 4,
    "fields": {
      "slug": 5,
      "week": "20190702",
      "search_hit": 180
    }
  },
  {
    "model": "search.search",
    "pk": 5,
    "fields": {
      "slug": 3,
      "week": "20190702",
      "search_hit": 29
    }
  }
]
```



