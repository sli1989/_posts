---
title: 渣渣中的渣渣 之 DaoVoice
tags:
  - hexo
  - plugin
  - instant-message
categories:
  - web
  - blog-framework
  - nodejs-hexo
  - plugin
abbrlink: 9ff21bc3
date: 2018-01-25 03:08:53
---
## 垃圾中的垃圾 之 DaoVoice

特点：高延迟

你如果用过DaoVoice的话，肯定知道它延迟很长。但是为什么延迟这么长呢，下面来看看。

通常web-chat都采用websocket。
html--server--html
就是一堆的websocket连接


反应特别慢，消息的发送和接收，在websocket中并未看到。


**消息的发送**
https://im.daovoice.io/v1/conversations/b1fba959-a843-43ca-9538-928a1cdfd62d/reply
的request payload参数进行明文传输的。

**消息的接收**
https://im.daovoice.io/v1/conversations/b1fba959-a843-43ca-9538-928a1cdfd62d/read

消息接收并非是服务器推送的，而是每次客户端主动发送消息时才会触发消息接收。(DaoVoice的设计也太挫了吧，这可不是一般的延迟啊，根本不能叫instant message)

开了个websocket，什么事都不干，发一些没用的数据。



## dao voice原理

基于websocket

Request
```
Request URL:wss://rtm.daovoice.io/socket.io/?EIO=3&transport=websocket&sid=-ezTav4AxWfvgBszAjuI
Request Method:GET
Status Code:101 Switching Protocols
```

Response header
```
Connection:upgrade
Date:Tue, 06 Feb 2018 01:52:13 GMT
Sec-WebSocket-Accept:+vrxS3Tw4HDKi3JDS5wRL7vIqKc=
Sec-WebSocket-Extensions:permessage-deflate
Server:nginx/1.9.13
Upgrade:websocket
```

Frames



首先发送http请求
https://rtm.daovoice.io/socket.io/?EIO=3&transport=polling&t=M5ZWKps&sid=JtjO6wXdOoHH7RXWFqhw

https://im.daovoice.io/v1/conversations/02010594-d7b8-4f3a-896a-4f82e2cc9198/fetch
https://im.daovoice.io/v1/conversations/02010594-d7b8-4f3a-896a-4f82e2cc9198/read
https://im.daovoice.io/v1/conversations/02010594-d7b8-4f3a-896a-4f82e2cc9198/reply

## 如何自己实现在线联系

### 利用websocket


### 利用微信api












## 参考
[利用dao voice](https://www.ezlippi.com/blog/2018/01/next-chat.html)
