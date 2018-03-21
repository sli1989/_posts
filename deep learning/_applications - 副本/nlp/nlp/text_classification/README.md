

## 任务

* 短文本分类
* 长文本分类
* 超短文本(一个word)分类


## methods:



- word-level
    - tfidf + svm/lr
    - fastText facebook (只是作为baseline而已)
    - lstm bilstm
    - lstm + attention
    - [cnn](TextCNN)  [code1](TextCNN-code) [code2](TextCNN-code)
    - gated cnn
    - [rcnn](RNN+CNN)

- char-level
    - char的作用？ 见NLP.md
    - char cnn  (Zhang and LeCun, 2015)
    - char rnn
    - char-CRNN (Xiao and Cho, 2016)
    - char-rnn + word rnn (Finding Function in Form: Compositional Character Models for Open Vocabulary Word Representation)  
    - char-cnn + word rnn
- Hierarchical:
    - char + word:
    - word + sentence: [Hierarchical Attention]([RNN+Attention])
    - char + word + sentence:




## datasets &

[IMDB movie reviews]: https://www.kaggle.com/c/word2vec-nlp-tutorial/data  





## paper & implementation

[TextCNN]: Convolutional Neural Networks for Sentence Classification
[TextCNN-code]: https://richliao.github.io/supervised/classification/2016/11/26/textclassifier-convolutional/


[TextRNN]: Recurrent Neural Network for Text Classification with Multi-Task Learning
[TextRNN-code]:

[RNN+Attention]: Hierarchical Attention Networks for Document Classification
http://www.jianshu.com/p/4fbc4939509f
[RNN+Attention-code]: https://richliao.github.io/supervised/classification/2016/12/26/textclassifier-RNN/


[RNN+CNN]: Recurrent Convolutional Neural Networks for Text Classification. AAAI. 2015.
[RNN+CNN-code]: https://github.com/knok/rcnn-text-classification

[fastText]:
* three papers.  https://github.com/facebookresearch/fastText  in C++
    * [1] P. Bojanowski*, E. Grave*, A. Joulin, T. Mikolov, Enriching Word Vectors with Subword Information
    * [2] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, Bag of Tricks for Efficient Text Classification
    * [3] A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, T. Mikolov, FastText.zip: Compressing text classification models
* https://github.com/scharmchi/char-level-cnn-tf
* !!!!!! char-level deep learning  https://offbit.github.io/how-to-read/    https://github.com/offbit/char-models






## tutorial & survey & blog

http://www.jeyzhang.com/cnn-apply-on-modelling-sentence.html
https://zhuanlan.zhihu.com/p/25928551


## web service

    1. watson NLC: https://www.ibm.com/watson/developercloud/natural-language-classifier/api/v1
    2. songfang NLC
