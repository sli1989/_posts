
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

# 2. 域名解析 (xusong.vip --> xu-song.github.io)


## 2.1 配置DNS解析

进入你的[阿里云DNS解析](https://home.console.aliyun.com)，选择你想要解析的域名，点击后面的解析。如下图所示：
![dns](https://user-images.githubusercontent.com/13825126/35460092-a97a685a-031d-11e8-9cc6-1ce1b730a917.PNG)



### 记录类型
[参考](https://www.alibabacloud.com/help/zh/doc-detail/58077.htm)
```yml
A:      将域名指向一个IPV4地址  #
CNAME:  将域名指向另外一个域名  # 将域名指向另一个域名，再由另一个域名提供IP地址
AAAA:   将域名指向一个IPV6地址  # 当您希望访问者通过IPv6地址访问您的域名时，可以使用AAAA记录。
NS:     将子域名指向其他DNS服务器解析 # 如果需要把子域名交给其他DNS服务商解析，就需要添加NS记录。
MX:     将域名指向邮件服务器地址  # 如果需要设置邮箱，让邮箱能收到邮件，就需要添加MX记录。
SRV:    记录提供特定服务的服务器
显性URL: 将域名302重定向到另外一个地址
隐性URL: 与显性URL类似，但是会隐藏真实目标地址
...
```

> We recommend you change this to a CNAME record pointing at [YOUR USERNAME].github.io.
> -- <a href="https://help.github.com/articles/setting-up-a-custom-subdomain/">Github Help</a>

**Github建议采用CNAME记录，为什么？**

因为IP有可能会变动，导致A记录失效吗？不是，是因为所有Github Pages共用ip，Github后台是根据host定位www目录的。详见[Github Pages原理]()

**阿里云建议采用A记录**

因为A记录限制最少，最灵活，多条不会冲突


**优先级**
- 单独设置的域名解析优先级高于泛域名解析
- NS记录优先于A记录。即，如果一个主机地址同时存在NS记录和A记录，则A记录不生效。这里的NS记录只对子域名生效。
- A记录优先于CNAME记录。即如果一个主机地址同时存在A记录和CNAME记录，则CNAME记录不生效
- MX记录可以通过设置优先级实现主辅服务器设置，“优先级”中的数字越小表示级别越高。也可以使用相同优先级达到负载均衡的目的


### 主机记录
主机记录就是域名前缀，常见用法有：
```yml
www: 解析后的域名为www.aliyun.com。
@: 直接解析主域名 aliyun.com。
*: 泛解析，匹配其他所有域名 *.aliyun.com。
mail: 将域名解析为mail.aliyun.com，通常用于解析邮箱服务器。
二级域名: 如：abc.aliyun.com，填写abc。
手机网站: 如：m.aliyun.com，填写m。
显性URL: 不支持泛解析（泛解析：将所有子域名解析到同一地址）
```


1. @和WWW是两个主机名，可以指向不同的IP(A记录)或域名(CNAME记录)
1. 可以为一个主机添加多个A记录 (1. 实现[负载均衡](https://www.alibabacloud.com/help/zh/doc-detail/60182.htm)，2. 可配合解析路线进行[智能解析](https://www.alibabacloud.com/help/zh/doc-detail/58142.htm))
1. 一个主机配置了CNAME记录，就不能再为该主机配置其他任何记录 (为啥呢？) 见 [记录冲突判断规则](https://www.alibabacloud.com/help/zh/doc-detail/58456.htm)


 负载均衡的实现：负载均衡(Server Load Balancing，SLB)是指在一系列资源上面动态地分布网络负载。负载均衡可以减少网络拥塞，提高整体网络性能，提高自愈性， 并确保企业关键性应用的可用性。当相同子域名有多个目标地址时，表示轮循，可以达到负载均衡的目的，但需要虚拟主机服务商支持。

### 解析路线
如果多个IP，[搜索引擎线路](https://www.alibabacloud.com/help/zh/doc-detail/58147.htm)

如果只有一个IP地址或CNAME域名，请务必选择【默认】。
```yml
默认: 必填！未匹配到智能解析线路时，返回【默认】线路设置结果。
世界: 向除中国大陆以外的其他国家和地区，返回设置的记录值。 # 可用于双线部署，
搜索引擎: 向搜索引擎爬虫的DNS，返回设置的记录值。

```

### TTL

TTL不需要填写，添加时系统会自动生成，默认为600秒（TTL为缓存时间，数值越小，修改记录各地生效时间越快）。

## 2.2 查看解析是否生效

怎样查看解析是否生效？

### Windows 用户测试

修改域名解析，实际上是在域名解析服务商处修改域名解析记录。修改的解析记录是否在用户端生效，既受运营商递归 DNS 服务器的直接影响，也受域名解析服务商提供的权威 DNS 服务器的间接影响。

测试本地运营商递归 DNS 服务器是否生效
```sh
$ nslookup eson.org
服务器: ...  # 一般返回的是最近的DNS服务器，
Address: ...
```
<!--
服务器: crl-ns1.crl.ibm.com
Address: 9.186.88.5
-->

测试域名解析服务商的权威 DNS 服务器是否生效。测试方法如下:

```sh
$ nslookup eson.org dns25.hichina.com
```
### Linux测试
`dig 要检测的域名 @dns服务器地址`

```sh
$ dig eson.org
; <<>> DiG 9.9.5-3ubuntu0.17-Ubuntu <<>> eson.org
;; global options: +cmd
;; Got answer:  # 为什么0个answer？
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 8309
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;eson.org.                      IN      A

;; AUTHORITY SECTION:   # 不应该啊，我已经改回阿里的name server了
eson.org.               3592    IN      SOA     hugh.ns.cloudflare.com. dns.cloudflare.com. 2027227883 10000 2400 604800 3600

;; Query time: 112 msec
;; SERVER: 9.0.146.50#53(9.0.146.50)
;; WHEN: Sun Mar 11 18:04:06 CST 2018
;; MSG SIZE  rcvd: 99
```
以上部分是不是延迟问题，明天再试试。

(Update: 第二天测试，果然解析到了`xu-song.coding.me`.)


```sh
$ dig eson.org vip1.alidns.com
; <<>> DiG 9.9.5-3ubuntu0.17-Ubuntu <<>> eson.org vip1.alidns.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 23319
;; flags: qr rd ra; QUERY: 1, ANSWER: 15, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;eson.org.                      IN      A

;; ANSWER SECTION:  # 这个就对了。我采用的双线部署。国内走coding.net
eson.org.               600     IN      CNAME   xu-song.coding.me.
xu-song.coding.me.      60      IN      A       103.72.147.211
xu-song.coding.me.      60      IN      A       103.72.145.7
xu-song.coding.me.      60      IN      A       23.91.101.50
xu-song.coding.me.      60      IN      A       103.218.240.147
xu-song.coding.me.      60      IN      A       36.255.221.66
xu-song.coding.me.      60      IN      A       107.150.121.91
xu-song.coding.me.      60      IN      A       107.150.121.231
xu-song.coding.me.      60      IN      A       103.72.147.89
xu-song.coding.me.      60      IN      A       103.14.35.185
xu-song.coding.me.      60      IN      A       103.72.146.177
xu-song.coding.me.      60      IN      A       36.255.220.102
xu-song.coding.me.      60      IN      A       23.91.96.142
xu-song.coding.me.      60      IN      A       23.91.97.251
xu-song.coding.me.      60      IN      A       103.218.241.74

;; Query time: 682 msec
;; SERVER: 9.0.146.50#53(9.0.146.50)
;; WHEN: Sun Mar 11 18:05:55 CST 2018
;; MSG SIZE  rcvd: 292

;; Got answer:  # 为什么又有一个query & answer？
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 52301
;; flags: qr rd ra; QUERY: 1, ANSWER: 9, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;vip1.alidns.com.               IN      A

;; ANSWER SECTION:   # 这是什么鬼？
vip1.alidns.com.        600     IN      A       14.1.112.11
vip1.alidns.com.        600     IN      A       140.205.29.113
vip1.alidns.com.        600     IN      A       106.11.30.113
vip1.alidns.com.        600     IN      A       116.211.173.151
vip1.alidns.com.        600     IN      A       106.11.41.151
vip1.alidns.com.        600     IN      A       140.205.1.1
vip1.alidns.com.        600     IN      A       121.29.51.151
vip1.alidns.com.        600     IN      A       140.205.228.51
vip1.alidns.com.        600     IN      A       47.88.44.151

;; Query time: 389 msec
;; SERVER: 9.0.146.50#53(9.0.146.50)
;; WHEN: Sun Mar 11 18:05:56 CST 2018
;; MSG SIZE  rcvd: 188
```
以上命令，第二天竟然变回了cloudflare的name server。why？
```
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1
...
AUTHORITY SECTION:
eson.org.               3600    IN      SOA     hugh.ns.cloudflare.com. dns.cloudflare.com.
```

```sh
$ dig eson.org dns25.hichina.com
; <<>> DiG 9.9.5-3ubuntu0.17-Ubuntu <<>> eson.org dns25.hichina.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 18683
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;eson.org.                      IN      A

;; AUTHORITY SECTION:   # 这个也有延迟啊。什么情况？dns25.hichina.com与vip1.alidns.com什么区别？是不是有个根节点?
eson.org.               3404    IN      SOA     hugh.ns.cloudflare.com. dns.cloudflare.com. 2027227883 10000 2400 604800 3600

;; Query time: 115 msec
;; SERVER: 9.0.146.50#53(9.0.146.50)
;; WHEN: Sun Mar 11 18:07:14 CST 2018
;; MSG SIZE  rcvd: 99

;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 31080
;; flags: qr rd ra; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;dns25.hichina.com.             IN      A

;; ANSWER SECTION:
dns25.hichina.com.      496     IN      A       106.11.211.69
dns25.hichina.com.      496     IN      A       106.11.211.59
dns25.hichina.com.      496     IN      A       106.11.141.129
dns25.hichina.com.      496     IN      A       106.11.141.119
dns25.hichina.com.      496     IN      A       140.205.41.29
dns25.hichina.com.      496     IN      A       140.205.41.19
dns25.hichina.com.      496     IN      A       140.205.81.29
dns25.hichina.com.      496     IN      A       140.205.81.19

;; Query time: 114 msec
;; SERVER: 9.0.146.50#53(9.0.146.50)
;; WHEN: Sun Mar 11 18:07:14 CST 2018
;; MSG SIZE  rcvd: 174
```
以上这个部分，第二天测试竟然不变。为什么会采用cloudflare的DNS服务器呢？


### 测试结果分析

如果递归 DNS 服务器和权威 DNS 服务器都未生效，表明域名确实没有添加成功。

如果递归 DNS 服务器未生效，权威 DNS 服务器已生效，表明域名刚添加不久，全球的递归 DNS 服务器未完全同步，需要等待域名配置的 `TTL 时间后再次检测`是否生效。如果某些个别的运营商递归 DNS 服务器依然未生效，很可能是你遇到了域名劫持或者 DNS 缓存投毒事件。

参考: https://www.alibabacloud.com/help/zh/doc-detail/58458.html

### 2.3 修改过 DNS 服务器，多长时间解析可以生效？
[ 多长时间解析可以生效](https://www.alibabacloud.com/help/zh/doc-detail/58458.htm)
要全球解析生效，得等上一会了，也可以先ping一下自己的设置对不对。阿里云域名服务的工作原理是，在你更新了域名解析之后，首先是阿里的万网云解析，然后传播到各大运营商的DNS服务器，刷新DNS缓存，至此你的域名可以被访问。



# 3. 重定向(xu-song.github.io --> xusong.vip)

## 配置github pages的custom domain

进入你的github pages的仓库，然后在设置里面将的你的域名的地址，添加到custom domain中，然后保存即可。如下图所示：

![default](https://user-images.githubusercontent.com/13825126/35460275-62ca64a4-031e-11e8-8e43-b15c8b2e1bcc.PNG)



这里是对github.io做了重定向，会重定向到所配置的站点。也可以随便填写一个站点，比如www.baidu.com，也会重定向过去

### 重新deploy，你会发现github page的domain设置又被改回去了，肿么办？

在source目录下新建CNAME文件，内容是`xusong.vip`。这样每次deploy会自动完成`步骤3`。




## 5. 疑点重重
- [x] 为什么还要再github仓库中设置？dns解析不是已经做了重定向了吗。指向ip:80端口还不够吗？
- [x] 每个账号的gitpage都是独立的IP吗？github怎么这么多独立外网IP？还是不同账号共用IP？
- [x] 不同github page共享ip 正因为如此，才需要`步骤3`的设置。
- [x]  配置github pages的custom domain，其作用仅仅是`xu-song.github.io --> xusong.vip (重定向)`吗？

[ss](./github pages原理.md)
