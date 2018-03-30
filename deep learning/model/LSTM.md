---
title: LSTM的源码浅析
keywords:
  - lstm
  - rnn
  - 源码
  - 深度学习
  - deep learning
tags: lstm
categories:
  - deep learning
  - model
abbrlink: a6941437
date: 2018-02-06 19:08:53
---
<!-- the implementation of LSTM -->

# Overview

LSTM网络是RNN的一种，专门设计用于解决long-term dependency/memory问题，1997年由 Hochreiter & Schmidhuber提出。
<!-- Long Short Term Memory networks – usually just called “LSTMs” – are a special kind of RNN, capable of learning long-term dependencies.  -->

名字：
long short-term memory。
意思是vanilla RNN是short-term memory，sequence太长，


LSTM的核心：
- cell + gate, cel
用于解决传统RNN中的梯度消失问题 (Gradient Vanish)




- **LSTM只能避免RNN的梯度消失**（gradient vanishing）；
- 梯度膨胀(gradient explosion)不是个严重的问题，一般靠裁剪后的优化算法即可解决，比如gradient clipping（如果梯度的范数大于某个给定值，将梯度同比收缩）。下面简单说说LSTM如何避免梯度消失.
- 梯度弥散是什么鬼？

cell: memory_cell



## 关于gate 以及梯度消失问题
<!-- vanishing gradient over time,或者 The Problem of Long-Term Dependencies-->

包括：input gate, output gate, forget gate

gate，即阀门，是一种开关。取值范围[0,1]，0表示关闭，1表示通行



<!-- 备用图片 http://www.solidswiki.com/images/3/34/Gate_valves.gif -->

<image width="70%" src="https://i.makeagif.com/media/7-27-2015/OLkiOf.gif">

> Gates are a way to optionally let information through.

待看
- An Empirical Exploration of Recurrent Network Architectures.
- Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling.

### 梯度消失问题--直观解释
<!-- In theory, RNNs are absolutely capable of handling “long-term dependencies.” -->

<image title="d" src="/images/raw/RNN - vanish gradient problem.png" width="70%">

传统RNN中存在的梯度消失。
<!-- conventional RNN: 1. The sensitivity of the input valus decays overtime 2. The network forgets the previous input-->


### 梯度消失 -- 产生的原因


本质原因就是因为矩阵高次幂导致的

在多层网络中，影响梯度大小的因素主要有两个：权重和激活函数的偏导。深层的梯度是多个激活函数偏导乘积的形式来计算，如果这些激活函数的偏导比较小（小于1）或者为0，那么梯度随时间很容易vanishing；相反，如果这些激活函数的偏导比较大（大于1），那么梯度很有可能就会exploding。因而，梯度的计算和更新非常困难。

https://www.zhihu.com/question/34878706

