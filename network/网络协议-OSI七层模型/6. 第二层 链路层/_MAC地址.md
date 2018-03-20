


## 有了 IP 地址，为什么还要用 MAC 地址？



一. 整体与局部信息传递时候，需要知道的其实是两个地址：
- 终点地址（Final destination address）
- 下一跳的地址（Next hop address）

IP地址本质上是终点地址，它在跳过路由器（hop）的时候不会改变，而MAC地址则是下一跳的地址，每跳过一次路由器都会改变。

这就是为什么还要用MAC地址的原因之一，它起到了记录下一跳的信息的作用。

注：一般来说IP地址经过路由器是不变的，不过NAT（Network address translation）例外，这也是有些人反对NAT而支持IPV6的原因之一。
