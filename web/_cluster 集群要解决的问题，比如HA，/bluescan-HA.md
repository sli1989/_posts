


## HA

-----

## 应用服务器HA/集群 & 负载均衡 & session共享



hi zhili ，我用nginx搭的负载均衡。

入口：
http://172.29.163.101:8080/bluescan/


实际节点：
http://172.29.163.104:8081/bluescan/
http://172.29.163.101:8081/bluescan/

目前采用的round-robin的轮替方式，暂时没发现什么问题。
另外绑定ip的方式，当一个节点故障，nginx会自动切换到另外节点。所以source-ip轮替方式也差不多够用



### 负载均衡


### session共享

-----

## 数据库 & 缓存

为什么要用solr？
不全文检索，就没必要用solr


derby？
小，稳定，但是只有本地版，

mysql？

redis

postgres

## 