参考:
- [BP Through Time and Vanishing Gradients](http://www.wildml.com/2015/10/recurrent-neural-networks-tutorial-part-3-backpropagation-through-time-and-vanishing-gradients/)
- [Supervised Sequence Labelling with Recurrent Neural Networks - Chapter 4](https://www.cs.toronto.edu/~graves/phd.pdf)
- [关于valve的比喻](https://medium.com/mlreview/understanding-lstm-and-its-diagrams-37e2f46f1714)


<!-- we fist introduce the interface, then the implementation  -->

## 梯度消失问题 -- 解决方案

使用一个合适激活函数，它的梯度在一个合理的范围。LSTM使用gate function，有选择的让一部分信息通过。gate是由一个sigmoid单元和一个逐点乘积操作组成，sigmoid单元输出1或0，用来判断通过还是阻止，然后训练这些gate的组合。所以，**当gate是打开的（梯度接近于1），梯度就不会vanish。并且sigmoid不超过1，那么梯度也不会explode**。

<img src="https://pic3.zhimg.com/80/v2-f093af62bd8ef9f9b31aa76c4948eb95_hd.jpg">


参考：https://www.zhihu.com/question/44895610

## 梯度消失问题 -- LSTM是如何避免的

1、当gate是关闭的，那么就会阻止对当前信息的改变，这样以前的依赖信息就会被学到。2、当gate是打开的时候，并不是完全替换之前的信息，而是在之前信息和现在信息之间做加权平均。所以，无论网络的深度有多深，输入序列有多长，只要gate是打开的，网络都会记住这些信息。



<!-- https://www.cc.gatech.edu/~san37/img/dl/grad_lstm.png -->
<image title="Preservation of gradient information by LSTM" width="70%" src="/images/raw/LSTM - preservation of gradient.png">
<!-- LSTM: 1. The cell remember the input as long as it wants 2. The output can be used anytime it wants-->

上面这个例子中，数据从实心1向后传递。通过gate的配合，成功在节点4和6输出该数据。数据流不会因long-term传输而消息，有效解决RNN的梯度消失问题。


- 当gate是关闭的，那么就会阻止对当前信息的改变，这样以前的依赖信息就会被学到。
- 当gate是打开的时候，并不是完全替换之前的信息，而是在之前信息和现在信息之间做加权平均。所以，无论网络的深度有多深，输入序列有多长，只要gate是打开的，网络都会记住这些信息。



# LSTM: 接口设计

##


```python
output, (h_n, c_n) = lstm(input, (h_0, c_0))  # pytorch的接口 hidden=(h,c)
new_h, (new_c, new_h) = lstm(inputs, (c, h))  # tensorflow的接口，其中state=(c, h)
```

inputs, state):
inputs, state):




**为什么lstm代码里和有些图里，习惯吧output称作h(hidden)？**
https://zhuanlan.zhihu.com/p/28919765
接口(对LSTM的封装)要具有良好的扩展性(水平扩展-sequence，垂直扩展-stack)。
在stack lstm中，下一层的out对接上一层的input，在深度模型的概念里这就是隐含层hidden的作用，所以命名为hidden。

但是呢，作为一个cell，我还是觉得叫output比较好。追根溯源，谁第一个采用hidden命名的？


**为什么lstm代码里要把(c, h)封装成一个tuple？**
这样设计的目的是为了兼容RNN的接口(毕竟LSTM属于RNN的一种)。




- [pytorch 源码 - LSTM](https://github.com/pytorch/pytorch/blob/master/torch/nn/modules/rnn.py#L346)
- [tensorflow源码 - BasicLSTMCell](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/rnn_cell_impl.py#L553)

## example 应用示例


[应用示例--基于lstm的语言模型](https://www.tensorflow.org/tutorials/recurrent)

```python
lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)
# current_batch_of_words不是sequence，只是
for current_batch_of_words in words:  
  # 这里的输入和输出都是符号，类型是tf.placeholder，lstm参数是tf.variable
  output, state = lstm(current_batch_of_words, state)
```


# LSTM: 实现

## LSTM: tensorflow实现

<image src="/images/raw/LSTM - tensorflow with Equation.png">


tensorflow源码 - [BasicLSTMCell](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/rnn_cell_impl.py#L553)

```python
# 源码精简版
def call(self, inputs, state):
  """Run one step of LSTM.
  Args:
    inputs: `2-D` tensor with shape `[batch_size, input_size]`. 是单个时间节点的batch样本
    state:
  Returns:
    hidden state, new state ().
  """
  c, h = state
  gate_inputs = math_ops.matmul(
      array_ops.concat([inputs, h], 1), self._kernel)
  gate_inputs = nn_ops.bias_add(gate_inputs, self._bias)
  # i = input_gate, j = new_input, f = forget_gate, o = output_gate
  i, j, f, o = array_ops.split(
      value=gate_inputs, num_or_size_splits=4, axis=one)

  forget_bias_tensor = constant_op.constant(self._forget_bias, dtype=f.dtype)

  # update
  new_c = add(multiply(c, sigmoid(add(f, forget_bias_tensor))),
              multiply(sigmoid(i), self._activation(j)))
  new_h = multiply(self._activation(new_c), sigmoid(o))
  new_state = LSTMStateTuple(new_c, new_h)
  return new_h, new_state
```

## pytorch

包装的好复杂，参考 https://blog.ddlee.cn/2017/05/29/LSTM-Pytorch%E5%AE%9E%E7%8E%B0/





# 常见问题


关于静态图和动态图？




gate是点，还是向量？
向量， decides what parts of the cell state we’re going to output

## 其他参考
- [通俗经典之作--Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [BasicLSTMCell对应的paper--Recurrent Neural Network Regularization](http://arxiv.org/abs/1409.2329)
- [Supervised Sequence Labelling with Recurrent Neural Networks](https://www.cs.toronto.edu/~graves/phd.pdf)


##
