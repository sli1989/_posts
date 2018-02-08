## introduction

- python socket编程
- java socket编程

## python socket编程

### 测试1

    import socket
    
    def sendHttpViaSocket():
        tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print tcpsoc.connect(('9.186.102.103', 8080)) # 三次握手 (三个包)
        print tcpsoc.send('GET /bluescan/ HTTP/1.1\r\nHOST:anystring\r\n\r\n') # 进行get请求，并获取数据
        response = tcpsoc.recv(1000000)  # 不发送数据包
        print response
    
    if __name__ == '__main__':
        sendHttpViaSocket()
    
    
    

### console输出:

    None
    43
    HTTP/1.1 200 OK
    Server: Apache-Coyote/1.1
    Accept-Ranges: bytes
    ETag: W/"2946-1467880723568"
    Last-Modified: Thu, 07 Jul 2016 08:38:43 GMT
    Content-Type: text/html;charset=UTF-8
    Content-Length: 2946
    Date: Sat, 30 Jul 2016 12:14:57 GMT
    
    <!DOCTYPE html>
    <html>  
    ...
    </html>

    
### wireshark抓包:

filter: ip.dst==9.186.102.103 or ip.src==9.186.102.103


    No  Time        Source          Destination     Pro   Len   Info
    // tcpsoc.connect(('9.186.102.103', 8080)) # 往返发送三个数据包，进行三次握手
    66	3.063170	9.186.58.171	9.186.102.103	TCP	  66	58415 → 8080 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1
    67	3.064642	9.186.102.103	9.186.58.171	TCP	  66	8080 → 58415 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
    68	3.064861	9.186.58.171	9.186.102.103	TCP	  54	58415 → 8080 [ACK] Seq=1 Ack=1 Win=17520 Len=0
    
    // tcpsoc.send('GET /bluescan/ HTTP/1.1\r\nHOST:anystring\r\n\r\n')
    // 一个html文件比较大，会分成几个数据包发送。
    69	3.065188	9.186.58.171	9.186.102.103	HTTP  94	GET /bluescan/ HTTP/1.1 
    70	3.070695	9.186.102.103	9.186.58.171	TCP	  1514	[TCP segment of a reassembled PDU]
    71	3.071086	9.186.102.103	9.186.58.171	TCP	  1514	[TCP segment of a reassembled PDU]
    72	3.071471	9.186.58.171	9.186.102.103	TCP   54	58415 → 8080 [ACK] Seq=41 Ack=2921 Win=17520 Len=0
    73	3.072820	9.186.102.103	9.186.58.171	HTTP  322	HTTP/1.1 200 OK  (text/html) // 这里会对之前的数据包做一个拼接(只拼接No)
    
    // 程序结束，socket由客户端自动结束 (四次挥手)
    74	3.074085	9.186.58.171	9.186.102.103	TCP	  54	58415 → 8080 [FIN, ACK] Seq=41 Ack=3189 Win=17252 Len=0
    75	3.076070	9.186.102.103	9.186.58.171	TCP	  54	8080 → 58415 [ACK] Seq=3189 Ack=42 Win=65536 Len=0
    76	3.076118	9.186.102.103	9.186.58.171	TCP	  54	8080 → 58415 [FIN, ACK] Seq=3189 Ack=42 Win=65536 Len=0
    77	3.076302	9.186.58.171	9.186.102.103	TCP	  54	58415 → 8080 [ACK] Seq=42 Ack=3190 Win=17252 Len=0



其中HTTP包(No 70)


    物理层: Frame 49: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits) on interface 0
    链路层: Ethernet II, Src: CiscoInc_42:89:c0 (e8:ba:70:42:89:c0), Dst: IntelCor_09:85:f8 (e8:b1:fc:09:85:f8)
    网络层: Internet Protocol Version 4, Src: 9.186.102.103, Dst: 9.186.58.203
    传输层: Transmission Control Protocol, Src Port: 8080 (8080), Dst Port: 58415 (58415), Seq: 1, Ack: 44, Len: 1460





## 

### 测试2，分小包发送

    import socket
    
    # 一口气能说完的话，非要分开很多包发送，很贱哎
    def sendHttpViaSocket():
        tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print tcpsoc.connect(('9.186.102.103', 8080)) # 三次握手 (三个包)
        tcpsoc.send('GET /bluescan/ HTTP/1.1') # 发送一个数据包，server返回一个ack (两个包)
        tcpsoc.send('\r\n') # 发送一个数据包，server返回一个ack (两个包)
        tcpsoc.send('HOST:anystring\r\n') # 发送一个数据包，server返回一个ack (两个包)
        tcpsoc.send('\r\n') # 到这才开始发送http请求数据包，并收到数据
        response = tcpsoc.recv(1000000) # do nothing
        print response
    
    if __name__ == '__main__':
        sendHttpViaSocket()
        
        
## java socket编程

client端代码

    package song.net.socket;
    
    /**
     * download from 
     * http://www.javatpoint.com/socket-programming
     */
    
    import java.io.*;
    import java.net.*;
    
    public class MyClientOneside {
    	public static void main(String[] args) {
    		try {
    			Socket s = new Socket("9.186.102.103", 6666); // 进行三次握手 (三个数据包)
    			DataOutputStream dout = new DataOutputStream(s.getOutputStream());  // 没包
    			dout.writeUTF("Hello Server"); // 发送一个数据包，返回一个确认包 (两个包)
    			dout.flush();
    
    			dout.close();
    			s.close();
    
    		} catch (Exception e) {
    			System.out.println(e);
    		}
    	}
    }


server端代码:

    package song.net.socket;
    
    /**
     * download from 
     * http://www.javatpoint.com/socket-programming
     */
    import java.io.*;
    import java.net.*;
    
    public class MyServerOneside {
    	public static void main(String[] args) {
    		try {
    			ServerSocket ss = new ServerSocket(6666);
    			Socket s = ss.accept();// establishes connection，等待连接，client端 new Socket("localhost", 6666)后，这一行执行好
    			DataInputStream dis = new DataInputStream(s.getInputStream()); // server端接收socket的信息
    			String str = (String) dis.readUTF(); //这里会卡住，等待client端 dout.writeUTF("Hello Server");
    			System.out.println("message= " + str);
    			ss.close();
    
    		} catch (Exception e) {
    			System.out.println(e);
    		}
    	}
    }


## 浏览器访问

'''
    
    Name                        Status Type      Initiator      Size
    login.html                  304    document  Other  123 B   349 ms   
    // server返回304，表示浏览器可以直接在本地缓存中读取资源，省去传输消耗
    jquery-1.7.2.min.js         304    script    login.html:43  124 B
    util.js                     304    script    login.html:44  124 B
    01_BlueSCAN_sign-in.gif     304    gif       login.html:43  125 B
    BlueSCAN_input_username.png 304    png       login.html:43  123 B
    BlueSCAN_input_password.png 304    png       login.html:43  123 B
    nudge-icon-arrow-up.png     200    png       Preview.js:28  (from cache)
    nudge-icon-arrow-down.png   200    png       Preview.js:28  (from cache)
    nudge-icon-arrow-lr.png     200    png       Preview.js:28  (from cache)
    nudge-icon-return.png       200    png       Preview.js:28
    
    
wireshark抓包




## comments

- java socket编程怎么这么丑啊！！！

## 疑问