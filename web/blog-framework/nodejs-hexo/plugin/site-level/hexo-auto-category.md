---
title: 【Hexo插件系列】日志的自动分类插件 hexo-auto-category
date: 2018-04-01
abbrlink: e2f6e239
tags:
- hexo
- plugin
- category
- 自动分类
- hexo-auto-category
- 目录
- directory
- 博客
- 日志
---


# 简介

> hexo-generator-category  这个插件是生成tag文件的，不是用来自动生成category的。




## pain point

用hexo写博客，通常我们都需要自己管理category。理想情况下是对每个博客都设置目录树(categories变量)，这样很大的增加了用户的负担，以及后续的维护成本。

主要问题如下：

- 手写麻烦易出错。
- 一致性差：大小写和中英文目录有可能混杂。比如有个`web`目录，偶尔我们写成了`Web`，造成了目录树中冗余的节点。
- 可维护性差：如果要更改目录树中的节点，就要手动更改每个日志的`categories`变量。麻烦到吐

## hexo-auto-category

[hexo-auto-category官方地址](https://github.com/xu-song/hexo-auto-category)

最常用的文件管理策略，就是利用文件系统目录结构(树形结构 directory-tree)。
同样，为了便于管理大量的日志文件，采用目录结构是一种简便可行的方案。`hexo-auto-category`根据日志文件(Markdown)所在文件目录自动分类，即自动生成`markdown`的front-matter中的`categories`变量。


# 示例

对于博客  `source/_post/web/framework/hexo.md`，自动生成以下`categoris`
```yml
categories:
  - web
  - framework
```


# 可行性分析

- 结构通用：`categories`变量是树形结构，文件系统的目录也是树形结构。关于树形结构竟然也有[争议](https://github.com/hexojs/hexo/issues/848)



# 疑问

这是theme-level的，还是site-level的？
