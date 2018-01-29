---
title: 为Github Pages设置独立域名
date: 2018-01-26 03:08:53
tags: git
categories: ["git","github","domain","dns"]
---

#

## 1. 购买域名

[阿里云-万网](https://wanwang.aliyun.com/) 或其他供应商

## 2. 域名解析 (xusong.vip --> xu-song.github.io)
**配置DNS解析**

进入你的[阿里云DNS解析](https://dc.console.aliyun.com/dns/)，选择你想要解析的域名，点击后面的解析。如下图所示：
![dns](https://user-images.githubusercontent.com/13825126/35460092-a97a685a-031d-11e8-9cc6-1ce1b730a917.PNG)



**[记录类型](https://www.alibabacloud.com/help/zh/doc-detail/58077.htm)**
```
A     - 将域名指向一个IPV4地址
CNAME - 将域名指向另外一个域名
...

```
> (1) github建议采用[CNAME记录](https://help.github.com/articles/setting-up-a-custom-subdomain/) (因为IP有可能会变动)
We recommend you change this to a CNAME record pointing at [YOUR USERNAME].github.io.
(2) 阿里云建议采用A记录(因为A记录限制最少，最灵活)



**主机记录**
```
主机记录就是域名前缀，常见用法有：

www：解析后的域名为www.aliyun.com。
@：直接解析主域名 aliyun.com。
*：泛解析，匹配其他所有域名 *.aliyun.com。
mail：将域名解析为mail.aliyun.com，通常用于解析邮箱服务器。
二级域名：如：abc.aliyun.com，填写abc。
手机网站：如：m.aliyun.com，填写m。
显性URL：不支持泛解析（泛解析：将所有子域名解析到同一地址）
```

> 注意
(1) @和WWW是两个主机名，可以指向不同的IP(A记录)或域名(CNAME记录)
(2) 可以为一个主机添加多个A记录 (1. 实现[负载均衡](https://www.alibabacloud.com/help/zh/doc-detail/60182.htm)，2. 可配合解析路线进行[智能解析](https://www.alibabacloud.com/help/zh/doc-detail/58142.htm))
(3) 一个主机配置了CNAME记录，就不能再为该主机配置其他任何记录 (为啥呢？)
(4) [记录冲突判断规则](https://www.alibabacloud.com/help/zh/doc-detail/58456.htm)

**解析路线**
如果多个IP，[搜索引擎线路](https://www.alibabacloud.com/help/zh/doc-detail/58147.htm)
```
如果只有一个IP地址或CNAME域名，请务必选择【默认】。

默认：必填！未匹配到智能解析线路时，返回【默认】线路设置结果。
世界：向除中国大陆以外的其他国家和地区，返回设置的记录值。
搜索引擎：向搜索引擎爬虫的DNS，返回设置的记录值。

```


**等待**
[ 多长时间解析可以生效](https://www.alibabacloud.com/help/zh/doc-detail/58458.htm)
要全球解析生效，得等上一会了，也可以先ping一下自己的设置对不对。阿里云域名服务的工作原理是，在你更新了域名解析之后，首先是阿里的万网云解析，然后传播到各大运营商的DNS服务器，刷新DNS缓存，至此你的域名可以被访问。



## 3. 重定向(xu-song.github.io --> xusong.vip)

### 配置github pages的custom domain

进入你的github pages的仓库，然后在设置里面将的你的域名的地址，添加到custom domain中，然后保存即可。如下图所示：

![default](https://user-images.githubusercontent.com/13825126/35460275-62ca64a4-031e-11e8-8e43-b15c8b2e1bcc.PNG)



这里是对github.io做了重定向，会重定向到所配置的站点。也可以随便填写一个站点，比如www.baidu.com，也会重定向过去




## 4. 疑问  & TODO list
- [ ] demo with deeplearning4j. 模型文件太大，就找个后台吧。参考stanford nlp的demo，等
- [ ] SEO
- [ ] 每个账号的gitpage都是独立的IP吗？github怎么这么多独立外网IP？还是不同账号共用IP？
- [ ]  配置github pages的custom domain。作用不仅仅是`xu-song.github.io --> xu-song.top (重定向)`，貌似对步骤2也起作用
- [x] 重新`hexo deploy`的时候，步骤3的设置又会自动改回去。肿么办？
  - 在source目录下新建CNAME文件，内容是`xu-song.top`。这样每次deploy会自动完成`步骤3`
- [ ] 如何解决md同步问题？
  - git-repo源，gist源，git issue源，gitpage源。最优的方式就是同源 + 自动deploy。
  - 方式一：以issue作源，要自己利用github api，读取issue，然后写到source目录(貌似也挺简单)。
  - 方式二：以git-repo作源，貌似不错哎。单独把source目录单独作为repo
  - 方式三：以gist作源：易集成(一行js即可)，但不易管理(不支持directory，文档多了很麻烦)
- [ ] 如何实现在线写blog，像wordpress那样
  - 用js调用github api，或者其他后台api即可
  - 后台
- [ ] 如何实现private space。密码登录
  - 都放前端，
## 5. reference
- [github pages+阿里云域名绑定搭建个人博客](https://github.com/HuYuee/blog/issues/13)
