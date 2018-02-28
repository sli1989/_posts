




# 如何解决百度爬虫无法爬取搭建在Github上的个人博客的问题？

## 现状 & 原因

### github做了什么。
- `robots.txt` 中屏蔽了baidu
- 即使百度爬虫无视robots协议强抓github，github也会通过`检查UA`，返回`403 forbidden`，即`拒绝访问`。(当然如果要想强抓是拦不住的，伪装一下UA即可)

### 造成的现状

- robots.txt 失效
- sitemap 失效

> 原因：github在robots.txt中屏蔽了百度，百度默认不抓取github的内容。

- 主动提交失效
- 自动提交失效
- 手动提交失效

> Github是通过 UA 来判定百度爬虫并返回 403 Forbidden 的

> 而百度爬虫的UA一般固定为 Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)

> 即使向百度提交了页面，github服务器一看UA是百度爬虫，就直接拒绝访问

### 如何解决

1. 换其他host服务器，比如coding.net
1. CDN
    - 百度爬虫不要直接向 Github 的服务器发送请求，而是通过 CDN 边缘服务器的缓存来抓取网站的内容。边缘服务器本身是不会关心 UA 的，所以问题就迎刃而解了。
    - [也不靠谱](http://jerryzou.com/posts/feasibility-of-allowing-baiduSpider-for-Github-Pages/)
    - https://www.dozer.cc/2015/06/github-pages-and-cdn.html


https://www.zhihu.com/question/30898326
