你需要在这个项目中实现[LeetCode面试](https://leetcode-cn.com/interview)部分功能扩展

目标：实现热门企业搜索功能，记录一周内用户搜索最多的前五企业供前端调用。

你需要自己分析此业务场景，实现合理的后端支持，防范恶意请求，在数据量巨大的时候设计机制依然能保证查询性能。

要求：使用Django2.x，Mysql，Graphql（https://github.com/graphql-python/graphene， https://github.com/graphql-python/graphene-django），Celery，Redis实现以下接口，

\- SaveCompanySearchResult -> 用以统计搜索

\- HotSearchCompanies -> 用以获取热搜企业