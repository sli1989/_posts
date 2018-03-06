---
title: 关于RNN
date: 2018-02-06 19:08:53
tags: rnn
categories:
- deep learing
- RNN
---

##



## 历史-- 发展史--背景，rnn之前

### before rnn
-  Memoryless models for sequences
-  HMM


## RNN Overview

- 狭义上的RNN，指vanilla RNN。
- 广义上的RNN，lstm gru等都属于RNN框架。

该文章针对广义上的RNN。

RNN的形式有很多种
<image title="An unrolled recurrent neural network" src="/image/raw/rnn-overview-xs.png" >

该图的总结很好，大部分应用都可归入该框架。具体的应用可参考[karpathy](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
<!-- 框架之外的模型: attention -->

核心:
out, hidden = lstm(input, hidden)  // 来自pytorch的抽象


名词解释:
- hidden 也叫cell, hidden_state, cell_state。它是forget的关键
- out 也叫 output，
- hidden
- cell
- output在stack RNN中也叫hidden

output = new_state =

Most basic RNN:
output = new_state = act(W * input + U * state + B).

https://www.quora.com/How-is-the-hidden-state-h-different-from-the-memory-c-in-an-LSTM-cell

vanilla RNN中没有cell，所以hidden=cell=out
LSTM中


## RNN的高层抽象

> 抽象不是实现，是API。由整体到局部，可把RNN当做一个黑盒子，有需求的情况下再细看其具体实现。

### keras的RNN抽象

```python
keras.layers.RNN(cell, return_sequences=False, return_state=False, go_backwards=False, stateful=False, unroll=False)
return_sequences: 是否返回整个序列out
return_state: 是否返回整个序列的hidden
```


[应用示例--lstm用于二分类](https://github.com/keras-team/keras/blob/master/examples/imdb_lstm.py#L41)：

```python
model = Sequential()
model.add(Embedding(num_words, 128))  # 输入整个sequence
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2)) # 输出最后一个cell的output
model.add(Dense(1, activation='sigmoid')) # 二分类
```
这是上图中的`many to one`模式。

- 关于
- 关于静态图：sequence的数目固定为80


<details>
  <summary>[应用示例--基于lstm的seq2seq](https://github.com/keras-team/keras/blob/master/examples/lstm_seq2seq.py)</summary>
  <div>
  ```
  # Define an input sequence and process it.
  encoder_inputs = Input(shape=(None, num_encoder_tokens))
  encoder = LSTM(latent_dim, return_state=True)
  encoder_outputs, state_h, state_c = encoder(encoder_inputs)
  # We discard `encoder_outputs` and only keep the states.
  encoder_states = [state_h, state_c]

  # Set up the decoder, using `encoder_states` as initial state.
  decoder_inputs = Input(shape=(None, num_decoder_tokens))
  # We set up our decoder to return full output sequences,
  # and to return internal states as well. We don't use the
  # return states in the training model, but we will use them in inference.
  decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
  decoder_outputs, _, _ = decoder_lstm(decoder_inputs,
                                       initial_state=encoder_states)
  decoder_dense = Dense(num_decoder_tokens, activation='softmax')
  decoder_outputs = decoder_dense(decoder_outputs)
  ```
  <div>
</details>

<details>
  <summary>[应用示例--基于lstm的attention-seq2seq](https://github.com/keras-team/keras/blob/master/examples/lstm_seq2seq.py)</summary>
  <p><code>
  </code></p>
</details>


keras是对整个sequence做的抽象。因为keras是面向tensorflow和theano的静态图做的封装。



### pytorch的RNN抽象

应用示例--基于lstm的
```python
# for a sequence inputs
for input in inputs:
  # Step through the sequence one element at a time
  out, hidden = lstm(input, hidden)
```

```python
output, (h_n, c_n) = lstm(input, (h_0, c_0))
```
pytorch是动态图，会随着inputsequence

[源码实现](https://github.com/pytorch/pytorch/blob/master/torch/nn/modules/rnn.py#L346)



## tensorflow的抽象



[示例--基于lstm的语言模型](https://www.tensorflow.org/tutorials/recurrent)

```
lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)
output, state = lstm(words, state) # 这里的输入和输出都是符号，类型是tf.placeholder，lstm参数是tf.variable
```

[BasicLSTMCell源码](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/rnn_cell_impl.py#L476)


## 基于RNN的变形（mainstream variation）

### cell


### cascade rnn


char-rnn + word rnn (Finding Function in Form: Compositional Character Models for Open Vocabulary Word Representation)  
char-cnn + word rnn (Exploring the Limits of Language Modeling)


## sequence labeling

Part-of-speech Tagging


## attention





## rnn new trends



## 未分类

recurrent highway network

## 参考
[The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
