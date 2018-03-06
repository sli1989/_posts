---
title: 反演 百度DNS解析规则
date: 2018-02-09
tags: ["network","dns"]
categories:
- network
- dns
---

<!--
反函数：inverse function (or anti-function[1]) is a function that "reverses" another function
反编译：

DNS解析：host--ip，，DNS的逆应该是ip--host.
ARP（地址解析协议） RARP（逆地址解析协议），DNS中是不是也有逆？

正向 ：DNS解析规则 -- 解析结果。逆向：解析结果--解析规则
-->

## Overview
域名系统（DNS）是一种用于 TCP/IP应用程序的分布式数据库，它提供主机名字和IP地址之间的转换及有关电子邮件的选路信息。

通常情况下，我们是先设定DNS解析规则，然后ISP(供应商)依据指定的解析规则进行DNS解析。同样，我们通过测试解析结果，也可以反推DNS解析规则。本文以百度首页为例，分析其DNS解析规则。

DNS地址解析器的核心功能能
- gethostbyname  主机名-->ip   
- gethostbyaddr  ip--主机名

**分析方式一：**
通过抓包，分析DNS查询和响应报文。每个响应报文对应一条DNS解析规则，通过一条或者多条记录才能完成DNS解析。

**分析方式二：**
一堆命令，见参考博客。



## 百度DNS解析规则

| 编号 | 记录类型 | 主机记录         | 解析线路(isp) | 记录值                       | TTL值(不定) | 备注                                  |
|------|----------|------------------|---------------|-------------------|-------|----------------------|
| 1    | CNAME    | www.baidu.com    | --            | www.a.shifen.com  | 268   |                     |
| 2    | A        | www.a.shifen.com | 新加坡 百度   | 45.113.192.101     | 160   | 见解析方式一  |
| 3    | A        | www.a.shifen.com | 北京电信      | 220.181.111.188    | 160   |                 |
| 4    | A        | www.a.shifen.com | 其他          |                   |       |                                       |
|      |          |                  |               |                   |       |                                       |
| 5    | CNAME    | www.a.shifen.com | --            | www.wshifen.com   | 271   |   见解析方式三                     |
| 6    | NS       | wshifen.com      | --            | ns1.wshifen.com   | 163   |                        |
| 7    | AAAA     | www.baidu.com    |               |                   |       | 百度没有AAAA记录吧？                  |
|      |          |                  |               |                   |       |                                       |
| 8    | A        | baidu.com        | 北京移动      | 111.13.101.208     |       |     见解析方式二                 |
| 9    | A        | baidu.com        | 北京联通...   | 123.125.114.144    |       |                                       |
| 10   | NS       | baidu.com        | --            | dns.baidu.com     | 900   | 见解析方式四                       |
|      |          |                  |               |                   |       |                                       |
| 11   | NS       | a.shifen.com     | --            | ns1.a.shifen.com   | 397   | 见解析方式五                       |

> 注：表中所有数据均来自作者抓包实测，所有解析路线由ip.cn提供。

解析方式一: 1-->2 （www.baidu.com，查询类型A，即查询IPv4地址）
```bash
# 一会功夫变成102了
# DNS响应一般为多个ip，后续连接只用一个ip
$ ping www.baidu.com
PING www.wshifen.com (45.113.192.102) 56(84) bytes of data.
64 bytes from 45.113.192.102: icmp_seq=1 ttl=43 time=87.3 ms
```

解析方式二：8  （baidu.com，查询类型A）

```bash
# 这种域名一般情况下是不能做cname解析的，只能用A记录
$ ping baidu.com
PING baidu.com (111.13.101.208) 56(84) bytes of data.
64 bytes from 111.13.101.208: icmp_seq=1 ttl=45 time=13.8 ms
```

