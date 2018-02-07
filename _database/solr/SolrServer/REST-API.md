
## Introduction


这里指的solr-server提供的rest api

支持的操作： add index update delete retrive query faceting




/select    solr.SearchHandler（后台的类吧？是servlet吗）
/query     solr.SearchHandler
/update
/export    solr.SearchHandler
/browse    solr.SearchHandler
/update/extract  solr.extraction.ExtractingRequestHandler

/delete  solrconfig.xml里没有



对应solr-server的？

core admin



## reference

* solrconfig.xml的RequestHandler模块
* 


## select

select?q=*:*

## dataimport

查看状态
/dataimport

重建索引
/dataimport?command=full-import&clean=false&offset=0&endset=1000000

增量索引
/dataimport?command=delta-import

重新加载配置
/dataimport?command=reload-config

终止一个在运行的操作
/dataimport?command=abort



创建索引库
/admin/cores?action=CREATE&name=collection3&instanceDir=/data/solr/member/example/solr/collection3&config=solrconfig.xml&schema=schema.xml&dataDir=data

加载core
/admin/cores?action=LOAD&core=c6

卸载core
/admin/cores?action=UNLOAD&core=collection2&deleteIndex=true

切换索引库
/admin/cores?action=SWAP&core=core1&other=core1

查看core的信息
/admin/cores?action=STATUS

重新加载core
/admin/cores?action=RELOAD&core=core0

合并core
/admin/cores?action=mergeindexes&core=core0&srcCore=core1&srcCore=core2




提交
/update?commit=true 

根据id删除索引
update/?stream.body=<delete><id>6380736</id></delete>&stream.contentType=text/xml;charset=utf-8&commit=true
删除所有索引
update/?stream.body=<delete><query>*:*</query></delete>&stream.contentType=text/xml;charset=utf-8&commit=true

备份
/replication?command=backup

获得最新的索引版本 
/replication?command=indexversion

让某从服务器不再从主服务器拉取索引
/replication?command=abortfetch  

使某从服务器可以从主服务器拉取修改的索引 
/replication?command=enablepoll 

返回配置和当前状态 
/replication?command=details 

