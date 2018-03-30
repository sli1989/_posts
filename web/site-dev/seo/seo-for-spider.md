---
title: 关于SEO
keywords:
  - domain
  - SEO
  - 域名
  - 搜索引擎
  - 站长
  - sitemap
  - 爬虫
tags:
  - domain
  - SEO
categories:
  - web
  - site-dev
abbrlink: 435df108
date: 2018-01-25 00:00:00
---

# 简介

## 如何检查自己网站是否被baidu google检索
site:xu-song.top git
site:xu-song.github.io git

## 提交百度检索

https://ziyuan.baidu.com/linksubmit/url

 >百度搜索资源平台为站长提供链接提交通道，您可以提交想被百度收录的链接，百度搜索引擎会按照标准处理，但不保证一定能够收录您提交的链接。

[Hexo 博客添加百度sitemap](https://blog.paddings.cn/2016/05/14/blog/hexo-sitemap/)

[hexo部署在github，用百度的站长收录sitemap，抓取失败怎么办？](https://www.zhihu.com/question/37633687)
Github屏蔽了百度爬虫。
除了sitemap还有其他提交方法，还可以采用主动推送和自动推送，


## 为什么我的博客始终无法被百度收录

我在GoDaddy购买了域名，完成了在谷歌搜录，百度完成自动推送的设置后在sitemap一栏中填入我的域名始终显示sitemap抓取失败，请问这是什么问题我该如何解决呢   -- 知乎

github 禁止了百度的爬虫，你可以在 国内的 coding.net 上放一份，然后修改域名服务商的 CNAME 让国内的指向 coding.net ，国外的依然指向 github。具体你自己查下吧

> 就算放开了，肯定也没有国内的vps收录快。还有就是并不是所有的ip地址的权重都一样。爬虫有自己喜欢和不喜欢的ip群

如果完全没有外链，也不向百度提交，相当于孤岛，是不可能被收录的。
除非有人替你提交，或者本身百度数据库有你域名的记录。

没外链不代表孤岛，没外链你DNS修改时候百度等也有可能会知道，参考dnspod和百度合作的某文章……

## 有多个域名，怎么做最符合 SEO?

把其他域名都转发到主域名。很多人把不同的域名都解析到同一个网站，这样导致的结果是其他的域名没有对主域名起到任何作用，反而可能导致负面影响，如：让搜索引擎分不清到底哪一个是主域名。

搜索引擎对同一ip下的域名有互相推广的作用，给的比重越来越小了，多个域名同时解析到一个主机上，对SEO是有影响的，比如说：排名不好、PR值低、收录量少等问题。

对于多域名绑定建议从下面入手：

    1.使用301重定向功能。关于301重定向的操作需要注意的是：不要将次要网站中的所有网页的流量都重定向到主站上，这样做虽然节省了很多工作量，但是如果用户从搜索引擎上找过来，访问到的网页并不是他想要的内容，就会损失流量。尽可能做到页对页的重定向，保证用户从搜索引擎找过来的网页即使不是绝对匹配也是相关的内容。

    2.给次要的网站首页做一个导航,把流量指引到主站上；

    3.给次要的域名做URL转发；

一定要这样做：实现301重定向把次域名重定向到主域名去，避免权重分散，甚至被K，或者影响SEO排名。

- 301 redirect:：301代表永久性转移。301重定向是网页更改地址后对搜索引擎最友好的方法，只要不是暂时搬移的情况，都建议使用301来做转址。
- 302 redirect:：302代表暂时性转移。在前些年，不少Black Hat SEO曾广泛应用这项技术作弊。各大主要搜索引擎均加强了打击力度。(怎么作弊？)

当网页A用301重定向转到网页B时，搜索引擎可以肯定网页A永久的改变位置，或者说实际上不存在了，搜索引擎就会把网页B当作唯一有效目标。好处是，第一，没有网址规范化问题，第二，也很重要的，网页A的PR网页级别会传到网页B。



# SEO与跳转(重定向)

301 vs 302 vs meta-refresh tag

<img src="http://www.redalkemi.com/public/tinymce/images/uploads/2008/04/bot-blog4.jpg"></img>

[参考](http://www.redalkemi.com/blog/post/the-seo-war-of-redirects-301-vs-302-vs-meta-refresh-tag)

URL 重定向服务实际并非DNS 服务，它们在 HTTP 级别运行，而非 DNS 级别。使用URL转发的客户基本都是免费DNS的用户，当前业务暂不会投入支持。


## 301重定向
301 重定向，是指当用户通过浏览器访问某个 URL 时，Web 服务器被设置自动跳转到另外一个 URL，此时给客户端的返回码是 301。

### 应用场景

301 重定向一般用于两个 URL 之间的跳转。由于 301 重定向可以实现 URL 跳转后的权重转移，实现 SEO 优化，所以常用于如下场景：


- 网站有多个域名，但有一个主域名作为 SEO 推广对象，所有其他域名可以做 301 重定向到主域名，实现权重转移。
- 网站更换过域名，希望用新的域名作为 SEO 推广对象，当网站的用户访问旧域名时就会被 301 重定向到新的域名，实现权重转移。
  - 迁移后，访问统计归零。
  - 301重定向之后是不会承继老网站的关键词排名，只不过老网站的排名依然在而已，用户点击你的老域名会直接指向新域名
- 网站部分内容做过调整，URL 已经无法访问，可以做 301 重定向实现权重转移。

参考：

http://www.360doc.com/content/14/0212/15/13780192_351920352.shtml

http://www.hurencai.com/archives/453



### 服务器ip迁移
比如从gitpage迁移到coding page。

https://www.zhihu.com/question/19987112

###


## URL设计 与 SEO
- 静态URL
- 尽量英文，中文用拼音。(现在搜索引擎也对中文优化了，貌似中文url也不错，例如wikipedia的中文页面就采用的中文url)
- 字母全部小写
- URL中包含关键词
- url要短
- 单词之间一般建议使用短横线（-）分隔，不要使用下划线或者其他符号

## robots.txt

robots.txt位置固定，sitemap.xml需要在robots.txt中指定路径

必要性

# 提交链接的几种方式

Sitemap提交：在配置sitemap文件时，无论是txt格式的文本文档还是还是xml格式的文件。都不建议将其sitemap的文件名命名为sitemap.txt或sitemap.xml这么大众化且谁都能够知道的文件名。如果你这样设置，你的竞争对手或需要你网站内容的人很容易就能拿到你所有的页面url。出于保险起见还是使用一些自己定义的较复杂的文件名。每一个url都必须包含http://，文件中包含的url不得超过5万条，单文件大小不得超过10MB，一个站点最多提交5万个sitemap文件，超出5万个不再处理并会提示“链接数超”。如果是通过子域名的形式验证的站点。那么主域名下的sitemap文件是可以包含该域名下的所有域名的url的。

主动推送：

对比sitemap而言在及时抓取上推送更快、发现更快、抓取更及时。如果是时效性文章不排除其收录速度达到一瞬间的效率，这里特别建议一下，最好是主动推送我们网站第一时间产生的新内容给百度其效果更佳；主动推送是有推送数量的限制，尽可能的不要推送重复的内容给百度。这样会大大浪费自己的可推送资源。

自动推送：`在页面被访问时，页面URL将立即被推送给百度`。

## sitemap
爬虫会通过网页内部的链接发现新的网页。但是如果没有连接指向的网页怎么办?或者用户输入条件生成的动态网页怎么办?能否让网站管理员通知搜索引擎他们网站上有哪些可供抓取的网页?这就是sitemap，最简单的 Sitepmap 形式就是XML文件，在其中列出网站中的网址以及关于每个网址的其他数据(上次更新的时间、更改的频率以及相对于网站上其他网址的重要程度等等)，利用这些信息搜索引擎可以更加智能地抓取网站内容。

新的问题来了，爬虫怎么知道这个网站有没有提供sitemap文件，或者说网站管理员生成了sitemap，(可能是多个文件)，爬虫怎么知道放在哪里呢?

由于robots.txt的位置是固定的，于是大家就想到了把sitemap的位置信息放在robots.txt里。这就成为robots.txt里的新成员了。


站点地图对于百度失效。可以用主动推送和自动推送，


对于主域名下有多个2级域名的问题，应该是每一个二级域名都有自己独立的robots文件和sitemap。


必要性：不做也能收录。
最好做，为蜘蛛提供一个引导，有利于收录

知乎没有sitemap.xml，或许自定义了文件名


https://blog.eson.org/2018/03/04/web/site-dev/seo-in-hexo/

## 主动推送

调用接口
http://data.zz.baidu.com/urls?site=https://blog.eson.org&token=hOraXsrU6jl6Pifg"

### 应用实例

hexo的baidu主动推送[hexo-baidu-url-submit](https://github.com/huiwang/hexo-baidu-url-submit)

新链接的产生，hexo generate会产生一个文本文件，里面包含最新的链接
新链接的提交，hexo deploy会从上述文件中读取链接，提交至百度搜索引擎。

## 自动推送
页面每次被访问时，页面URL将立即被推送给百度。借助用户的浏览行为来触发推送动作，无需站长汇总URL再进行主动推送操作，省去了站长人工操作的时间。

### 源码
需要将这段js代码部署到我们的每一个网页中
```js
<script>
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);  //
})();
</script>
```

每当用户进行访问时，就会触发了这段代码，这段代码自动将当前页面的url推送给了百度。具体推送代码如下：

[push.js](https://zz.bdstatic.com/linksubmit/push.js)
```js
!function() {
    var e = /([http|https]:\/\/[a-zA-Z0-9\_\.]+\.baidu\.com)/gi
      , r = window.location.href
      , t = document.referrer;
    if (!e.test(r)) {
        var o = "https://sp0.baidu.com/9_Q4simg2RQJ8t7jm9iCKT-xh_/s.gif";
        t ? (o += "?r=" + encodeURIComponent(document.referrer),
        r && (o += "&l=" + r)) : r && (o += "?l=" + r);
        var i = new Image;
        i.src = o
    }
}(window);
```

比如每次访问页面`https://blog.eson.org`时，都会触发一个http请求`https://sp0.baidu.com/9_Q4simg2RQJ8t7jm9iCKT-xh_/s.gif?l=https://blog.eson.org/`。这就是自动推送。


### 应用实例：

hexo-theme-next中的baidu自动推送，[ baidu-push.swig](https://github.com/theme-next/hexo-theme-next/blob/master/layout/_third-party/seo/baidu-push.swig)


## 总结

建议同时配置这三种方式，并让三者协同工作，将抓取和收录价值最大化。


# 怎样判断网站有网址规范化问题？
1) 查一下这些URL是否都有差不多的PR值和网页快照：

http://domainname.com
http://www.domainname.com/index.html
http://domainname.com/index.html
http://www.domainname.com

2)搜一下site:domain.com看是否结果中有多个主页版本。

3)你的网站是否在Google有大量网页被标为“ 补充材料”(Supplemental Result)。一般认为被归为“ 补充材料”是网址规范化问题的征兆。

reference： https://www.seozac.com/seo/301-redirect/

site:.top
# tips
1. edu和gov后缀的域名天生权重更高。有些域名天生反链高，比如xxx   sex   之类的等等！
    - 百度说：使用何种形式的域名后缀对百度网页搜索没有影响

2. 注册时间越早的域名，越有利于排名。

3. 到期时间越晚的域名，越有利于排名。

4. 不同的子域名是会被当作独立网站处理的，不能继承主域名的权重。

5. 不同国家的域名，在本国会越有利于排名，比如http://abc.cn在中国会排名更好，而http://abc.us在美国会排名更好。

一个网站有多个域名没问题，请做好301跳转，别每个域名都可以访问。

gov和edu对排名有利，但对大多数人没什么指导意义，因为你根本弄不到这种后缀的域名。

域名买卖历史，（不涉及到违规行业越好）


惩罚 & 奖励
- 关键词堆砌
- 频繁的修改网页title、description和keywords
- 网站加上黑链
- 短时间内频繁的增加外链，或者短时间内大量的删除外链
- 服务器不稳定，网站经常打不开活域名解析错误。
- 全站 HTTPS，谷歌对 HTTPS 有加分
- 响应式设计，谷歌对提供友好移动端友好页面有加分
- AMP，谷歌对提供 AMP 支持的网站有加分
- PWA，谷歌对 PWA 有加分
- 加载优化，谷歌对 Pageseed 测试 90 分以上的网站有加分


- 页面内容持续不断更新，迎合了搜索引擎喜新厌旧的特性。
- 关键词密度要提升，但不是堆积
- 高质量内容出现在代码更靠前的位置，方便搜索引擎识别抓取。

- 内容很少的页面搜索引擎肯定不喜欢

## tricks

有很多大学生在他们大学的个人网站上出卖链接。搜索引擎怎样去辨别哪些来自.edu的链接是自然的？哪些又是买卖的呢？


## seo诊断
bing站长有SEO Analyzer。

### title长度

诊断我的主页，title太短，因为只有四个字母ESON。

> Recommended Action:
Change the length of the title to be between 5 and 100 characters

> SEO Explanation:
If the title is too short, it may not provide us and users with enough information to understand the relevancy of your page.  If the title is too long, we may need to shorten it in the search results and your keywords may not appear on the search results page.  You should try to keep the length of the title somewhere between at least 5 characters and 100 characters.

### description长度

> Recommended Action:
Change the description in the <meta description> tag in the page source to be between 25 and 160 characters in length.

> SEO Explanation:
Search engine crawlers only show the first 150-160 characters of the description in the search results page, so if a description is too long, searchers may not see all of the text. If a description is too short, the search engines may add text found elsewhere on the page. Note that search engines may show a different description from the one you have authored if they feel it may be more relevant to a user's search.


### <h1> tag数量太多
https://blog.eson.org/2018/01/25/web/site-dev/seo/seo-for-spider/

> There are multiple <h1> tags on the page.
> Recommended Action:
Remove redundant <h1> tags from the page source, so that only one <h1> tag exists.

### <img> tag 的 ALT属性


> Recommended Action:
Use the <img alt> attribute to write descriptive content for the image: <img source="pic.gif" alt="Accurate and descriptive keyword text that represents the image."</img>.

> SEO Explanation:
As a general rule, search engines do not interpret the content of image files. The text provided in the <img alt> attribute enables the site owner to provide relevant information to the search engine and to the end user. Alt text is helpful to end users if they have images disabled or if the image does not properly load. In addition, the Alt text is utilized by screen readers. Make sure that your Alt text is descriptive and accurately reflects what the image represents and supports the content on the page.


## reference
https://www.webmasterworld.com/forum25/3716.htm
http://www.ehcoo.com/seo.html
[百度站长平台关于SEO的建议](https://ziyuan.baidu.com/college/articleinfo?id=36)
[自动推送Hexo博客文章至百度](https://lemonxq.cn/2017/11/23/[%E8%87%AA%E5%88%B6%E5%B7%A5%E5%85%B7]%E5%AE%9E%E7%8E%B0%E8%87%AA%E5%8A%A8%E6%8E%A8%E9%80%81Hexo%E5%8D%9A%E5%AE%A2%E6%96%87%E7%AB%A0%E8%87%B3%E7%99%BE%E5%BA%A6/) 待看
[知乎是怎么把 SEO 做起来的？](https://www.zhihu.com/question/22726981)
- [https建议](http://www.chinaz.com/web/2015/1118/471868.shtml)
- [新站如何被百度快速收录](https://ziyuan.baidu.com/college/articleinfo?id=874)
## 待续


# 常见疑问

## http站点转为https后，对站点原本的评价权重得分是否有影响？  

无影响，后续会有正向收益，认为https更安全，在排序上会有倾斜。

## 转https后，需要做301跳转，在这个过程中，http已有的排名是否会有变动？快照是否有变动？301需要永久存在吗？  

快照和排名不会有变化，建议301永久存在，不管是对搜索引挚还是对用户来说都更好一些。

## 针对https的站点，百度在抓取技术层面上有哪些建议？

如果以前有http站点，建议永久保留跳转行为。之后注意通过百度站长平台的抓取诊断工具和抓取异常工具关注抓取结果。



## 百度索引量增加收录量反而下降是什么原因？

百度索引量是指被百度收集的数量，百度收录量是指被百度放出的数量
> 1. 索引量指可以被搜索用户搜索到的网站数据库，索引量工具同时支持站点自定义想要关注的目录，查看某一目录规则下的索引量；索引量不等于流量，索引量会有定期数据波动，属于正常现象。
> 2. 百度索引数据最快每天更新一次，最迟一周更新一次，不同站点的更新日期可能不同。
> 3. 您可以查询到近一年中每天的索引量数据，一年前的索引量数据为每月索引量数据。
> 4. 如果已有流量数据查询不到，请隔日再查，最长间隔一周可查询到数据。
> 来自百度 https://ziyuan.baidu.com

1. 百度索引是指你的网页已被百度蜘蛛爬取到百度索引库里了，但这不表示你的网页被百度收录了，所以你是检索不到的。
1. 百度收录是指，在百度索引库的网页经一定检查符合百度标准的，百度“转移到”（这个词是我自己说的，方便理解，实际百度未必这样处理）收录库里，予以放出，也就是被百度收录了这时你才能检索到自己的网页，但此时你的网页如果不符合标准仍然有从百度收录库被删的可能，比如文章是复制的重复率太高等等，百度检查也不是完美的。

索引增加说明，百度蜘蛛还会定期到你的网站爬取网页，所以你的索引会增加。
收录减少很可能是因为你的网页在百度的价值不够，又被百度收录删了。


## 为什么百度索引量和收录量一直不增加呢?

新站开始收录比较慢比较正常，当然有些新站收录也会比较好。
这个也是有一些偶性的，看下抓取频次和日志里面的蜘蛛爬行情况，都是正常即可。

## 提交链接后，都会被百度抓取并收录吗？
百度对已提交的数据，不保证一定会抓取及收录所有网址。是否收录与页面质量相关。

## 实例

电商比较重视排名，SEO一定要好


# 总结

麻蛋，百度不行啊。seo设置麻烦，收录又慢。google都不用设置，收录又新又好。
