---
title: 抓包 斗鱼
---
## 浏览器信息

浏览器访问的URL

```
    http://www.douyu.com/   # 浏览器访问斗鱼的主页，下面是对视频的请求
    http://175.25.168.26/hdl3.douyucdn.cn/live/868191rzb9Z8BR7r.flv?wsAuth=927a7c21a4c2303678529e208271ea1b&token=web-566086-868191-d17a433e9e430492d1b7be4cf13dc183&logo=0&expire=0&wsiphost=ipdb
```
socket会keep-alive，复用同一个socket，url保持不变。

Request Header

```
GET /hdl3.douyucdn.cn/live/852315r71MZwNkYi.flv?wsAuth=98cdd891123dc85668196c67d741a853&token=web-566086-852315-c12ea88bc6b9657e3e6bf1e3f7794fa9&logo=0&expire=0&wsiphost=local HTTP/1.1
Host: 114.64.222.49  # 首页会因为直播间不同，而Host和URL不同。
Connection: keep-alive
X-Requested-With: ShockwaveFlash/22.0.0.192
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
Accept: */*
Referer: http://www.douyu.com/
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4
```

Response Header

```
HTTP/1.1 200 OK
Expires: Sat, 30 Jul 2016 09:28:28 GMT
Cache-Control: no-cache
Content-Type: video/x-flv
Pragma: no-cache
Via: 1.1 zdx49:7755 (Cdn Cache Server V2.0)
Connection: close
```
## wireshark抓包

filter: ip.dst==114.64.222.49 or ip.src==114.64.222.49

filter之后显示的连接数据包如下：

```
No      Time        Source          Destination     Protocol length Info
// 三次握手
1672	15.896971	9.186.58.171	114.64.222.49	TCP	     66	    54185 → 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1
1674	15.906057	114.64.222.49	9.186.58.171	TCP	     66	    80 → 54185 [SYN, ACK] Seq=0 Ack=1 Win=1460 Len=0 MSS=1380 SACK_PERM=1 WS=128
1675	15.906271	9.186.58.171	114.64.222.49	TCP	     54 	54185 → 80 [ACK] Seq=1 Ack=1 Win=16560 Len=0
// 握手成功，第四个包才是http的
1676	15.907013	9.186.58.171	114.64.222.49	HTTP	 592	GET /hdl3.douyucdn.cn/live/852315r71MZwNkYi.flv?wsAuth=98cdd891123dc85668196c67d741a853&token=web-566086-852315-c12ea88bc6b9657e3e6bf1e3f7794fa9&logo=0&expire=0&wsiphost=local HTTP/1.1
// server向client发送一个ack码，约定以后客户端必须通过seq=539来确认收到的总字节数目
1677	15.916612	114.64.222.49	9.186.58.171	TCP  	 54	    80 → 54185 [ACK] Seq=1 Ack=539 Win=15744 Len=0

// 传输视频流数据
1679	16.376026	114.64.222.49	9.186.58.171	TCP	     247	[TCP segment of a reassembled PDU]
1680	16.378970	114.64.222.49	9.186.58.171	TCP	     1434	[TCP segment of a reassembled PDU]
1681	16.379198	114.64.222.49	9.186.58.171	TCP	     1434	[TCP segment of a reassembled PDU]
1682	16.379304	114.64.222.49	9.186.58.171	TCP	     1434	[TCP segment of a reassembled PDU]
1683	16.379412	114.64.222.49	9.186.58.171	TCP	     1434	[TCP Previous segment not captured] [TCP segment of a reassembled PDU]
1684	16.379451	114.64.222.49	9.186.58.171	TCP  	 1434	[TCP segment of a reassembled PDU]
1685	16.379476	114.64.222.49	9.186.58.171	TCP	     1434	[TCP Out-Of-Order] [TCP segment of a reassembled PDU]
1686	16.379921	9.186.58.171	114.64.222.49	TCP 	 54	    54185 → 80 [ACK] Seq=539 Ack=1574 Win=16560 Len=0  //
1687	16.379937	9.186.58.171	114.64.222.49	TCP 	 54	    54185 → 80 [ACK] Seq=539 Ack=4334 Win=16560 Len=0

```



