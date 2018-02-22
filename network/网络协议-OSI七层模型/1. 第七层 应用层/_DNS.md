



## 概念


- 域名系统（DNS）是一种用于 TCP/IP应用程序的分布式数据库，它提供主机名字和IP地址之间的转换及有关电子邮件的选路信息。

- DNS Server
- 名字解析器
- 名字服务器a
- Nameserver:
Nameserver is a server on the internet specialized in handling queries regarding the location of a domain name’s various services. Nameservers are a fundamental part of the Domain Name System (DNS).

- 地址解析器 resolver
在 Unix主机中，该解析器主要是通过两个库函数gethostbyname和来访问
的，它们在编译应用程序时与应用程序连接在一起。

- 网络信息中心NIC。负责分配顶级域和委派其他指定地区域的唯一授权机构。 -- TCPIP详解

- ISP

- 本地域名服务器
- 根域名服务器
- 顶级域名服务器
- 下级的域名服务器
- 转发域名服务器


### 概念疑问

BasicDNS and Web Hosting DNS 区别？

BasicDNS includes the nameservers which are provided by default during domain registration while Web Hosting DNS is the set of nameservers which comes along with the corresponding shared hosting package purchased at Namecheap.

DNS除了nameserver之外，还包含什么？



## 解析过程


DNS地址解析器的核心功能能
- gethostbyname  主机名-->ip   
- gethostbyaddr  ip--主机名


### gethostbyname  主机名-->ip   

DNS服务器在名称解析过程中正确的查询顺序为:<br>
本地缓存记录→区域记录→根域名服务器→转发域名服务器

具体步骤如下：
1. 客户机提交域名解析请求，并将该请求发送给`本地域名服务器`。
1. 当本地的域名服务器收到请求后，就先查询`本地缓存`。如果有查询的DNS信息记录，则直接返回查询的结果。如果没有该记录，本地域名服务器就把请求发给`根域名服务器`。
1. `根域名服务器`再返回给本地域名服务器一个所查询域的`顶级域名服务器`的地址。
1. 本地服务器再向返回的域名服务器发送请求。
1. 接收到该查询请求的域名服务器查询其缓存和记录，如果有相关信息则返回`本地域名服务器`查询结果，否则通知本地域名服务器`下级的域名服务器`的地址。
1. 本地域名服务器将查询请求发送给`下级的域名服务器`的地址，直到获取查询结果。
1. 本地域名服务器将返回的结果保存到缓存，并且将结果返回给客户机，完成解析过程。




通常情况下，我们是先设定DNS解析规则，然后ISP(供应商)依据指定的解析规则进行DNS解析。同样，我们通过测试解析结果，也可以反推DNS解析规则。本文以百度首页为例，分析其DNS解析规则。





## 其他



什么是智能解析？

云解析DNS支持多线智能解析，即根据网站`访问者的IP`，智能判断给用户提供`最佳的访问解析地址`，使访问用户获得最快捷、最流畅的体验。例如当判断访问者来源为中国联通用户，那云解析DNS就将域名解析到中国联通的服务器IP上；当判断访问者来源为中国电信用户，那云解析DNS就将域名解析到中国电信的服务器IP上。


归结就是，一个域名，配了多条A记录。





## 原理

> 解析器主要是通过两个库函数 gethostbyname 和gethostbyaddr来访问的，它们在编译应用程序时与应用程序连接在一起。

- gethostbyname  主机名-->ip   
- gethostbyaddr  ip--主机名

主机名和ip是多对多关系。多个主机名可指向同一IP(别名，多个入口)，一个主机名也可指向多个IP(可用于多线智能解析和负载均衡)。




## 疑问



##
