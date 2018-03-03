---
title: Coding Pages托管静态博客-原理浅析
date: 2018-03-02
keywords: ["github","pages","pages服务","blog","博客","静态网页","网页托管","免费","自定义域名","Jekyll"]
tags: ["git","blog"]
categories:
- web
- host
---







> github page不支持多个域名，因此不存在重定向





## coding page跳转至首页


首选域名，一次到达

```sh
$ wget https://blog.eson.org
# 这个不需要重定向
--2018-03-02 18:51:26--  https://blog.eson.org/
Resolving blog.eson.org (blog.eson.org)... 107.150.121.91, 107.150.121.231, 103.72.147.89, ...
Connecting to blog.eson.org (blog.eson.org)|107.150.121.91|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 72536 (71K) [text/html]
Saving to: ‘index.html.1’


```
跳转的域名，采用301跳转

```sh
$ wget xusong.vip
--2018-03-02 17:35:28--  http://xusong.vip/
# dns解析，CNAME记录：xusong.vip --> xu-song.coding.me
# 即域名xu-song.coding.me对应的服务器。
# 返回301跳转到 http://blog.eson.org/
Resolving xusong.vip (xusong.vip)... 103.72.145.7, 23.91.101.50, 103.218.240.147, ...
Connecting to xusong.vip (xusong.vip)|103.72.145.7|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: http://blog.eson.org/ [following]
# dns解析
--2018-03-02 17:35:29--  http://blog.eson.org/
Resolving blog.eson.org (blog.eson.org)... 103.72.147.211, 103.72.145.7, 23.91.101.50, ...
Reusing existing connection to xusong.vip:80.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://blog.eson.org/ [following]
#
--2018-03-02 17:35:31--  https://blog.eson.org/
Connecting to blog.eson.org (blog.eson.org)|103.72.147.211|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 72536 (71K) [text/html]
Saving to: ‘index.html’


```


```sh
$ wget blog.eson.org
# 默认是访问 http://blog.eson.org，返回301重定向 https://blog.eson.org/
--2018-03-02 18:50:27--  http://blog.eson.org/
Resolving blog.eson.org (blog.eson.org)... 36.255.221.66, 107.150.121.91, 107.150.121.231, ...
Connecting to blog.eson.org (blog.eson.org)|36.255.221.66|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://blog.eson.org/ [following]
#
--2018-03-02 18:50:28--  https://blog.eson.org/
Connecting to blog.eson.org (blog.eson.org)|36.255.221.66|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 72536 (71K) [text/html]
Saving to: ‘index.html’


```



要跳转2次，一次302，一次301
```sh
$ wget xu-song.coding.me
#
--2018-03-02 18:58:45--  http://xu-song.coding.me/
Resolving xu-song.coding.me (xu-song.coding.me)... 23.91.97.251, 103.218.241.74, 103.72.147.211, ...
Connecting to xu-song.coding.me (xu-song.coding.me)|23.91.97.251|:80... connected.
HTTP request sent, awaiting response... 302 Found
Location: http://blog.eson.org/ [following]
#
--2018-03-02 18:58:46--  http://blog.eson.org/
Resolving blog.eson.org (blog.eson.org)... 103.72.147.211, 103.72.145.7, 23.91.101.50, ...
Reusing existing connection to xu-song.coding.me:80.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://blog.eson.org/ [following]
#
--2018-03-02 18:58:46--  https://blog.eson.org/
Connecting to blog.eson.org (blog.eson.org)|103.72.147.211|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 72536 (71K) [text/html]
Saving to: ‘index.html.3’


```

## 301，302 区别

### 对于用户
301，302对用户来说没有区别，他们看到效果只是一个跳转，浏览器中旧的URL变成了新的URL。页面跳到了这个新的url指向的地方。


### 对于引擎及站长

#### 302 redirect: 302 代表暂时性转移(Temporarily Moved ) 临时跳转

302转向可能会有URL规范化及网址劫持的问题。可能被搜索引擎判为可疑转向，甚至认为是作弊。

302重定向和网址劫持（URL hijacking）有什么关系呢？这要从搜索引擎如何处理302转向说起。从定义来说，从网址A做一个302重定向到网址B时，主机服务器的隐含意思是网址A随时有可能改主意，重新显示本身的内容或转向其他的地方。大部分的搜索引擎在大部分情况下，当收到302重定向时，一般只要去抓取目标网址就可以了，也就是说网址B。

实际上如果搜索引擎在遇到302转向时，百分之百的都抓取目标网址B的话，就不用担心网址URL劫持了。问题就在于，有的时候搜索引擎，尤其是Google，并不能总是抓取目标网址。为什么呢？比如说，有的时候A网址很短，但是它做了一个302重定向到B网址，而B网址是一个很长的乱七八糟的URL网址，甚至还有可能包含一些问号之类的参数。很自然的，A网址更加用户友好，而B网址既难看，又不用户友好。这时Google很有可能会仍然显示网址A。

由于搜索引擎排名算法只是程序而不是人，在遇到302重定向的时候，并不能像人一样的去准确判定哪一个网址更适当，这就造成了网址URL劫持的可能性。也就是说，一个不道德的人在他自己的网址A做一个302重定向到你的网址B，出于某种原因， Google搜索结果所显示的仍然是网址A，但是所用的网页内容却是你的网址B上的内容，这种情况就叫做网址URL劫持。你辛辛苦苦所写的内容就这样被别人偷走了。


DNS解析有一条 显性URL-将域名302重定向到另外一个地址。

#### 301 redirect: 301 代表永久性转移(Permanently Moved)，

当网页A用301重定向转到网页B时，搜索引擎可以肯定网页A永久的改变位置，或者说实际上不存在了，搜索引擎就会把网页B当作唯一有效目标。
301的好处是:

- 第一， 没有网址规范化问题。
- 第二， 也很重要的，网页A的PR网页级别会传到网页B。


变更网站域名建议直接做301重定向，UEL跳转不利于SEO蜘蛛本身不喜欢，运气不好还会被判作弊
当网页A用301重定向到网页B时，搜索引擎可以肯定网页A永久的改变位置，或者说实际上不存在了，搜索引擎就会把网页B当作唯一有效目标。
好处是，第一没有网址规划问题；第二，网页A的PR网页级别会传到网页B。


## 大家常用的301 302

### 301
t.cn
知乎跳转
dns解析跳转
coding page跳转主页


## 如何实现转发

- DNS可配置 302转发
- apache / nginx 配置文件中写转发规则，rewrite xxx yyy 301
- 写一个 index.html 文件，里面写 meta refresh 跳转规则
