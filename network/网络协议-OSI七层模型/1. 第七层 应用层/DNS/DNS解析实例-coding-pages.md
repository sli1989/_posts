---
title: DNS解析实例之 Coding Pages
keywords:
  - dns
  - 解析
  - coding.net
  - pages
tags:
  - network
  - dns
categories:
  - network
  - dns
abbrlink: 2902c89e
date: 2018-03-06 00:00:00
---






## coding page跳转至首页

DNS配置
<img src="/images/raw/建站 - DNS解析 - 配置.png"></img>

coding.net域名配置
<img src="/images/raw/建站 - Coding Pages - 域名配置.png"></img>


`首选`域名，一次到达

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
`跳转至首页`的域名，采用301跳转

```sh
$ wget xusong.vip
--2018-03-02 17:35:28--  http://xusong.vip/
# dns解析xusong.vip，根据CNAME记录得到xu-song.coding.me。
# 然后解析xu-song.coding.me对应的服务器IP。
# 返回“301跳转到 http://blog.eson.org/”
Resolving xusong.vip (xusong.vip)... 103.72.145.7, 23.91.101.50, 103.218.240.147, ...
Connecting to xusong.vip (xusong.vip)|103.72.145.7|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: http://blog.eson.org/ [following]
# DNS解析http站点，返回“301跳转至https页面”
--2018-03-02 17:35:29--  http://blog.eson.org/
Resolving blog.eson.org (blog.eson.org)... 103.72.147.211, 103.72.145.7, 23.91.101.50, ...
Reusing existing connection to xusong.vip:80.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://blog.eson.org/ [following]
# DNS解析https站点，返回页面内容
--2018-03-02 17:35:31--  https://blog.eson.org/
Connecting to blog.eson.org (blog.eson.org)|103.72.147.211|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 72536 (71K) [text/html]
Saving to: ‘index.html’


```

不加https协议，会首先301跳转到https站点。

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


直接访问coding pages页面，要跳转2次，一次302，一次301
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