解析方式三: 1-->5-->6  （www.baidu.com，查询类型AAAA，即查询IPv6地址）
```yml
# 为什么走这个路线？
# 目前使用IPv6的还是极少数，所以得不到AAAA记录的。
# DNS响应报文中的资源记录部分：回答字段、授权字段和附加信息字段，均采用一种称为资源记录RR（ Resource Record）的相同格式。
#
Domain Name System (response)
    Questions: 1
    Answer RRs: 2
    Authority RRs: 1
    Additional RRs: 0
    Queries
        www.baidu.com: type AAAA, class IN
    Answers # 回答字段
        www.baidu.com: type CNAME, class IN, cname www.a.shifen.com
            Name: www.baidu.com
            Type: CNAME (Canonical NAME for an alias) (5)
            CNAME: www.a.shifen.com
        www.a.shifen.com: type CNAME, class IN, cname www.wshifen.com
            Name: www.a.shifen.com
            Type: CNAME (Canonical NAME for an alias) (5)
            Class: IN (0x0001)
            Time to live: 271
            Data length: 14
            CNAME: www.wshifen.com
    Authoritative nameservers  # 授权字段
        wshifen.com: type SOA, class IN, mname ns1.wshifen.com
            Name: wshifen.com
            Type: SOA (Start Of a zone of Authority) (6)
            Primary name server: ns1.wshifen.com baidu_dns_master.baidu.com


```

解析方式四：10  （baidu.com，查询类型AAAA）
```bash

Domain Name System (response)
    Questions: 1
    Answer RRs: 0
    Authority RRs: 1
    Queries
        baidu.com: type AAAA, class IN
    Authoritative nameservers
        baidu.com: type SOA, class IN, mname dns.baidu.com
            Name: baidu.com
            Type: SOA (Start Of a zone of Authority) (6)
            Primary name server: dns.baidu.com


```

解析方式五: 11  （www.a.shifen.com，查询类型AAAA）
```

```

## 疑问 & 剖析

### 编号1中，别名www.a.shifen.com的作用

觉得没啥用啊。看看网上的说法：

- 使用CNAME有个好处就是，我IP地址去做改动的时候不需要去DNS运营商上面做改动，只需要自己的服务器做改动就好，方便自己的域名与实际IP地址做对应。    --觉得没什么道理啊


- 百度弄的一个域名保护壳。？
- CDN加速节点？

逆向思维吧。如果没什么用，为什么要保留呢？是不是还有点作用？

### 编号2,3中，多条A记录的作用

- 可用于多线智能解析，为了每条线路（电信、联通/网通、移动等）上的用户都能最快访问站点
- 可用于简单的[负载均衡](https://cloud.tencent.com/document/product/302/9069)(dns轮询)
- 可HA(高可用)


### 关于返回主机(IP)的策略

考虑的因素有：
- [智能解析线路](https://cloud.tencent.com/document/product/302/8643) 用户所在网络的网络运行商类型、区域
- 距离--跳数

当我一个IP到DNS上面请求DNS域名解析的时候，DNS系统会根据你的IP地址所到达的域名对应的IP地址中路由跳数最小的那个IP地址作为访问的IP地址，具体你可以用LINUX的NSLOOKUP来查看域名所对应的IP地址，然后用PC的TRACERT的功能把所有DNS解析出来的IP地址进行跳数记录，然后在访问该域名，查看具体是哪个地址解析给你的PC。



### 为什么无法直接访问www.a.shifen.com

<image src="/image/raw/HTTP%20-%20Wireshark%20-%20www.a.shifen.com.png">

流程：
- [x] [1,2,3,4] - DNS解析
- [x] [5,6,7] - 三次握手，建立TCP连接
- [x] [8] - 发送HTTP Get请求
- [ ] [9] - 服务器返回RST复位信号，强制关闭TCP连接

服务器成功收到了HTTP Get请求，后台逻辑认为这个连接不符合规范()。所谓baidu定义的规范那应该就是服务器检查host，非`baidu.com`或``就拒绝访问。


### 抓包貌似看不到整个路由，是吗？如何分析整个路由？

--

## 参考

https://www.zhihu.com/question/36891472/answer/69455356

http://skyrover.me/2017/02/19/BAIDU%E7%9A%84DNS%E8%A7%A3%E6%9E%90/
