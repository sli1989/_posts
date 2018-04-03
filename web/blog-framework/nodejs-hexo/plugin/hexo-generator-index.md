---
title: 【Hexo插件系列】hexo-generator-index
keywords:
  - hexo
  - 博客
  - 插件
  - 置顶
  - top
  - 排序
categories:
  - web
  - blog-framework
  - nodejs-hexo
  - plugin
abbrlink: 70564e
tags:
  - hexo
  - plugin
  - generator
  - hexo-generator-index
date: 2018-04-02 00:00:00
---

# 简介

Hexo默认提供了按发布日期的排序，即hexo-generator-index

核心逻辑：

[index.js](https://github.com/hexojs/hexo-generator-index/blob/master/index.js)
```js
var assign = require('object-assign');

hexo.config.index_generator = assign({
  per_page: typeof hexo.config.per_page === 'undefined' ? 10 : hexo.config.per_page,
  order_by: '-date'  // 默认提供了按发布日期的排序
}, hexo.config.index_generator);

hexo.extend.generator.register('index', require('./lib/generator'));
```

[generator.js](https://github.com/hexojs/hexo-generator-index/blob/master/lib/generator.js)
```js
var pagination = require('hexo-pagination');

module.exports = function(locals) {
  var config = this.config;
  var posts = locals.posts.sort(config.index_generator.order_by); // 默认 sort by date
  var paginationDir = config.pagination_dir || 'page';
  var path = config.index_generator.path || '';

  return pagination(path, posts, {
    perPage: config.index_generator.per_page,
    layout: ['index', 'archive'],
    format: paginationDir + '/%d/',
    data: {
      __index: true
    }
  });
};
```


# Hexo文章置顶的最优解决方案

## 被pass的方案 - 加top属性

github issue

- https://github.com/hexojs/hexo-generator-index/pull/6
- https://github.com/hexojs/hexo-generator-index/pull/9

这两个PR并未被merge，很有道理。


## 最优方案

通过date置顶。比如

```yml
date: 2020-01-01
```

这样就很容易置顶了

Hexo文章置底也是同样的道理，比如设置日期为2000年，或者1000年来实现文章置底。
