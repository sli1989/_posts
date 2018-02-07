



## 哪些是动态图？现实中有哪些例子？


## tensorflow是怎样解决动态图问题的？



## 动态图示例：

- pytorch示例：
http://pytorch.org/tutorials/beginner/pytorch_with_examples.html#pytorch-control-flow-weight-sharing

-


##


- In PyTorch, each forward pass defines a new computational graph.
- A graph contains enough information to compute derivatives

- 每次forward定义一个graph
- backward都要重新build graph，

pytorch在什么阶段build的graph？应该是在backward阶段吧，求导阶段意味着graph完成了。a graph contains enough information to compute derivatives.


http://pytorch.org/tutorials/beginner/pytorch_with_examples.html#tensorflow-static-graphs
