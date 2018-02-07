

## residual & highway 发展历程

### Highway Networks

既然LSTM gate 也是为了解决 Information flow，有没有其他方式去解决？更直观一点的，不通过 gradient 的？既然 information 像被阻隔了一样，我们就“暴力”让它通过一下，给它们来个特权——在某些 gate 上，你就不用接受“审查”（transform）了，直接通过吧。这像高速公路一样——于是就有了这个名字，Highway Networks（HW-Nets）。  （gate直接等于1吗？）



###  Deep Residual Learning for Image Recognition 


### Identity Mappings in Deep Residual Networks
分析了 ResNet 中 Identity mapping 为什么比较好，为何能让梯度在网络中顺畅的传递而不会爆炸或消失

Residual Net 核心思想是，去拟合残差函数 F （F = y - h（x）），选 h(x)=x 时效果最好。



### code

* torch (lua)
    * [resnet-1k-layers](https://github.com/KaimingHe/resnet-1k-layers) by Kaiming He
    * [fb.resnet.torch](https://github.com/facebook/fb.resnet.torch)


## 待看blog

