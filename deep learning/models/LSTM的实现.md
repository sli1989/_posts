---
title: LSTM的源码浅析
date: 2018-02-06 19:08:53
tags: lstm
categories:
- deep learing
- RNN
---

<!-- the implementation of LSTM -->

# Overview

LSTM是RNN的一种，

名字：
long short-term memory。
意思是vanilla RNN是short-term memory，sequence太长，


LSTM的核心：
- cell:
- gate: 用于解决传统RNN中的梯度消失问题



##


## 关于gate 以及梯度消失问题
<!-- vanishing gradient over time-->
包括：input gate, output gate, forget gate

> Gates are a way to optionally let information through.


<image title="d" src="https://github.com/xsung/raw/raw/master/RNN-vanish-gradient-problem.PNG" width="70%">

传统RNN中存在的梯度消失。


<image title="Preservation of gradient information by LSTM" width="70%" src="https://github.com/xsung/raw/raw/master/LSTM-grad.PNG">


LSTM中，数据从实心1向后传递。通过三个gate的配合操作，成功在节点4和6输出该数据。数据流不会因long 有效解决RNN的梯度消失问题。


参考:
- [BP Through Time and Vanishing Gradients](http://www.wildml.com/2015/10/recurrent-neural-networks-tutorial-part-3-backpropagation-through-time-and-vanishing-gradients/)
- [Supervised Sequence Labelling with Recurrent Neural Networks - Chapter 4](https://www.cs.toronto.edu/~graves/phd.pdf)

# LSTM的实现源码

## tensorflow

<image src="https://github.com/xsung/raw/raw/master/LSTMs-tensorflow-BasicLSTMCell.png">



[应用示例--基于lstm的语言模型](https://www.tensorflow.org/tutorials/recurrent)

```python
lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)
# current_batch_of_words不是sequence，只是
for current_batch_of_words in words:  
  # 这里的输入和输出都是符号，类型是tf.placeholder，lstm参数是tf.variable
  output, state = lstm(current_batch_of_words, state)
```


tensorflow源码 - [BasicLSTMCell](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/rnn_cell_impl.py#L553)

```python
def call(self, inputs, state):
  """Long short-term memory cell (LSTM).
  Args:
    inputs: `2-D` tensor with shape `[batch_size, input_size]`. 是单个时间节点的batch样本
    state: An `LSTMStateTuple` of state tensors, each shaped
      `[batch_size, self.state_size]`, if `state_is_tuple` has been set to
      `True`.  Otherwise, a `Tensor` shaped
      `[batch_size, 2 * self.state_size]`.
  Returns:
    A pair containing the new hidden state, and the new state (either a
      `LSTMStateTuple` or a concatenated state, depending on
      `state_is_tuple`).
  """
  sigmoid = math_ops.sigmoid
  one = constant_op.constant(1, dtype=dtypes.int32)
  # Parameters of gates are concatenated into one multiply for efficiency.
  if self._state_is_tuple:
    c, h = state
  else:
    c, h = array_ops.split(value=state, num_or_size_splits=2, axis=one)

  gate_inputs = math_ops.matmul(
      array_ops.concat([inputs, h], 1), self._kernel)
  gate_inputs = nn_ops.bias_add(gate_inputs, self._bias)

  # i = input_gate, j = new_input, f = forget_gate, o = output_gate
  i, j, f, o = array_ops.split(
      value=gate_inputs, num_or_size_splits=4, axis=one)

  forget_bias_tensor = constant_op.constant(self._forget_bias, dtype=f.dtype)
  # Note that using `add` and `multiply` instead of `+` and `*` gives a
  # performance improvement. So using those at the cost of readability.
  add = math_ops.add
  multiply = math_ops.multiply
  new_c = add(multiply(c, sigmoid(add(f, forget_bias_tensor))),
              multiply(sigmoid(i), self._activation(j)))
  new_h = multiply(self._activation(new_c), sigmoid(o))

  if self._state_is_tuple:
    new_state = LSTMStateTuple(new_c, new_h)
  else:
    new_state = array_ops.concat([new_c, new_h], 1)
  return new_h, new_state
```

## pytorch

包装的好复杂，参考 https://blog.ddlee.cn/2017/05/29/LSTM-Pytorch%E5%AE%9E%E7%8E%B0/



# 常见问题

为什么lstm代码里和有些图里，习惯吧output称作h(hidden)？


gate是点，还是向量？
向量， decides what parts of the cell state we’re going to output

## 参考
- [通俗经典之作--Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [BasicLSTMCell对应的paper--Recurrent Neural Network Regularization](http://arxiv.org/abs/1409.2329)
- [Supervised Sequence Labelling with Recurrent Neural Networks](https://www.cs.toronto.edu/~graves/phd.pdf)


##
