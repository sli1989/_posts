---
title: wireshark原理
date: 2018-02-09
tags: ["network"]
categories:
- network
- tools
---

<!--
实际上吧，叫 抓包(packet analyzer)也能算是一个分类

-->


## 常用filter

常用的filter可参考`wireshark--视图--着色规则`

表达式规则

 1. 协议过滤

比如TCP，只显示TCP协议。
http
dns

同时显示两个协议： http || dns

2. IP 过滤

比如 ip.src ==192.168.1.102 显示源地址为192.168.1.102，

ip.dst==192.168.1.102, 目标地址为192.168.1.102

3. 端口过滤

tcp.port ==80,  端口为80的

tcp.srcport == 80,  只显示TCP协议的愿端口为80的。

4. Http模式过滤

http.request.method=="GET",   只显示HTTP GET方法的。

5. 逻辑运算符为 AND/ OR

常用的过滤表达式


## Loopback capture

本机内部进程间的socket通信，不能通过wireshark抓包。本机进程间socket通信是不经过网卡的。

- https://wiki.wireshark.org/CaptureSetup/Loopback


## Wireshark不能做的
为了安全考虑，wireshark只能查看封包，而不能修改封包的内容，或者发送封包。

## Wireshark VS Fiddler

Fiddler是在windows上运行的程序，专门用来捕获HTTP，HTTPS的。

wireshark能获取HTTP，也能获取HTTPS，但是不能解密HTTPS，所以wireshark看不懂HTTPS中的内容



总结，如果是处理HTTP,HTTPS 还是用Fiddler,  其他协议比如TCP,UDP 就用wireshark
