数据库设计方面，由于我们需要统计每周各个公司的被搜索情况，这里采用两个表， Company 表用来记录公司的信息，Search 表用来记录每个公司在不同的周的被搜索情况，属于一对多的关系。

### Search Table

| id(pk) | company_id（ refer on Company.id） | Week of Month                 | Hits |
| ------ | ---------------------------------- | ----------------------------- | ---- |
| 1      | 1                                  | 20190702(Week 2 of July 2019) | 20   |
| 2      | 1                                  | 20190701(Week 1 of July 2019) | 290  |
| 3      | 2                                  | 20190701(Week 1 of July 2019) | 218  |

### Company Table

| id(pk) | name             | slug     | pinyin  | isPremiumOnly |
| ------ | ---------------- | -------- | ------- | ------------- |
| 1      | 力扣（LeetCode） | leetcode | likou   | True          |
| 2      | 腾讯             | tencent  | tengxun | True          |

## Fake Data

由于 Django 似乎没有一个好用的 Faker，所以自己写了一个用来生成假数据的脚本，默认生成 25W 条公司数据 + 25W 条公司被搜索数据（一一对应，时间为 20190702，访问数量随机生成）

在 seeds 目录下：

```
python gen_company_seeds.py
```

即可开始生成假数据，文件名为：`fake_companies.json`，将此文件移动到 `app` 目录下，并使用：

```
python manage.py loaddata fake_companies.json
```

进行导入。