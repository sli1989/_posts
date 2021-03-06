---
title: Github Pages托管静态博客-原理浅析
keywords:
  - github
  - pages
  - pages服务
  - blog
  - 博客
  - 静态网页
  - 网页托管
  - 免费
  - 自定义域名
  - Jekyll
tags:
  - github
  - pages
  - blog
categories:
  - web
  - site-dev
  - host
  - github-pages
abbrlink: bfc2ae40
date: 2018-01-26 00:00:00
---
## 关于github提供的http server

#### ping 几个不同账号的gitpage(比如`colah.github.io`,`xu-song.github.io`)，发现对应的是同一个ip。为什么返回的页面不同呢？

github pages 的 CNAME 是绑定 pages.github.io，不是${username}.github.io

coding.net 的 CNAME 是绑定 pages.coding.me 

显然，Github肯定在后台做了处理。即github自身会维护一个映射，`host_name --> www_path`，这样就可以根据不同的host信息返回不同的html了。

这样，在访问`xu-song.github.io`时github就找到了该返回的html。


## 关于custom domain
现在我们改用`custom domain`的方式访问gitpage主页。假设已经配置好了dns的A记录映射。
访问`xusong.vip`，dns解析得到ip地址。然而这次github服务器得到的host是`xusong.vip`。懵逼了，github不认识`xusong.vip`(host数据里没有该记录)，返回404页面

<image src="https://user-images.githubusercontent.com/13825126/35623051-fc61df6c-06c4-11e8-89a7-6207bc430d85.PNG" style="width: 60%;">


**怎么办呢？**

那就让github认识一下`xusong.vip`，也就是在github page里设置一下custom domain，或者添加CNAME文件，详见[用Github Pages搭建独立域名的个人博客](../利用Github Pages搭建独立域名的个人博客/)


- [ ] 如果DNS设置CNAME记录，是不是github page不用设置就能work？

## 那么上一篇中的重重疑点也就解开了

- [x] 每个账号的gitpage都是独立的IP吗？github怎么这么多独立外网IP？还是不同账号共用IP？
  - 很多账号是同一个ip。
- [x] 不同github page共享ip 正因为如此，才需要`步骤3`的设置。
- [x]  配置github pages的custom domain，其作用仅仅是`xu-song.github.io --> xusong.vip (重定向)`吗？
  - 不是。1. 查dns解析是否通过 2. 部署到github服务器的相应目录（因为） 3. github page到domain的重定向


## 关于https

### 为什么Github Pages不支持为自定义域名添加SSL证书？

https://steffan.cn/2017/03/22/use-cloudflare-to-implement-HTTPS-for-GithubPages-with-custom-domain-names/



## 多个域名能否指向同一个 GitHub Pages？

GitHub Pages 的官方文档，一个 username.github.io 只能支持一个域名。

coding page支持多个域名。

## 一个账号能否见多个github page？

可以建立多个， 个人账户page只能有一个， 项目page可以有多个

比如你的账号名为  username, 项目叫 project1    那你可以通过  username.github.io/project1 访问， 如果配置了个人域名就可以用自己的域名访问了

但是CNAME不能指向username.github.io/project1，怎么办？


## todo
- [ ] 如何解决md同步问题？
  - git-repo源，gist源，git issue源，gitpage源。最优的方式就是同源 + 自动deploy。
  - 方式一：以issue作源，要自己利用github api，读取issue，然后写到source目录(貌似也挺简单)。
  - 方式二：以git-repo作源，貌似不错哎。单独把source目录单独作为repo
  - 方式三：以gist作源：易集成(一行js即可)，但不易管理(不支持directory，文档多了很麻烦)
- [ ] 如何实现在线写blog，像wordpress那样
  - 用js调用github api，或者其他后台api即可
