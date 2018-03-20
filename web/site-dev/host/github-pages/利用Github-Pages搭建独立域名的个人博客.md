---
title: 利用Github Pages搭建独立域名的个人博客
date: 2018-01-26 03:08:53
keywords: ["建站","domain","blog","pages","域名"]
tags: ["建站","domain","blog","DNS","pages","github"]
categories:
- web
- host
---


# 1. 购买域名

[阿里云-万网](https://wanwang.aliyun.com/) 或其他供应商

[了解更多域名]()

# 2. 域名解析 (xusong.vip --> xu-song.github.io)

域名注册完成后首先需要做域名解析，域名解析就是把域名指向网站所在服务器的IP，让人们通过注册的域名可以访问到网站。

## 2.1 配置DNS解析

进入你的[阿里云DNS解析](https://home.console.aliyun.com)，选择你想要解析的域名，点击后面的解析。如下图所示：
![dns](https://user-images.githubusercontent.com/13825126/35460092-a97a685a-031d-11e8-9cc6-1ce1b730a917.PNG)


> We recommend you change this to a CNAME record pointing at [YOUR USERNAME].github.io.
> -- <a href="https://help.github.com/articles/setting-up-a-custom-subdomain/">Github Help</a>

**Github建议采用CNAME记录，为什么？**

因为IP有可能会变动，导致A记录失效吗？不是，是因为所有Github Pages共用ip，Github后台是根据host定位www目录的。详见[Github Pages原理]()

**阿里云建议采用A记录**

因为A记录限制最少，最灵活，多条不会冲突

参考
[DNS解析-解析记录](/2018/01/26/web/site-dev/host/github-pages/%E5%88%A9%E7%94%A8Github-Pages%E6%90%AD%E5%BB%BA%E7%8B%AC%E7%AB%8B%E5%9F%9F%E5%90%8D%E7%9A%84%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/)

# 3. 重定向(xu-song.github.io --> xusong.vip)

## 3.1 配置github pages的custom domain

进入你的github pages的仓库，然后在设置里面将的你的域名的地址，添加到custom domain中，然后保存即可。如下图所示：

![default](https://user-images.githubusercontent.com/13825126/35460275-62ca64a4-031e-11e8-8e43-b15c8b2e1bcc.PNG)



这里是对github.io做了重定向，会重定向到所配置的站点。也可以随便填写一个站点，比如www.baidu.com，也会重定向过去

细心的同学会发现，配置custom domain后github仓库的根目录多了一个`CNAME`文件，里面正式刚刚配置的域名地址。

### 3.2 重新deploy，你会发现github page的domain设置又被改回去了，肿么办？

原因是，hexo deploy时会采用`git push --force`。如果deploy版本没有`CNAME`文件，则会强制删除3.1中添加的CNAME文件，导致custom domain失效。

因此，最佳的方式是我们手动添加CNAME文件来设置domain。在source目录下新建CNAME文件，内容是`xusong.vip`。这样每次deploy会自动完成`步骤3.1`。




## 5. 疑点重重
- [x] 为什么还要再github仓库中设置？dns解析不是已经做了重定向了吗。指向ip:80端口还不够吗？
- [x] 每个账号的gitpage都是独立的IP吗？github怎么这么多独立外网IP？还是不同账号共用IP？
- [x] 不同github page共享ip 正因为如此，才需要`步骤3`的设置。
- [x]  配置github pages的custom domain，其作用仅仅是`xu-song.github.io --> xusong.vip (重定向)`吗？

[ss](./github pages原理.md)
