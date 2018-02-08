
## notes发送邮件

filter: ip.dst==114.64.222.49 or ip.src==114.64.222.49
(not arp) and (not icmp) // 

tcp.port eq 25 or tcp.port eq 587 or icmp    // Show only SMTP (port 25) and ICMP traffic:

IBM nots SMTP server
 
tcp.port eq 25 or tcp.port eq 587 or tcp.port eq 26 or tcp.port eq 465 or icmp

## hotmail发邮件


## wireshark 抓包