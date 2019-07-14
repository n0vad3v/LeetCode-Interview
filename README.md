# LeetCode Interview Plugin

- Nova Kwok
- Miloas

## 概览

作为一个力扣（LeetCode） Interview 的功能增强，本插件使用 GraphQL 实现了以下两个功能接口：

- 搜索企业信息
- 统计各个自然周的热搜企业

## 背景

企业面试部分随后会增加企业，为了保证搜索的完整性以及对于用户搜索习惯的统计，我们需要两个接口完全后端的操作给前端进行调用。

## 里程碑

| 时间       | 事件                                           |
| ---------- | ---------------------------------------------- |
| 2019/07/11 | 开始项目                                       |
| 2019/07/11 | 完成企业以及搜索数据库结构确认                 |
| 2019/07/11 | 自学并实现了 GraphQL 查询企业以及热搜企业接口  |
| 2019/07/12 | 优化数据库结构，加入了每周企业搜索统计         |
| 2019/07/12 | 引入 Celery 对于企业搜索结果的更新进行延迟更新 |
| 2019/07/13 | 加入 redis 对于企业搜索以及热搜企业进行缓存    |
| 2019/07/13 | 持续优化接口                                   |
| 2019/07/14 | 代码审计，加入更多测试用例                     |
| 2019/07/14 | 在于 GitLab 做了很多斗争之后，完成了 CI        |

## 思路

### 数据持久化

关于数据库结构以及假数据生成请参考：[DB.md](./DB.md)

- MySQL 数据库 + Django loaddata 加入测试数据

### 缓存

- Redis

~~通过 MySQL 对数据进行持久化，数据的搜索使用 Agolia 完成，由于需要针对大量的搜索请求，每次搜索的结果不应该直接写入 MySQL，而应该丢入 redis 缓存。（建立 `公司-搜索数` 键值对完成 Cache，并通过计划任务每天凌晨同步进数据库。~~

由于对于公司的搜索不存在关键词全文检索的需求，所以不需要 Agolia 等三方服务，可以考虑直接使用数据库的 `LIKE` 语句对于关键词进行匹配，这样减少了实现的难度，不过提升了对于数据的查询压力，一些可以优化/已经优化的点参考 [OPTIMIZE.md](./OPTIMIZE.md)。

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