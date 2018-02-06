## 格式

mobi, azw, azw3, epub 这几种电子书格式从本质上来说都是从 HTML 文档转换而来，大多数 HTML 标签和 CSS 样式表的特性它们都支持，它们之间的主要区别在于对排版及新特性的支持与否上。

calibre只能编辑epub和azw3格式书籍。

 格式转换工具：Calibre 

## pdf
优点，编辑方便，
 缺点：

## epub
epub实际上就是一个html的打包，里面的内容都是由html来进行排版，由CSS控制样式的。因此制作epub和制作网页没有太多的区别。
epub是开源格式

 

 

## mobi：

amazon的格式，.mobi是压缩包，里面主要包含html和资源文件


mobi是良心格式啊，能转化为htmlz。（是工具提供的还是）


### 编辑mobi
* 方式一：转化为epub
	转化为epub, 然后通过sigil或jutoh修改，之后用calibre转为mobi
* 方式二：转化为html
	转化为htmlz，解压缩，




## 格式转换 信息丢失

* 转化原理，格式A--html--格式b。如果转化成

* azw3是升级版的mobi，转换成 mobi 后会产生丢失格式的问题

* pdf信息量最少(比如换行)，所以不要拿pdf当做转换源



## 做笔记

* 方式一：在pdf中做笔记
	* 优势：做笔记方便，
	* 缺陷：pdf格式不易于操作，不易于读写
* 方式二：在html中，利用canvas做笔记。 不影响html源码，只是添加了一堆js
	* 优势：做笔记方便，
	* 缺陷：
* 方式三：在html中，利用标签做笔记。
	* 优势：style可以自定义。
	* 缺陷：图形的笔记不好做。

最推荐利用方式三