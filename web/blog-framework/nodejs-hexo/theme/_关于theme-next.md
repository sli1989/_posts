---
title: 关于theme-next
date: 2018-01-25 03:08:53
tag: ["hexo"]
categories:
- web
- blog-framework
---



# 简介


# 目录结构

```
├── _config.yml      // 主题配置项文件
├── languages        // 语言文件
├── layout           // 布局（模板）文件夹
├── scripts           
└── source    

```
## search



# bug

## Duplication of `keywords`

https://github.com/theme-next/hexo-theme-next/pull/115

Hexo has generate keywords from `page.keywords`, `page.tags` and `config.keywords` (not theme.keywords).
In [hexo](https://github.com/hexojs/hexo/blob/92827129f37600d5dd2939d28ef46f66db5e23dd/lib/plugins/helper/open_graph.js#L41)
```js
const keywords = page.keywords || (page.tags && page.tags.length ? page.tags : undefined) || config.keywords;

  if (keywords) {
    if (typeof keywords === 'string') {
      result += meta('keywords', keywords);
    } else if (keywords.length) {
      result += meta('keywords', keywords.map(tag => {
        return tag.name ? tag.name : tag;
      }).filter(keyword => !!keyword).join());
    }
  }
```
In [theme-next](https://github.com/theme-next/hexo-theme-next/blob/master/layout/_partials/head/head-unique.swig#L1)

```js
{% if page.keywords %}
  <meta name="keywords" content="{{ page.keywords }}" />
{% elif page.tags and page.tags.length %}
  <meta name="keywords" content="{% for tag in page.tags %}{{ tag.name }},{% endfor %}" />
{% elif theme.keywords %}
  <meta name="keywords" content="{{ theme.keywords }}" />
{% endif %}
```

I think it would be better to inherit Hexo keyword or overwrite it.

## solution
If you are concerning about lose some feature.  The following
