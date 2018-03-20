

## 简介

HTTP 请求格式
HTTP请求格式主要有四部分组成，分别是：请求行、请求头、空行、消息体，每部分内容占一行

消息体：请求体是客户端发给服务端的请求数据，这部分数据并不是每个请求必须的


HTTP 响应格式
服务器接收处理完请求后返回一个HTTP相应消息给客户端。HTTP响应消息的格式包括：状态行、响应头、空行、消息体。每部分内容占一行。

## 疑问
chrome debug里的General是什么？general的remote address是什么？request header中没有这个ip啊。

### HTTP 无状态性

1. 无状态的意思就是给他一样的参数你要有一样的结果。
1. 即使HTTP协议本身“无状态”，增加cookie和session机制，就可以管理状态了。

前后两者矛盾吗，到底有没有状态？
后面的cookie是作为http参数传向后台的。每次传相同的参数(包含cookie),后台有session机制的情况下是可以返回不同结果的。



参考：
https://www.zhihu.com/question/23202402


**数学模型角度**
RNN HMM有状态，hidden state can contain information。无状态的，是时间独立的(independent through time)。

这里的`hidden state`与http中的`session`具有类似的作用。

**编程角度**

跟tf.scan  lambda表达式有关系吗？

跟streaming有关系吗？

### HTTP幂等性

幂等（idempotent、idempotence）是一个数学与计算机学概念，常见于抽象代数中。

在编程中.一个幂等操作的特点是其任意多次执行所产生的影响均与一次执行的影响相同。幂等函数，或幂等方法，是指可以使用相同参数重复执行，并能获得相同结果的函数。这些函数不会影响系统状态，也不用担心重复执行会对系统造成改变。例如，“getUsername()和setTrue()”函数就是一个幂等函数.更复杂的操作幂等保证是利用唯一交易号(流水号)实现.

**什么是幂等性(Idempotence)？**
f(f(x)) = f(x).
同一个请求，发送一次和发送N次效果是一样的！

idempotence
在编程中一个幂等操作的特点是其任意多次执行所产生的影响均与一次执行的影响相同。


参考
http://www.i3geek.com/archives/841
http://www.cnblogs.com/weidagang2046/archive/2011/06/04/2063696.html
## telnet 模拟http

1. 打开"运行"->cmd进入命令环境；
2. 输入"telnet www.baidu.com 80"，回车后 ,屏幕为全黑，此时我们利用快捷键"Ctrl+](右中括号)"来打开本地回显功能，这样我们就可以看见我们所打的东西了，

telnet 9.186.102.103 8080
GET /bluescan/ HTTP/1.1     
GET /bluescan/login.html HTTP/1.1
HOST:   // 如果不加host会出现 400 bad request,全写为 host:9.186.102.103


### 浏览器访问
http://9.186.102.103:8080/bluescan/login.html

Browser's Request Header:

    GET /bluescan/login.html HTTP/1.1
    Host: 9.186.102.103:8080  // 注意host都是精确到端口号的，如果不加端口号，就是默认的80端口
    Connection: keep-alive
    Pragma: no-cache
    Cache-Control: no-cache
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Encoding: gzip, deflate, sdch
    Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4
    Cookie: ...

Browser's Response Header:

    Age:0
    Cache-Control:max-age=60
    Connection:keep-alive
    Content-Encoding:gzip
    Content-Length:129616
    Content-Type:text/html
    Date:Wed, 27 Jul 2016 08:50:23 GMT
    Expires:Wed, 27 Jul 2016 08:51:23 GMT
    Last-Modified:Wed, 27 Jul 2016 08:48:11 GMT
    Server:PWS/8.1.38
    Vary:Accept-Encoding
    X-Px:rf-ms h0-s2.p1-maa ( origin)


### telnet模拟HTTP请求

telnet 9.186.102.103 8080

header1

    GET /bluescan/ HTTP/1.1
    HOST:anystring

    response:
    HTTP/1.1 200 OK
    Server: Apache-Coyote/1.1
    Accept-Ranges: bytes
    ETag: W/"2946-1467880723568"
    Last-Modified: Thu, 07 Jul 2016 08:38:43 GMT
    Content-Type: text/html;charset=UTF-8
    Content-Length: 2946
    Date: Wed, 27 Jul 2016 08:56:51 GMT

    <!DOCTYPE html>
    <html> ...

    解析: 1. 没有设置cookie 2. hostname为什么比较随意呢？

header2:

    GET /bluescan/ HTTP/1.1
    HOST:

    response:
    HTTP/1.1 505 HTTP Version Not Supported
    Server: Apache-Coyote/1.1
    Date: Wed, 27 Jul 2016 06:24:17 GMT
    Connection: close

    原因：第一行的行尾多了一个空格HTTP/1.1*



