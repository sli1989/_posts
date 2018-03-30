---
title: 关于websocket
tags:
  - html5
  - websocket
categories:
  - web
  - 服务器推送
abbrlink: 5f589e78
date: 2018-02-05 19:08:53
---
websocket属于服务器推送技术的一种。
HTML5定义了 WebSocket 协议，以及相关的编程API，能更好的实现双向通信且节省服务器资源和带宽。
>  WebSocket 实际上指的是一种协议，与我们熟知的 Http 协议是同等的一个网络协议。用网络模型结构来解释的话， WebSocket 和 Http 协议都属于 应用层协议，两者都基于传输层协议 TCP。

http协议  http://  
ftp协议   ftp://
websocket协议 ws://

Websocket是基于HTTP协议的，或者说借用了HTTP的协议来完成一部分握手。
在握手阶段是一样的

## 背景

以前的网站为了实现推送功能，使用的方法都是轮询。所谓的轮询就是在特定的时间间隔（例如1秒），由浏览器向服务器发出一个 Http request，然后服务器返回最新的数据给客户端浏览器，从而给出一种服务端实时推送的假象。由于Http Request的Header（请求头）很长,而传输的数据可能很短就只占一点点，每次请求消耗的带宽大部分都消耗在 Header上。从网上资料得知后来还有改进的轮询方法叫做 Comet，使用 Ajax。但这种技术虽然可达到双向通信，但依然需要发出请求，而且在Comet中，普遍采用了长链接，这也会大量消耗服务器带宽和资源。


## 流程

1. 首先WebSocket 服务器启动，并监听端口
2. 客户端new websocket(dfd)，建立连接


## 客户端的API (js)

不同浏览器有不同的实现，但都提供的javascript API，所以客户端API都类似，或者可以统一API。



## 服务端的实现
websocket服务器则因语言不同而提供不同的调用方式。

是叫实现，还是应该叫封装？

- 基于java的实现
    - [tomcat的websocket实现](https://github.com/BitMindLab/tomcat-example/tree/master/WEB-INF/classes/websocket/)
    - [jetty的websocket实现]()
- 基于nodejs的实现
    - 服务器端的socket.io，搭配客户端js库`socket.io-client`
- 基于python的实现
- 基于shell的实现
    - WebSocketd


## 原理

```bash
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket      ## 这个就是Websocket的核心了，告诉Apache、Nginx等服务器：注意啦，窝发起的是Websocket协议，快点帮我找到对应的助理处理~不是那个老土的HTTP。
Connection: Upgrade    ##
Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
Origin: http://example.com
```



## 参考

- http://www.ruanyifeng.com/blog/2017/05/websocket.html
- https://en.wikipedia.org/wiki/Comparison_of_WebSocket_implementations

- [学习WebSocket协议—从顶层到底层的实现原理](https://github.com/abbshr/abbshr.github.io/issues/22)
- [WebSocket 是什么原理？为什么可以实现持久连接？](https://www.zhihu.com/question/20215561)  ---很赞

- [理论联系实际：从零理解WebSocket的通信原理、协议格式、安全性](https://juejin.im/entry/5a5c559c518825734859ee5e)

## 疑问
- websocket是依赖TCP吗？


#### 如何debug websocket？

**方式一：在chrome inspect中查看websocket连接**

network下的WS选项可以查看websocket连接。
能看到Request连接:wss://echo.websocket.org/
在frame中能看到明文数据，wss竟然也是明文传输

[超详细教程](https://kaazing.com/inspecting-websocket-traffic-with-chrome-developer-tools/)




**方式二：通过chrome console中命令查看**
```
var webSocket = new WebSocket('ws://address:port');
webSocket.onmessage = function(data) { console.log(data); }
```

**方式三：在chrome internal里查看**

chrome://net-internals/#sockets

**方式四：通过抓包查看**

见network/tools/wireshark/抓包





#### 如何查看websocket发送的数据？

浏览器inspect能看到websocket连接，为什么没看到发送的数据包？
那么通过抓包总能够看到吧。


- websocket的实现原理是什么？在TCP的基础上做了什么？加了header？


## online demo

- [socket.io的在线聊天室](https://socket.io/demos/chat/)
- [webSocket.org Echo demo](http://www.websocket.org/echo.html)








##




##
