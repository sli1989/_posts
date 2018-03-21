# machine translation

## models

* GNMT
* facebook FAIR在上个月刚祭出state of the art的convseq2seq
* 谷歌全attention机器翻译模型Transformer, WMT en-de和en-fr都刷
到了新的state of the art，而且这次不用RNN，不用CNN，只有attention
*

### end to end


## ideal
- 双向的seq2seq，可实现双向翻译。

-


## codes [常用深度学习工具包]
- pytorch [seq2seq_translation](http://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html)
- tensorflow


## Dataset




|  dataset     |  size | download | homepage | example code  | pretrained_model|  state of art | 备注|
| :-------- | -----:| ----:|--------:|--------:|:--: |
| WMT 2014 Englishto-German translation task  	  | 1.3G (4.5M sent_pair)| [raw]() [processed_stanford](https://nlp.stanford.edu/projects/nmt/data/wmt14.en-de/)| [raw]() [processed_stanford](https://nlp.stanford.edu/projects/nmt/)| Transformer | 无 | - |
| WMT 2014 English-to-French translation task  	  |  |  | | Transformer | 无 | - |
| WMT 2015 English-to-French translation task  	  | 20G  | [download]() | [homepage](http://www.statmt.org/wmt15/translation-task.html) | [tensorflow](models/tutorials/rnn/translate)
| WMT 2015 English-Czech data| 2.7G (15.8M sent_pair)| [raw]() [processed_stanford](https://nlp.stanford.edu/projects/nmt/data/wmt15.en-cs/)| [raw]() [processed_stanford](https://nlp.stanford.edu/projects/nmt/)|
| WMT 2017 | | [download]() | [homepage](http://data.statmt.org/wmt17/translation-task/) |
| IWSLT 2015 English-Vietnamese data | 30M (133K sentence pairs) | [raw]() [processed_stanford](https://nlp.stanford.edu/projects/nmt/data/iwslt15.en-vi/) | [raw]() [processed_stanford](https://nlp.stanford.edu/projects/nmt/)  |
|  IWSLT 2016 GermanEnglish parallel corpus    | 23M | [download](https://wit3.fbk.eu/archive/2016-01//texts/de/en/de-en.tgz) | [homepage]()  | Transformer |   |
|UN parallel corpus en-zh 中英文| 1.2G || [homepage](https://conferences.unite.un.org/UNCorpus/) | [blog](https://www.jianshu.com/p/58ef2b990d3f) | |





## reference


|  模型     |  paper | year + 会议 |   简介|  创新点 | 缺陷| code |
| :-------- | -----:| ----:|------:|--------:|:--: |
|基于短语的翻译（PBMT）||IBM 1989| 模型超复杂|
|  | Sequence to Sequence Learning with Neural Networks | NIPS 2014 | | |  |[tensorflow](https://www.tensorflow.org/tutorials/seq2seq)|
|  | Learning Phrase Representations using RNN Encoder-Decoder for SMT | EMNLP2014 |
||Effective Approaches to Attention-based Neural Machine Translation| EMNLP 2015|基于高斯分布推导了Local Attention,比较了Global Align Attention和Local Align Attention， 和视频处理里面 Soft Attention 和 Hard Attention建立了联系。 |  | | [code](https://nlp.stanford.edu/projects/nmt/)|
|  | Neural machine translation by jointly learning to align and translate | ICLR 2015 | RNN+attention | 首次加入attention，ALIGN AND TRANSLATE |
| GNMT | Google’s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation| 2016|deep_LSTM, residual, attention, converage，subword



## toolbox

汇总

* Giza++ a training tool for IBM Model 1-5 (version for gcc-4) , and extension of Giza
* MGiza++是在Giza++基础上扩充的一中多线程Giza++工具
* Pgiza++是运行在分布式机器上的Giza++工具，使用了MapReduce技术的框架
* Moses, a complete SMT system
* UCAM-SMT, the Cambridge Statistical Machine Translation system
* Phrasal, a toolkit for phrase-based SMT
* cdec, a decoder for syntax-based SMT * Joshua, a decoder for syntax-based SMT
* Jane, decoder for syntax-based SMT
*  Pharaoh a decoder for phrase-based SMT
* Rewrite a decoder for IBM Model 4
* BLEU scoring tool for machine translation evaluation



from http://www.statmt.org/







1. Egypt
    Egypt是在1999年约翰霍普金斯大学统计机器翻译夏季讨论班上，由一些研究人员共同合作开发的统计机器翻译工具包。它包括4个模块：
Whittle：语料库预处理模块；
GIZA：用于从句子对齐的双语语料库中训练词语对齐；
Cairo：词语对齐的可视化工具

   Decoder：解码器，即用来执行具体的翻译过程模块，这一模块没有开放源码。

2.SRILM

   SRILM是一个建立和使用统计语言模型的开源工具包，从1995年开始由SRI 口语技术与研究实验室（SRI Speech Technology and Research Laboratory）开发，现在仍然不断推出新版本，被广泛应用于语音识别、机器翻译等领域。这个工具包包含一组C++类库、一组进行语言模型训练和应用的可执行程序等。利用它可以非常方便地训练和应用语言模型。



0.法老（Pharaoh）系统

    “法老”是较早公开的统计机器翻译系统，是由美国南加州大学信息科学实验室（Information Science Institute）的菲利普.科恩（Philipp Koehn）在2004年做博士论文期间编写的。可能由于较早的开源软件以“埃及（Egypt）”命名的缘故吧，这一系统也采用埃及的代表性事物“法老（Pharaoh）”命名。它是一个基于短语的（Phrased-based）统计机器翻译系统。为此，我们首先要了解一下基于短语的系统的工作原理。
基于短语的方法是目前比较成熟的统计机器翻译技术，它的主要思想是以短语作为翻译的基本单元。给定一个源语言句子，其翻译过程如下：
a． 对源语言句子进行短语划分；
b． 根据翻译模型翻译每个短语；
c． 对短语进行重排序。

“法老”正是基于这一思想的统计机器翻译系统。它包括两大部分；训练和解码。训练过程用来从语料库中获得统计知识。它利用了已有的开源软件GIZA++和SRILM，GIZA++用来训练词语对齐，SRILM训练语言模型。既然是以短语作为翻译的基本单元，因此还需要获得关于短语翻译的知识。通过前面的介绍我们知道通过GIZA++训练可以得到单词对齐，根据单词对齐我们可以进行短语抽取。请注意，这里我们所说的短语是指任意连续的单词串，而不管它是否具有语法意义。








1.   Moses                http://www.statmt.org/moses/
      当今最有名的开源统计机器翻译系统。绝大多数的统计机器翻译技术在Moses中都有支持，比如基于短语的模型、基于句法的模型、各种解码方法、各种特征权重训练方法。概括一下：历史悠久（相对），技术全面，性能出色，论文的baseline。

 “摩西”是“法老”的升级版本，增加了许多功能。它是由英国爱丁堡大学、德国亚琛工业大学等8家单位联合开发的一个基于短语的统计机器翻译系统。来自这8家单位的研究人员于2006年在约翰霍普金斯大学召开了一次研讨会，利用6个星期的时间共同开发了这一系统。整个系统用C++语言写成，从训练到解码完全开放源代码，可以运行在Windows平台和Linux平台。

相比于“法老”，“摩西”主要有如下几个新的特性：

a.使用要素翻译模型（Factored Translation Model）

b.混合网络解码（Confusion Network Decoding）






2.   Joshua                http://joshua-decoder.org/
      继Moses之后推出的开源系统。最开始以层次短语为主，现在也支持句法的模型。Joshua对层次短语模型的实现是最早的（如果不算DavidChiang的python版本），现在来看性能也是最稳定的系统之一。概括一下：层次短语的baseline，性能稳定。


3.   cedc                http://cdec-decoder.org/index.php?title=Main_Page
      CMU开发的一个通用解码器，声称能做许许多多任务（似乎没有不能干的）。不过主要还是用在机器翻译中，基本思想是把问题转化为超图的构建，之后用相对通用的方法在超图上解码。


4    SAMT               http://www.cs.cmu.edu/~zollmann/samt/
      CMU开发的另一套系统（没办法，谁让那边MT的组多，随便就弄出几套系统）。SAMT应该是最早开源出来使用（语言学）句法的翻译系统。而且早期的版本就考虑了hadoop，试想我们2010年以前有几个知道hadoop。


5.   Jane                http://www-i6.informatik.rwth-aachen.de/jane/
      德国亚琛工业大学开发的系统。最早的版本只支持层次短语系统，现在也支持了基于短语的系统。国内用得比较少，不过据说性能还不错。毕竟是机器翻译老牌名校开发，技术成熟。


6.   Phrasal                http://nlp.stanford.edu/phrasal/
      又是名校，Standard的NLP组开发的系统。他里面的基线系统和Moses是一模一样的，其主要特点是支持非连续短语。Java实现，估计对于许多人人来说代码阅读会比较容易。


7.   HiFST                ???
      剑桥大学Speech组开发的统计机器翻译系统。估计很少有人听说过，不过最近可能要开源。这个系统使用有限状态自动机方法来实现层次短语系统，挺cool。性能强劲，从多个任务的BLEU上看，似乎比Joshua要稳定的高一些。


8.   SilkRoad 丝路               http://www.nlp.org.cn/project/project.php?projid=14


中国第一个开源的统计机器翻译系统，“法老”的出现揭开了统计机器翻译的神秘面纱，然而其核心部分解码器的源码仍然没有公开。为此，中国的研究人员联合开发了一个完全开放源代码的统计机器翻译系统“丝路”。该系统由中国的五家研究机构和高校（中科院计算所、中科院自动化所、中科院软件所、厦门大学、哈尔滨工业大学）联合开发，并在2006年中国第二届统计机器翻译研讨会[14]上发布。“丝路”包括以下模块：语料预处理及后处理模块“仙人掌”、词语对齐模块“楼兰”、短语抽取模块“胡杨”、以及三个解码器（“骆驼”、“绿洲”和“商队”）。


说到机器翻译开源就不能不说我们国内多个机构联合开发的丝路系统。从全世界范围来看丝路也是很早的开源系统，对国内机器翻译的研究是个重要的标志。只不过，后期的更新和维护没有跟上，现在使用的似乎不是非常多。


9.   NiuTrans               http://www.nlplab.com/NiuPlan/NiuTrans.html
      不用多说，都懂。NiuTrans的特点是国人开发，性能稳定，翻译模型支持全面，NiuTrans团队对系统进行不断升级，可以提供最及时的技术支持（而且可以汉语交流，这个最重要了）。


从全世界范围来看，现在机器翻译的开源工具不下30个。还有其它的系统，比如Akamon等，还有比较相关的如GIZA++，SRILM等，但是这里就不详细介绍了。



10 GenPar

  GenPar是Generalized Parsing 的缩写。这一工具包实现了一个基于句法的统计机器翻译系统。基于句法的方法将句法结构信息引入到统计机器翻译中来，目前已成为统计机器翻译领域的研究热点。但是构建基于句法的统计机器翻译系统远比构建基于短语的要困难得多，为了让研究者们很快进入这一领域，在JHU2005夏季研讨会上，由纽约大学艾·丹·米拉姆德（I. Dan Melamed）等人组成的统计机器翻译组开发了GenPar.






最后再多说两句：


在所有开源统计机器翻译系统里估计Moses是名声最大的了。写论文大家也都愿意用Moses做baseline，因为比较可靠，评委不会有意见。实际上我觉得Moses的短语系统是非常成功的，甚至可以说是当今最成功的短语系统。如果参加机器翻译评测，使用Moses的短语系统应该是非常保险的。但是，对统计机器翻译的初学者来说，Moses并不非常容易上手。特别是现在的Moses系统极其复杂，代码阅读起来是比较吃力的。如果是想学习统计机器翻译技术，我倒是觉得Joshua和NiuTrans是不错的选择。前者的层次短语系统实现非常巧妙，代码也容易理解；后者的短语系统也非常简单，估计花个一两天就能看懂。相比直接去死扣Moses的代码要容易许多。


再有，在上面提到的这些系统中，我个人认为最有特点的是SAMT和HiFST。SAMT的模型很有特点，甚至可以说作者非常聪明。HiFST也是类似，完全是把FST的精髓使用到了SMT中。虽然这只是个人意见，我还是推荐感兴趣的人可以关注一下这两个系统。


最后还是要说一下。上面所提到的所有系统只是给我们提供了一种搭建机器翻译的平台基础，并不是说有了这些引擎就能随便构建性能优异的翻译系统。影响机器翻译性能的因素有很多，比如，我们使用什么样的数据，多大规模的数据，分词、专名处理模块的性能如何等因素都会影响最终的翻译结果。如果简单的拿这些系统“傻”跑，甚至裸奔，结果不可能太好。开源只是个开始，如果想要真正的高质量翻译，还要用户自身的努力。我敢说，就是PhilippKoehn教授来参加CWMT，如果什么也不调，只是拿Moses裸跑，成绩也肯定不会好
------------------
这些开源工具是不是说只是统计机器翻译最核心的部件? 如果我们自己构建一套真正的统计机器翻译系统，还需要我们自己提供很多东西呢？

没错，通常需要自己提供双语句对数据、训练语言模型的目标语单语数据、源语/目标语分词工具、词对齐工具、源语/目标语句法分析工具（面向句法翻译模型）。但词对齐、分词和句法分析可以采用开源工具来实现。这对于一般用户来说，确实需要附加工作还是很多。

为了缓解这个问题，目前NiuTrans已经提供了分词（自行开发）和词对齐工具（GIZA++），整合在一起，便于用户自行使用自己提供的语料数据来构建统计机器翻译系统。另外，下一步计划提供整合自行开发的句法分析器，基于shift-reduce parsing 算法，分析速度比目前其它开源的工具快很多。这对于大规模双语句对数据处理是很重要的。



1. Egypt
    Egypt是在1999年约翰霍普金斯大学统计机器翻译夏季讨论班上，由一些研究人员共同合作开发的统计机器翻译工具包。它包括4个模块：
􀂄 Whittle：语料库预处理模块；
􀂄 GIZA：用于从句子对齐的双语语料库中训练词语对齐；
􀂄 Cairo：词语对齐的可视化工具

   Decoder：解码器，即用来执行具体的翻译过程模块，这一模块没有开放源码。

2.SRILM

   SRILM是一个建立和使用统计语言模型的开源工具包，从1995年开始由SRI 口语技术与研究实验室（SRI Speech Technology and Research Laboratory）开发，现在仍然不断推出新版本，被广泛应用于语音识别、机器翻译等领域。这个工具包包含一组C++类库、一组进行语言模型训练和应用的可执行程序等。利用它可以非常方便地训练和应用语言模型。


















## 必看

* [重磅 | 谷歌翻译整合神经网络：机器翻译实现颠覆性突破（附论文）][101]
* [重磅 | 谷歌神经机器翻译再突破：实现高质量多语言翻译和zero-shot翻译（附论文）][102]
* [重磅 | Facebook提出全新CNN机器翻译：准确度超越谷歌而且还快九倍（已开源）][103]
Attention Is All You Need


[101]: http://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650719470&idx=1&sn=3368dea980517ea7d7942967da2740dc&chksm=871b0090b06c89863620be4e75c757940d03d8a43cd3c1d9a8309b6594c1bccd769cab193177&scene=21#wechat_redirect
[102]: http://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650720536&idx=2&sn=1617ed96796bba31f4d6c6749b7579db&chksm=871b0d66b06c8470e86bf243fab1b7710dd8b222ecbfa99d5ac61dac07694542e6d4b6846db8&scene=21#wechat_redirect
[103]: http://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650726462&idx=1&sn=144e68df0057ac69002e3927073fc540&chksm=871b2440b06cad565eb98857d057cf8dbb6cbde7786da2ffb676ae76c6246090640591e76572&mpshare=1&scene=23&srcid=0510r21f1gUKWuv7YaLlLLmF##


[401]: https://wit3.fbk.eu/archive/2016-01//texts/de/en/de-en.tgz

##
