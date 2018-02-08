


## demo
首先，去web/html5/websocket教程中查看demo，


## 建立连接

webSocket建立以后不再有tcp连接建立:


## 过滤规则(rules in filter)

方式一：按端口过滤
```
tcp.dstport == your_websoket_port
```

方式二：按协议过滤
```
websocket
```


## 抓包分析 --  echo.websocket.org

我的ip 9.186.58.178
echo.websocket.org 174.129.224.73

```
No      Time        Source          Destination     Protocol length Info
12821   649.588871  174.129.224.73	9.186.58.178	WebSocket	84	WebSocket Text [FIN]
```

```
Frame 12821: 84 bytes on wire (672 bits), 84 bytes captured (672 bits) on interface 0
Ethernet II, Src: Cisco_42:89:c0 (e8:ba:70:42:89:c0), Dst: IntelCor_09:85:f8 (e8:b1:fc:09:85:f8)
Internet Protocol Version 4, Src: 174.129.224.73, Dst: 9.186.58.178
Transmission Control Protocol, Src Port: 80, Dst Port: 65331, Seq: 543, Ack: 667, Len: 30
WebSocket
Line-based text data
    Rock it with HTML5 WebSocket
```


## 疑问
[FIN] 和 [FIN][MASKED]什么区别？

websocket为什么是单独的一个层？是不是算在了应用层和传输层之间的某个层。
line-based text data包含数据，为什么也是单独的一个层？


是否明文传输？
是明文传输的!

我为啥开了ssl也能看见明文？（用https握手之后用wss连接的） -- 来自知乎

## 参考

http://blog.csdn.net/lusyoe/article/details/53858320
