
## Introduction



## 分类

* one-hot representation
    * 容易受维数灾难的困扰
    * 不能很好地刻画词与词之间的相似性
* distributed representation (也叫word embedding)
    * word2vec: 最快
    * GloVe
    * FastText:训练相对比较慢 
    * WordRank


## word distance

* embedding distance
* edit distance，编辑距离体现character级别的信息。


## idea

* enriching word vector with character information
    * 采用cnn
    * 采用rnn
    * 采用编辑距离 约束




## 主要方向

* semantic-level:
    * HMM: 
    * lstm: 前面context 重构后面
        * supervised lstm for embedding
    * bi-lstm:
    * word2vec: 前后context 重构中间。并强制遵循向量加减法。（有点类似RBM到autoencoder，挺好）
        * supervised word2vec

* char-level:
    * 比如fatherland-father-land, beautiful-beauty, 北京电影学院-北影

* context-based:
	* 不同上下文，具有不同的含义

* 采用multichannel
    * 一个channel采用word2vec学习到的embedding
    * 一个channel采用charCNN学习到的embedding
    * 一个channel采用自变量(类似cnn_for_text_classification)





## 原理
见paper & zotero

## idea


## pretrained w2v
* [fastText](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md) 294 languages, trained on **Wikipedia** using fastText.
* [w2v-api](https://github.com/3Top/word2vec-api#where-to-get-a-pretrained-models)

## eval
见
https://bitbucket.org/song_xu/word2vec-evaluation/src


## code

### training

* c 
    * [official](https://github.com/dav/word2vec)

* python
    * [tensorflow](https://github.com/tensorflow/models/tree/master/tutorials/embedding)
    * [theano]
    * [gensim]

* java

### IO & service

* python
    * [word2vec-api](https://github.com/3Top/word2vec-api#where-to-get-a-pretrained-models)

* java
    * [load model](https://gist.github.com/ansjsun/6304960)




## 实验结果

tensorflow word2vec结果



	I word2vec_kernels.cc:200] Data file: text8 contains 100000000 bytes, 17005207 words, 253854 unique words, 71290 unique frequent words.
	Data file:  text8
	Vocab size:  71290  + UNK
	Words per epoch:  17005207
	Eval analogy file:  questions-words.txt
	Questions:  17827
	Skipped:  1717
	Epoch    1 Step   150984: lr = 0.024 words/sec =    60987
	Eval 1495/17827 accuracy =  8.4%
	Epoch    2 Step   301985: lr = 0.023 words/sec =     4728
	Eval 2414/17827 accuracy = 13.5%
	Epoch    3 Step   452967: lr = 0.021 words/sec =    32599
	Eval 3073/17827 accuracy = 17.2%
	Epoch    4 Step   603916: lr = 0.020 words/sec =    18969
	Eval 3536/17827 accuracy = 19.8%
	Epoch    5 Step   754822: lr = 0.019 words/sec =     9619
	Eval 4034/17827 accuracy = 22.6%
	Epoch    6 Step   905765: lr = 0.018 words/sec =     1897
	Eval 4466/17827 accuracy = 25.1%
	Epoch    7 Step  1056711: lr = 0.016 words/sec =     1001
	Eval 4731/17827 accuracy = 26.5%
	Epoch    8 Step  1207666: lr = 0.015 words/sec =    16715
	Eval 4963/17827 accuracy = 27.8%
	Epoch    9 Step  1358605: lr = 0.014 words/sec =    23958
	Eval 5293/17827 accuracy = 29.7%
	Epoch   10 Step  1509587: lr = 0.013 words/sec =    28068
	Eval 5465/17827 accuracy = 30.7%
	Epoch   11 Step  1660544: lr = 0.011 words/sec =    36671
	Eval 5738/17827 accuracy = 32.2%
	Epoch   12 Step  1811515: lr = 0.010 words/sec =    51473
	Eval 5888/17827 accuracy = 33.0%
	Epoch   13 Step  1962487: lr = 0.009 words/sec =    64456
	Eval 6033/17827 accuracy = 33.8%
	Epoch   14 Step  2113465: lr = 0.008 words/sec =    48950
	Eval 6260/17827 accuracy = 35.1%
	Epoch   15 Step  2264436: lr = 0.006 words/sec =    48388
	Eval 6404/17827 accuracy = 35.9%



tensorflow language_model结果


