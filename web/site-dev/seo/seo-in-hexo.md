---
title: Hexo中的SEO技巧
tags:
  - domain
  - SEO
  - hexo
categories:
  - web
  - site-dev
abbrlink: 8b29356c
date: 2018-03-04 00:00:00
---


## 关于keywords

为每个post添加tag，因为tag会被放入页面的`keywords`

```html

{% if page.keywords %}
  <meta name="keywords" content="{{ page.keywords }}" />
{% elif page.tags and page.tags.length %}
  <meta name="keywords" content="{% for tag in page.tags %}{{ tag.name }},{% endfor %}" />
```


每个页面 keywords 的选择顺序，是按照如下优先顺序进行

1. page 中定义的 keywords
1. page 中定义的 tags
1. _config.yml 中定义的 keywords (hexo中定义的keyword，不是theme的config)


源码
https://github.com/hexojs/hexo/blob/master/lib/plugins/helper/open_graph.js

https://github.com/theme-next/hexo-theme-next/blob/master/layout/_partials/head/head-unique.swig


建议tags标签和keywords标签都加。由于keywords在页面不会展示，因此添加更自由，添加面向SEO的标签。

## 关于robots.txt 和 sitemap.xml

## 参考

http://www.restran.net/2017/05/02/hexo-custom-html-meta-keywords/
