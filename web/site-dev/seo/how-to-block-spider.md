---
title: 禁止搜索引擎收录的方法
tags:
  - 域名
  - web
  - robot协议
  - 搜索引擎
categories:
  - web
  - site-dev
  - seo
abbrlink: c429c70d
date: 2018-02-27 00:00:00
---
# 什么是robots协议

Robots协议（也称为爬虫协议、机器人协议等）的全称是“网络爬虫排除标准”（Robots Exclusion Protocol），网站通过Robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取。搜索引擎抓取网站内容前会先抓取robots.txt，据此“自觉地”抓取或者不抓取该网页内容，其目的是保护网站数据和敏感信息、确保用户个人信息和隐私不被侵犯。

需要注意的是robots协议并非是规范，只是行业内一个约定俗成的协议。什么意思呢?Robots协议不是什么技术壁垒，而只是一种互相尊重的协议，好比私家花园的门口挂着“闲人免进”，尊重者绕道而行，不尊重者依然可以推门而入，比如说360。

如果网站有数据需要保密，必需采取技术措施，比如说：用户验证，加密，ip拦截，访问频率控制等。




# 为什么要禁止搜索引擎收录

1. 某些路径下是个人隐私或者网站管理使用，不想被搜索引擎抓取
1. 不喜欢某个搜索引擎，不愿意被他抓取，最有名的就是之前淘宝不希望被百度抓取
1. 流量有限或者需要付费，希望搜索引擎抓的温柔点。
1. 阻止竞争抓取自己的网站内容，比如搜索引擎之间相互屏蔽，360


# robots的屏蔽恩怨历史

汇总

|                    | 百度 | google | bing | 备注                                                                 |
|--------------------|------|--------|------|----------------------------------------------------------------------|
| 淘宝               | ×    | √      | √    | 不屏蔽google，因为google不做淘宝的竞价排名。另外还能作为淘宝流量入口 |
| 京东               | √    | √      | √    |                                                                      |
|                    |      |        |      |                                                                      |
| 微信公众平台       |      |        |      |                                                                      |
| 社交网络--开放空间 |      |        |      |                                                                      |
| weibo              |      |        |      |                                                                      |
| facebook           |      |        |      |                                                                      |
| twitter            |      |        |      |                                                                      |
| 社交网络--隐私空间 |      |        |      |                                                                      |
| qq空间             |      |        |      |                                                                      |
| 微信朋友圈         |      |        |      |                                                                      |
|                    |      |        |      |                                                                      |
| baidu、google      | ×    | ×      | ×    | 搜索引擎，屏蔽一切搜索引擎爬虫                                       |
|                    |      |        |      |                                                                      |
|                    |      |        |      |                                                                      |
## github - 屏蔽百度、搜狗、360等

### 为什么屏蔽百度

> We are currently blocking the Baidu user agent from crawling GitHub Pages sites in response to this user agent being responsible for an excessive amount of requests, which was causing availability issues for other GitHub customers.

> This is unlikely to change any time soon, so if you need the Baidu user agent to be able to crawl your site you will need to host it elsewhere.

> -- by <a href="http://jerryzou.com/posts/feasibility-of-allowing-baiduSpider-for-Github-Pages/">Github Support</a> Jerry's blog


即百度爬虫爬得太猛烈，已经对很多 Github 用户造成了可用性的问题了，而禁用百度爬虫这一举措可能会一直持续下去。



白名单中竟然有 EtaoSpider。why？
为什么百度中搜索`site:github.io`有结果？

`www.github.com`中的[robots.txt](www.github.com/robots.txt)
```yml
User-agent: Googlebot   # google yandex等都在白名单。
Allow: /*/*/tree/master
Allow: /*/*/blob/master

User-agent: *   
Allow: /humans.txt
Disallow: /      # 百度不在白名单，即整个站点屏蔽百度
```

除设置了robots.txt之外，github后台服务器还会检查HTTP请求的UA，如果是百度就返回403 forbidden。

