# GHActEval

# 简介


根据指定的仓库坐标分析其在github的社区活跃度，主要包含六个维度：

- Stars
- Forks
- Total Community Engagement
- 6-Month Community Engagement Overview
- Annual Contributors Overview
- 12-Month Commit Summary

分析结果如下:

<p align = "center">    
<img  src="https://github.com/yanghaiji/GHActEval/blob/main/doc/img/img.png" width="400" />
</p>


# 启动配置

- 修改github_token 
>修改application.yaml 里github_token 的值,配置成自己的token
> 
> [关于如何获取token可以参考 managing-your-personal-access-tokens](https://docs.github.com/zh/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

- 修改repos配置
修改application.yaml 里repos的配置,配置成您想分析分仓库集合,需要提供到组织的维度,如下
```
repos:
# 数据库连接池
  - brettwooldridge/HikariCP
  - apache/commons-dbcp
  - swaldman/c3p0
  - h2database/h2database
  - vibur/vibur-dbcp
  - alibaba/druid
```

