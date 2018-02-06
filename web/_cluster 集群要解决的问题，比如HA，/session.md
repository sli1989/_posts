一、工作中因为要使用到Tomcat集群部署，此时就涉及到了Session共享问题，主要有三种解决方案：

0. tomcat自带的session共享

1. 使用数据库来存储Session

2. 使用Cookie来存储Session

3. 使用Redis来存储Session。优点：使用Session的代码没有任何变化，Tomcat默认把Session保存到Redis上面了。



二、本文中主要讲一下第3种方案，也就是使用Redis来存储Session，Github中已经有该开源组件（tomcat-redis-session-manager），下面讲一下配置的步骤

1、配置tomcat配置文件context.xml