## 电商
### 淘宝 - 屏蔽百度

- 争夺流量入口
-
- .

2008年淘宝屏蔽了百度搜索引擎，自此用户再也无法从百度直接搜索到关于淘宝的信息。

淘宝网站曾经屏蔽百度搜索爬虫，禁止百度搜索引擎抓取淘宝网站的网页内容，淘宝官方的解释是“杜绝不良商家欺诈”。

首先，在08年9月淘宝先屏蔽了百度搜索，使得当我们在百度搜索淘宝产品名时，百度返回不到有效信息。导致普通网民在进行网上购物行为时，会直接选择登陆淘宝网，用站内搜索进行，从上网入口上讲，淘宝这样就让网民一步到位了，而不是单单记住百度这个工具，淘宝的流量肯定会水涨船高，带来的好处也不言而明。

如果当初淘宝没有屏蔽百度，不多说：最起码30%的购物搜索会来自百度。淘宝屏蔽百度以后，淘宝真正的成为了购物的第一入口。



淘宝主页`www.taobao.com`的[robots.txt](www.taobao.com/robots.txt)
```yaml
User-agent: Baiduspider
Allow: /article
Allow: /oshtml
Disallow: /product/  # 禁止百度抓取www.taobao.com/product/
Disallow: /          # 屏蔽网站其他路径

User-Agent: Googlebot
Allow: /article
Allow: /oshtml
Allow: /product   # 对google很宽松，即开放google入口，
Allow: /spu
Allow: /dianpu
Allow: /oversea
Allow: /list
Disallow: /
```
淘宝商品页面`item.taobao.com`的[robot.txt](https://item.taobao.com/robots.txt)

```yml
User-agent: Baiduspider   # 百度，你被完全屏蔽了
Disallow: /

User-Agent: Googlebot     # 对google和bing开放
Allow: /item.htm

User-agent: Bingbot
Allow: /item.htm
```

搜索示例：
1. 关键词搜索 - 百度
  - `洗面奶 淘宝` 搜不到淘宝的商品。
  - `洗面奶 京东` 能搜到京东的商品。
2. 站点搜索 - 百度
  - `site:www.taobao.com 洗面奶` 竟然能搜索`www.taobao.com/product/`中的页面，点进去是无效商品链接
  - `site:www.jd.com 洗面奶` 能搜到京东的商品


### 京东 - 屏蔽一淘(阿里) 惠惠(网易)

京东和阿里向来水火不容，京东不准用户使用支付宝支付，也因为新浪和阿里的关系不准用户用新浪微博登录。2011年10月，京东和当年淘宝屏蔽百度一样，毅然屏蔽了一淘搜索。失去京东这么大的一个电商平台，一淘可谓流年不顺。

```yml
User-agent: *
Disallow: /?*
Disallow: /pop/*.html
Disallow: /pinpai/*.html?*

User-agent: EtaoSpider  # 屏蔽一淘
Disallow: /

User-agent: HuihuiSpider # 屏蔽惠惠购物助手
Disallow: /
```

阿里旗下自家的比价产品一淘网曾因抓取京东的商品数据而被京东通过代码进行干扰，刘强东亦亲自出来抨击一淘网，但是嘴仗一时痛快，最终的结果却是一淘至今仍然可以索引京东，而京东的抗争只能是停止与支付宝的合作。


为什么taobao不屏蔽惠惠购物助手？

这是阿里抛出的交易筹码，即如果比价软件想要全年抓取天猫淘宝等站的数据，作为与我这边发放通行证的交换，比价软件需要遵从的是在“双十一”期间主动阉割，否则就会尝到终身制的闭门羹。

参考--[如何看待惠惠购物助手被迫在双十一期间停止比价功能？](https://www.zhihu.com/question/37369996)

### amazon


## 社交网络/媒体

### QQ空间
QQ空间自05年诞生时就没有开放给百度与谷歌，和Facebook一样封闭。QQ的逻辑是要将QQ空间打造成一个巨大的闭环，唯一的搜索只能是旗下的搜搜。

2012年的时候，QQ空间也终于向百度与谷歌开放。

现在网友多数将自己的空间设置的为加密空间、非好友不能访问，所以里面的日志是没办法搜索；

### 新浪微博


### 微信公众平台 - 屏蔽所有

微信做了公众账号后，积累了大量高质量的作者和文章。为了对这种优质数据进行独家保护，微信利用robot协议，不允许所有搜索引擎进行内容抓取。

```yaml
User-Agent: *
Allow: /$
Allow: /debug/   # 微信公众平台接口调试工具
Allow: /qa/  
Allow: /wiki/
Allow: /cgi-bin/loginpage
Disallow: /     # 公众号文章
```

后来，腾讯投资搜狗，开放微信数据供搜狗搜索独家使用，[搜狗 微信搜素](http://weixin.sogou.com/)，将微信的公众号文章嵌入了搜狗搜索中。



## Facebook -  屏蔽谷歌搜索

Facebook屏蔽谷歌的原因也很简单，用户在Facebook上产生的内容势必会有能够带来商业价值的数据并且同时也涉及到用户隐私，所以Facebook也同样不会将这些数据轻易交付给第三方的。facebook至今仍然屏蔽谷歌搜索。


## 新闻站点

### 默多克旗下新闻 - 屏蔽谷歌搜索，后来又开放

从传统媒体起家的默多克，对于搜索引擎的态度相当不友善，默多克曾说`搜索引擎是“网络寄生虫”`。

默多克原话“他们是Google,他们是微软,他们是Ask.com,他们不应该免费获得内容,我想我们一直睡着了.”而默多克在09年开始展开计划，对谷歌等搜索引擎展开行动，对旗下多家新闻网站屏蔽搜索爬虫。

谷歌的回应也很简单明了”如果贵站不想在谷歌上出现，请修改贵站的robots文件即可“。不过到了2012年，默多克就投降了，`默多克向谷歌认输，重新允许搜索抓取报纸网站`。其实默多克的想法还是停留在传统的付费阅读的思维上，缺少对网络的深刻洞察。

## 搜索引擎 - 互相屏蔽 - 偷抓
sogou、baidu、360、google

[百度诉360违反Robots协议 一审判360赔偿70万](http://tech.163.com/14/0807/12/A31UJS5P000915BD.html)
360方面认为，Robots协议并不具有任何法律效力，而是百度利用了Robots协议自设白名单，谷歌、微软必应、雅虎、搜狗、SOSO等搜索引擎均可以抓取这些内容，唯独禁止360搜索抓取，属于打压竞争对手，涉嫌违反《反垄断法》。


[网曝百度不顾robots协议擅自抓取微信内容](http://lusongsong.com/blog/post/1472.html) baidu通过大量抓取[搜狗中的微信数据](weixin.sogou.com)，将其放入搜索结果中，用于提升自己的搜索体验。

[百度违反 Robots 协议抓搜狗数据，有图有真相有撕逼 - 知乎](https://www.zhihu.com/question/38937716)

搜狗与360曾互诉对方不正当竞争，并提出千万级别的索赔。

sogou偷爬baidu，baidu偷爬搜狗

http://weixin.sogou.com






[2013年，百度诉奇虎360违反“Robots协议”抓取、复制其网站内容的不正当竞争行为一案，索赔金额高达一亿元](http://lusongsong.com/reed/732.html)


### 参考
[虎嗅-盘点那些robots的屏蔽恩怨历史](https://www.huxiu.com/article/21696.html)

# 如果搜索引擎不遵守robot协议呢？

搜索引擎不遵守robot协议，对网站都抓，会违法吗？

robot协议是规定还是法律，不遵守robot协议是道德问题还是法律问题？
robots.txt 协议不是法律法规，也不是行业规范。但是一个搜索引擎声称自己遵守 robots.txt 协议那就有道德责任遵守。

## ss



# 如何在技术上反爬虫

检查UA


# s
