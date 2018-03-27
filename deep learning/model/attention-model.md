---
title:  seq2seq里的 attention机制 的 原理 及 代码
---

seq2seq缺陷：无论之前的context有多长，包含多少信息量，最终都要被压缩成一个几百维的vector。这意味着context越大，最终的state vector会丢失越多的信息。

Attention based model的核心思想: 一个模型完全可以在decode的过程中利用context的全部信息，而不仅仅是最后一个state。




### global attention


### local attention



## 参考
[知乎](https://www.zhihu.com/question/36591394)
[注意力机制和PyTorch实现机器翻译](https://plmsmile.github.io/2017/10/12/Attention-based-NMT/)