连接流程

```
三次握手:
    第一次握手：客户端向服务器发送连接请求包，标志位SYN（同步序号）置为1，序号为X=0
    第二次握手：服务器收到客户端发过来报文，由SYN=1知道客户端要求建立联机。向客户端发送一个SYN和ACK都置为1的TCP报文，设置初始序号Y=0，将确认序号(Acknowledgement Number)设置为客户的序列号加1，即X+1 = 0+1=1,
    第三次握手：客户端收到服务器发来的包后检查确认序号(Acknowledgement Number)是否正确，即第一次发送的序号加1（X+1=1）。以及标志位ACK是否为1。若正确，服务器再次发送确认包，ACK标志位为1，SYN标志位为0。确认序号(Acknowledgement Number)=Y+1=0+1=1，发送序号为X+1=1。客户端收到后确认序号值与ACK=1则连接建立成功，可以传送数据了。
HTTP请求:
断开连接: (客户端要求断开连接则需要四次挥手)
```





HTTP包(No 1676)
```
物理层: Frame:  1676: 592 bytes on wire (4736 bits), 592 bytes captured (4736 bits) on interface 0   // 物理层的数据帧概况
链路层: Ethernet II, Src: IntelCor_09:85:f8 (e8:b1:fc:09:85:f8), Dst: All-HSRP-routers_65 (00:00:0c:07:ac:65)   // 数据链路层以太网帧头部信息，e8:b1:fc:09:85:f8这是我的mac地址
网络层: Internet Protocol Version 4, Src: 9.186.58.171, Dst: 114.64.222.49  // 9.186.58.171是本机ipconfig显示的ip，也就是局域网ip (不是网关ip，也不是外网ip)
传输层: Transmission Control Protocol, Src Port: 54185 (54185), Dst Port: 80 (80), Seq: 1, Ack: 1, Len: 538
应用层: 跟浏览器中的request header相同

注意: Frame = sum[header] + content(null)，即一堆header叠加在一起，封装在物理层数据帧中，没有内容
```

TCP视频流数据包(No 1680)
```
物理层: Frame 1680: 1434 bytes on wire (11472 bits), 1434 bytes captured (11472 bits) on interface 0
链路层: Ethernet II, Src: CiscoInc_42:96:c0 (e8:ba:70:42:96:c0), Dst: IntelCor_09:85:f8 (e8:b1:fc:09:85:f8)
网络层: Internet Protocol Version 4, Src: 114.64.222.49, Dst: 9.186.58.171
传输层: Transmission Control Protocol, Src Port: 80 (80), Dst Port: 54185 (54185), Seq: 194, Ack: 539, Len: 1380

注意: Frame = sum[header] + content(很多内容)
```

## 其他细节

### TCP out of order

原因：
多半是网络拥塞，导致顺序包抵达时间不同，延时太长，或者包丢失，需要重新组合数据单元，因为他们可能是通过不同的路径到达的。
TCP Out-Of-Order ，有些 Packet 可能 Lost，所以重新传送造成。
另一个可能是因为 Client 到 Server 间有两条网路路径，像是 Load Balance 之类的架构。
因此若两个封包走不同路径，晚送的封包却比早送的到达，就会发生 Out-Of-Order。

解决方法:
- reassembling packets into order
- forcing retries of out-of-order packets.

- 参考 https://en.wikipedia.org/wiki/Out-of-order_delivery

###

## comments

- 能够看出是一直复用的一个连接: 54189<-->80 端口之间建立的socket连接


## 疑问

    - 为什么采用TCP
    - TCP阻塞问题怎样解决的
    - tcp丢包是否还会续传？续传仍然丢包呢
    - socket编程中，send之后的status只怎么来的？应该是两个数据包吧？可以试试
