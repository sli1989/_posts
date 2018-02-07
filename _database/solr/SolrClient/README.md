## Introduction

httprequest是solrclient的核心，万变不离其宗。

* solr-web-html
* curl
* solrj
* pysolr
* solrPHP



客户端使用 Solr 的五个基本操作来使用 Solr。这些操作有查询、索引、删除、提交和优化。

/select
/update
/delete
/

API

* /select  [SearchHandler](http://wiki.apache.org/solr/SearchHandler)
* /query  SearchHandler
* /export  SearchHandler
* /browse  SearchHandler
* /update/extract  [




################# httpclient
HttpRequestBase
	HttpGet
	HttpEntityEnclosingRequestBase
		HttpPost
	HttpDelete, 
	
	 
	HttpHead, 
	HttpOptions, 
	HttpTrace



## 问题集

### solr的/query和/select有什么区别？

- /query是页面，调用的solr/tpl/query.html
- /select是api，执行query的时候调用的/select api

### 