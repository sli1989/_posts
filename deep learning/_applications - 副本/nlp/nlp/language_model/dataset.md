##  enwik8 & text8

### 简介
- enwiki8是从wikipedia上扒下来的前100，000，000个字符。最早是用来做文本压缩的。
- text8是enwiki8的clean text


* all from [Matt Mahoney's page](http://mattmahoney.net/dc/textdata.html)
* [enwik8.zip download](http://mattmahoney.net/dc/enwik8.zip)
* [text8.zip download](http://mattmahoney.net/dc/text8.zip )



### 格式：


    enwik8 （复杂格式）
	'''Anarchism''' originated as a term of abuse first used against early [[working class]] [[radical]]s including the [[Diggers]] of the [[English Revolution]] and the [[sans-culotte|''sans-culottes'']] of the [[French Revolution]].[http://uk.encarta.msn.com/encyclopedia_761568770/Anarchism.html] Whilst the term is still used in a pejorative way to describe ''&quot;

    text8 (1行，10^8个字符)
	 anarchism originated as a term of abuse first used against early working class radicals including the diggers of the english revolution and the sans culottes of the ....


| text8 | all_size | vocab_size | 
| :---- | --------:| :--: |
| 95M | dd | 71290  + UNK (tensorflow显示的) |


**预处理:** (enwik8-->text8)

* 只包含27种字符：小写的从a到z，以及空格符
* 大写字符 --> 小写字符，
* 数字 --> 对应的英语单词

比如：’s也换成了空格+s  e.g被处理成了e g

### used in
* [google word2vec](https://code.google.com/archive/p/word2vec/)
* [tensorflow/word2vec](https://www.tensorflow.org/tutorials/word2vec)








------------


## Latest Wikipedia dump


##



## ptb

ptb.train.txt