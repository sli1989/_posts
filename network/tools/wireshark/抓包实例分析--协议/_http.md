---
title: 一次完整的HTTP请求过程

---



域名解析 --> 发起TCP的3次握手 --> 建立TCP连接后发起http请求 --> 服务器响应http请求，浏览器得到html代码 --> 浏览器解析html代码，并请求html代码中的资源（如js、css、图片等） --> 浏览器对页面进行渲染呈现给用户



##

使用命令 wget www.baidu.com 来请求，发现直接使用chrome浏览器请求时，干扰请求比较多，所以就使用wget命令来请求，不过使用wget命令只能把index.html请求回来，并不会对index.html中包含的静态资源（js、css等文件）进行请求。




## 待看

https://www.cnblogs.com/engeng/articles/5959335.html
