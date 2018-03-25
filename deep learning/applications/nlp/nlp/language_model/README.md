




## language model

语言模型经常使用在许多自然语言处理方面的应用，如语音识别，机器翻译，词性标注，句法分析和资讯检索。由于字词与句子都是任意组合的长度，因此在训练过的语言模型中会出现未曾出现的字串(资料稀疏的问题)，也使得在语料库中估算字串的概率变得很困难，这也是要使用近似的平滑n元语法(N-gram)模型之原因。
在语音辨识和在资料压缩的领域中，这种模式试图捕捉语言的特性，并预测在语音串列中的下一个字。



## 大方向
* Context-dependent Language Model 


## 常用方法
- HMM
- n-gram
- LSTM 同时学习了language model和word embedding。疑问：lstm学习的embedding怎么样？



## char-level

* char-rnn + word rnn
    * Finding Function in Form: Compositional Character Models for Open Vocabulary Word Representation 2015

* char-cnn + word rnn
    * 
    * Character-Aware Neural Language Models 2015 (with highway)
    * Exploring the Limits of Language Modeling 2016




Character-Aware Neural Language Models

## idea
###  为什么只以预测next word为目标，而不采用前后context填词？

**背景:**

采用前后context的有：word2vec(用来学习embedding)

**思路:** 很简单，left word right
优化目标改为 left-->word & right-->word。

**关键词:**
* bidirectional lstm for language model