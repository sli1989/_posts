---
title: Hexo 插件推荐
categories:
  - web
  - blog-framework
  - nodejs-hexo
  - plugin
abbrlink: 92bb368
date: 2018-03-31 00:00:00
---

# 综述
官方收录插件：[hexo.io/plugins/](https://hexo.io/plugins/)


我现在的博客，采用的是`hexo-abbrlink` + `hexo-auto-category`插件。  前者生成`路径无关`的hash作为URL，比较鲁棒。后者提供`依赖路径`的category，既自动生成category，又能方便在浏览器端`定位到日志的文件路径`。


# 可视化插件

- fancy box大赞

- chart相关，很多插件

# 博客管理插件

## 博客分类(category)自动管理

[hexo-auto-category](https://github.com/xu-song/hexo-auto-category)

根据日志(Markdown文件)所在目录层级自动分类。用户只需要把日志按照目录的方式组织，该插件就会在日志头部自动生成category标签。

既方便管理日志，又省去了人工维护`categories`标签的麻烦。

<!--
发现自己貌似重新造了个轮子 hexo-directory-category
-->


## markdown文件的引用

[hexo-include-markdown](https://github.com/tea3/hexo-include-markdown) 避免了多个博客写重复的内容。

```md
---
title: Hello World
---

## include sample

Please load another markdown file with the following code.

<!-- md template.md -->
```


# SEO插件


## 永久链接(permalink)插件 - hexo-abbrlink

 -

URL的设计尽量做到以下几点：

- 不变性/鲁棒性：`date>title>path>content`，即内容更新最频繁，标题和日期变动较少。
  - ~~path~~，~~content~~ 这俩被pass了
- 唯一性：`content path title date` 唯一性都挺好
- 长度要短 & 容量要大：
  - ~~content~~



Hexo默认采用 date+path作为URL，唯一性很好，但是鲁棒性就比较差（对于我）。像我就经常改变文件的路径，对文件重新归纳整理，这样会造成批量URL变动，严重影响SEO。

## 重复网页 权威链接 - hexo-auto-canonical

据估计，网上有10%-30%的URL是内容相同但URL不一样的不规范化网址。

解决，做301重定向

```js
hexo.extend.helper.register('autoCanonical', function (config, page) {
  var base_url = config.url;
  if (config.url.charAt(config.url.length - 1) !== '/') base_url += '/';

  return '<link rel="canonical" href="' + base_url + page.canonical_path.replace('index.html', '').toLowerCase() + '"/>';
});
```

什么鬼？这么简单？

## hexo-autonofollow

Add rel="external nofollow" to all external links, SEO friendly.
Add target="_blank", Open external links in new window or tab

## baidu SEO 相关插件

反正我一直没搞定百度。难道是因为网站没备案？



# 推荐系统插件

- [hexo-related-popular-posts](https://github.com/tea3/hexo-related-popular-posts)
采用的相似tag作为推荐标准，需要自己合理设置日志的tag

# 内容扩展插件

## Instagram扩展

instagram提供内嵌脚本，只不过有点长，直接贴到markdown也还将就。

[hexo-tag-instagram](https://github.com/tea3/hexo-tag-instagram)




示例：
```js
{% instagram https://www.instagram.com/p/Bg71nq4HuAU/ %}
```

{% instagram https://www.instagram.com/p/Bg71nq4HuAU/ %}

## facebook扩展

## hexo-tag-bilibili

## youtube

{% youtube video_id %}

https://hexo.io/zh-cn/docs/tag-plugins.html

## twitter扩展

[hexo-tag-twitter](https://github.com/tea3/hexo-tag-twitter)

示例：
```js
{% twitter https://twitter.com/realDonaldTrump/status/976891486510907393 %}
```

{% twitter https://twitter.com/realDonaldTrump/status/976891486510907393 %}



## 微博扩展

## flickr扩展

貌似直接`<img>`标签就能搞定

## soundcloud扩展

hexo-tag-soundcloud

{% soundcloud https://soundcloud.com/rich-the-kid/plug-walk-1 %}

## 代码扩展

gist提供内嵌脚本

# 加速 & 优化

- cdn：hexo-cdnify
- minify: hexo-all-minifier
- hexo-asset-pipeline

# 无聊 鸡肋 插件 (纯属个人意见)

前端加密类：hexo-encrypt.  

hexo-blog-encrypt  [原理见博客](http://edolphin.site/2016/05/31/encrypt-post/)


````
 var content = CryptoJS.AES.decrypt(document.getElementById("encrypt-blog").innerHTML.trim(), pass);
```


插件无关类(功能独立，无须作为hexo插件)：hexo-beautify

# Hexo博客推荐

<!--
- https://photo-tea.com  很赞，虽然看不懂写的是什么。[Github](https://github.com/tea3/)
- https://blog.zthxxx.me/
-->
