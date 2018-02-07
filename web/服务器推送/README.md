---
title: 服务器推送技术
date: 2018-02-07 19:08:53
tags: ["web","推送"]
categories:
- web
- 推送技术
---

## 主要推送技术

- 伪推送技术，轮询
  - AJAX短轮询：客户端定时向服务器发送ajax请求，服务器接到请求后马上返回响应信息并关闭连接。<br>
  `缺点`: 请求中有大半是无用，浪费带宽和服务器资源。<br>
  `实例`:

  - Comet
    - 基于Ajax的长轮询(long-polling): 其原理是利用AJAX给后台发送请求，后台不立即返回客户端数据，而是保持这个请求等待数据到来（或超时），之后将数据作为结果返回给客户端。浏览器JS在处理请求返回信息（超时或有效数据）后再次发出请求，重新建立连接。<br>
    `优点`: 在无消息的情况下不会频繁的请求。<br>
    `缺点`: 服务器hold连接会消耗资源<br>
    `实例`: WebQQ、web微信、Facebook IM

    - 基于 Iframe 及 htmlfile 的流(http streaming): 在页面里嵌入一个隐蔵iframe，将这个隐蔵iframe的src属性设为对一个长连接的请求，服务器端就能源源不断地往客户端输入数据。(怎么搞？iframe是怎么个原理，待看)
    <br>
    `优点`：消息即时到达，不发无用请求。<br>
    `缺点`：服务器维护一个长连接会增加开销。<br>
    `实例`: Gmail聊天<br>
    这个貌似不是`伪推送`了吧？


- 推送
  - websocket采用了一些特殊的报头(Header)，使得浏览器和服务器只需要做一个握手的动作，就可以在浏览器和服务器之间建立一条连接通道，而毋须消耗大量服务器资源。<br>
  `缺点`: 某些浏览器可能不支持<br>
  `实例`:
  - SSE(Server-Sent Event，服务端推送事件): ...
## 使用场景

实时性要求不高使用长轮询，比如微博；实时性要求较高使用comet，比如聊天室。


## 其他技术

- AJAX multipart streaming
- Forever Iframe
- JSONP Polling：比如知乎
- Flash Socket：在页面中内嵌入一个使用了Socket类的 Flash 程序JavaScript通过调用此Flash程序提供的Socket接口与服务器端的Socket接口进行通信，JavaScript在收到服务器端传送的信息后控制页面的显示。
优点：实现真正的即时通信，而不是伪即时。
缺点：客户端必须安装Flash插件；非HTTP协议，无法自动穿越防火墙。
实例：网络互动游戏。


## 参考
https://www.zhihu.com/question/19876749
