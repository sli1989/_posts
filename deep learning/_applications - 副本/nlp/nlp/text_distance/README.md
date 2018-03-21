## Introduction

text similarity or distance



##

similarity = representation + metric



## representation

见text representation.md

## metric
见metric




## models

* 欧氏距离
* cosine距离
    * cosine-bow
    * cosine-tfidf
    * cosine-docEmbedding
* wmd.. ICML 2015
    * 核心： distance = EMD(BOW1,BOW2,word-distance)
    * 优点：
        * BOW作为doc-representation
        * 如果word-distance矩阵为0-1矩阵，是不是等同某个metric？
        * 
    * 缺陷：无序。改进：
        * 用word_binding，词组，句子 来增强BOW，即扩充词典。怎样来word-binding呢？词组数目会指数膨胀吧？
        * cnn
        * spatial pyramid pooling + 
    * 其他
        * 用tfidf代替BOW应该更好，因为能够降低stop-word的权重，以及高df word的权重

* rwmd

