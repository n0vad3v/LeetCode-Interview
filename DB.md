数据库设计方面，由于我们需要统计每周各个公司的被搜索情况，这里采用两个表， Company 表用来记录公司的信息，Search 表用来记录每个公司在不同的周的被搜索情况，属于一对多的关系。

### Search Table

| slug（ refer on Company.slug） | Week of Month                 | Hits |
| ------------------------------ | ----------------------------- | ---- |
| leetcode                       | 20190702(Week 2 of July 2019) | 20   |
| leetcode                       | 20190701(Week 1 of July 2019) | 290  |
| tencent                        | 20190701(Week 1 of July 2019) | 218  |

### Company Table

| name             | slug     | pinyin  | isPremiumOnly |
| ---------------- | -------- | ------- | ------------- |
| 力扣（LeetCode） | leetcode | likou   | True          |
| 腾讯             | tencent  | tengxun | True          |
|                  |          |         |               |