## LeetCode Interview Plugin

这个仓库用来完成对于已有公司的搜索，并且统计各个自然周的最热门公司情况。

## 要求

> 以下是官方要求

你需要在这个项目中实现[LeetCode面试](https://leetcode-cn.com/interview)部分功能扩展

目标：实现热门企业搜索功能，记录一周内用户搜索最多的前五企业供前端调用。

你需要自己分析此业务场景，实现合理的后端支持，防范恶意请求，在数据量巨大的时候设计机制依然能保证查询性能。

要求：使用Django2.x，Mysql，Graphql（https://github.com/graphql-python/graphene， https://github.com/graphql-python/graphene-django），Celery，Redis实现以下接口，

\- SaveCompanySearchResult -> 用以统计搜索

\- HotSearchCompanies -> 用以获取热搜企业

## 思路

### 数据持久化

关于数据库结构以及假数据生成请参考：[DB.md](./DB.md)

- MySQL 数据库 + Django loaddata 加入测试数据

### 缓存

- Redis

~~通过 MySQL 对数据进行持久化，数据的搜索使用 Agolia 完成，由于需要针对大量的搜索请求，每次搜索的结果不应该直接写入 MySQL，而应该丢入 redis 缓存。（建立 `公司-搜索数` 键值对完成 Cache，并通过计划任务每天凌晨同步进数据库。~~

由于对于公司的搜索不存在关键词全文检索的需求，所以不需要 Agolia 等三方服务，可以考虑直接使用数据库的 `LIKE` 语句对于关键词进行匹配，这样减少了实现的难度，不过提升了对于数据的查询压力，一些可以优化的点参考 [OPTIMIZE.md](./OPTIMIZE.md)。

## 安装 & 复现

环境要求：

* Python 3
* MySQL，且已经设置为 `utfmb4` 编码（[Django 使用 MySQL 中文報錯](https://ignorance.nova.moe/django-mysql-encoding-error-on-chinese/)）

创建好目录之后，clone 下本仓库，进入 `app` 目录后创建虚拟环境并进入：

```bash
cd app
python -m venv env
source env/bin/activate
```

安装所有需要的包：

```
pip3 install -r requirements.txt
```

创建本地的 `settings.py` 配置文件：

```bash
cd Interview
cp settings.py.example settings.py
```

创建超级用户：

```
python manage.py createsuperuser
```

迁移数据库模型：

```
python manage.py migrate
```

导入测试数据：

> 参考 [DB.md](./DB.md)

运行 redis，Django 和 Celery：

```bash
systemctl start redis
python manage.py runserver
celery -A search worker -l info
```

访问：[http://localhost:8000/graphql](http://localhost:8000/graphql)，开始发起请求，请求相关见：[GRAPHQL.md](./GRAPHQL.md)