### socket programming

跟telnet和浏览器访问是等价的。

    import socket

    def sendHttpViaSocket():
        tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsoc.connect(('9.186.102.103', 8080)) #bind to googles ip
        tcpsoc.send('GET /bluescan/ HTTP/1.1\nHOST:anystring\n\n')
        response = tcpsoc.recv(1000000)
        print response

    if __name__ == '__main__':
        sendHttpViaSocket()

## telnet www.baidu.com

### My Header & Response

header1：

    GET / HTTP/1.1
    HOST:www.baidu.com

GET / HTTP/1.1
HOST:
Connection: keep-alive

    GET / HTTP/1.1
    HOST:www.baidu.com
    Connection: keep-alive

    response:    
    HTTP/1.1 200 OK
    Date: Wed, 27 Jul 2016 07:09:06 GMT
    Content-Type: text/html
    Content-Length: 14613
    Last-Modified: Wed, 03 Sep 2014 02:48:32 GMT
    Connection: Keep-Alive
    Vary: Accept-Encoding
    Set-Cookie: BAIDUID=5350879C0EC2CAEEB00507D07A00EE45:FG=1; expires=Thu, 31-Dec-3
    7 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: BIDUPSID=5350879C0EC2CAEEB00507D07A00EE45; expires=Thu, 31-Dec-37 23
    :55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: PSTM=1469603346; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=214748
    3647; path=/; domain=.baidu.com
    P3P: CP=" OTI DSP COR IVA OUR IND COM "
    Server: BWS/1.1
    X-UA-Compatible: IE=Edge,chrome=1
    Pragma: no-cache
    Cache-control: no-cache
    Accept-Ranges: bytes

    <!DOCTYPE html><!--STATUS OK-->
    <html>
    <head>

    解析：


### Browser's Request Header:

    GET / HTTP/1.1
    Host: www.baidu.com // 省略了80端口
    Connection: keep-alive
    Cache-Control: max-age=0
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Encoding: gzip, deflate, sdch, br
    Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4
    Cookie: ...



## telnet post

- [get与post的区别](http://www.w3school.com.cn/tags/html_ref_httpmethods.asp)

常用编码类型:   application/x-www-form-urlencoded

示例：

    telnet wenshu.court.gov.cn 80

    POST /List/ListContent HTTP/1.1
    Host: wenshu.court.gov.cn
    Connection: keep-alive
    Content-Length: 100  // 没有这一行会response： HTTP/1.1 411 Length Required
    Accept: */*
    X-Requested-With: XMLHttpRequest
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8  // 这一行貌似必须要加啊，不然返回response内容为空

    Param=%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B%3A%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6&Index=1&Page=5&Order=%E6%B3%95%E9%99%A2%E5%B1%82%E7%BA%A7&Direction=asc


## [四种POST的发包方式](http://homeway.me/2015/07/19/understand-http-about-content-type/)
Content-Type


- application/x-www-form-urlencoded  // 默认方式
- multipart/form-data
- application/json 比如 {"mapName":"myMapName","mapURL":"http://tinypic.com/myimg"}
- text/xml // 有的写作application/xml

注意区别于responseheader中的Content-Type，用于定义网络文件的类型和网页的编码，决定浏览器将以什么形式、什么编码读取这个文件。



## 注意

* GET / HTTP/1.1 行尾不能有空格，
*

## 疑问

* telnet怎么post data？ 怎么发送文件？ post数据应该是上层加密后，利用tcp传输加密后的数据把。  发送文件应该是建立一个keep-alive的socket连接？
* socket怎么post data？ 怎么发送文件？
* 直接socket编程，模拟http？
* socket编程可以实现telnet，效果一样？
* java - Send HTTP Request manually via socket

### server的80端口，如果与一个浏览器客户端建立长连接，其他客户端还能访问吗？

可以的，搞清楚socket连接的5要素: src_ip src_port dest_ip dest_port protocol.
这样才算是一个连接。同一个dest_ip:port可以同时接收多个src_ip:port的连接

### 监听的端口、建立连接的端口、数据传输的端口 是不是都是一个端口？

可以不是一个，这要看http server的具体实现。

一台服务器同时负责几万个请求，对于数据处理，如果只有一个端口负责建立连接和数据传输，这时候的服务器能否并行。


## socket常识

* 浏览器下载文件，是建立一个tcp连接，连接中断，无法续传。 (无须设置keep-alive)
* python文档写的Client sockets are normally only used for one exchange，也就是发送换一次消息，socket就废了。怎样建立keep-alive的tcp连接？
