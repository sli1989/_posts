

## 简介



### src的github目录

* solr/    编译后只剩下个solr-core-5.4.0.jar
* lucene/   编译后剩下个很多lucene包
* dev-tools/
* build.xml
* README.txt



## 主要交互接口是handler

* /select  [SearchHandler](http://wiki.apache.org/solr/SearchHandler)
* /query  SearchHandler
* /export  SearchHandler
* /browse  SearchHandler
* /update/extract  [solr.extraction.ExtractingRequestHandler]


## 流程

* 发送/select请求
* 该请求由SolrRequestFilter(见web.xml)捕获并分配给SearchHandler(solrconfig.xml)
* 



## how to deploy solr project in eclipse

* solr in action附录一



## 问题

* 根据query，后台如何计算出score的？
* 如何highlight的？
* query能否得到





