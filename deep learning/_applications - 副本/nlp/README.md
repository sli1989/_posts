
## basic: representation

1. word-representation:
    * one-hot
    * embedding
    	* word2vec
    	* glove
    	* rnn language-mode
2. text-representation:
    * BOW
    * tf-idf
    * word-sequ


## task




text1 --> text2  机器翻译



| input->output      |    任务 | 场景  | Methods | loss function |
| :-------- | --------:| --------:| --------:|  :--: |
| text  | 语言模型 |  作诗，写歌，输入法| HMM,RNN, | |
| text  | word2vec |  | | |
| [text->label](nlp/text_classification)  | 文本分类 |  情感分析   | | |
| [text1+text2->label](nlp/text_match)     |  text_match,paraphrase,relationship_extraction,text_similarity |  Document_Retrieval, 搜索引擎 | |
| text+image->label     |   text_image_match，multi_modal  |   | |
| text1->text2  |     | translation,reasoning/NLI/entailment,摘要summary  | | |
| image->text   |   image caption  |   | |


leanring to match


## 根据方法分类

## word-level





## char-level

### 用法

** char 直接用 **

** char embedding **
为什么要embedding？


### 缺陷
- word-level lstm生成的句子，可能不是
- word-level的依赖是不是变差了。

### idea
char-enhanced word-lstm
char-enhanced word2vec


### 类比

- char level 之所以work，是因为word设计(用char组成word)的时候具有一定的合理性。比如
- 中文不用分词，
- 中文笔画级别
- 图像pixel-level


## idea

paper & patent !!!

### pixel embedding
- gray embedding （256）
- RGB embedding （256×256×256）
- Bucketization embedding （bucket_size）

**why embedding**
pixel is more than single value, it has its meaning.

### reference
- pixel level generation?
- pixel rnn


## toolbox design pattern
- 模块化，去耦合
-
