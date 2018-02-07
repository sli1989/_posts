
## solrj

solrj核心就是调用的solr-server提供的restapi。

使用SolrJ操作Solr会比利用httpClient来操作Solr要简单。SolrJ是封装了httpClient方法，来操作solr的API的。SolrJ底层还是通过使用httpClient中的方法来完成Solr的操作。 


## SolrClient

SolrClient 是一个抽象类，因此要连接到一个远程Solr实例，你需要创建一个 HttpSolrClient 或 CloudSolrClient 的实例。 
它们都通过 HTTP 来和 Solr 交流。然后你可以发送 SolrRequest 或 SolrQuery 并获取 SolrResponse

### HttpSolrClient
	单节点 Solr 客户端
### ConcurrentUpdateSolrClient 
	当实现一个将会一次性批量加载大量文档的 java 应用时，应该考虑使用 ConcurrentUpdateSolrClient 来替代 HttpSolrClient。 ConcurrentUpdateSolrClient 会缓冲所有被添加的文档并将它们写到开启的 HTTP 连接中。 这个类是线程安全的。 尽管任何 SolrClient 请求都可以通过该实现完成， 我们通常推荐仅将 ConcurrentUpdateSolrClient 用在 /update 上。

### CloudSolrClient SolrCloud 客户端

### LBHttpSolrClient

## SolrQuery
	
	
## SolrRequest
process操作

	AbstractUpdateRequest
		ContentStreamUpdateRequest
		UpdateRequest
		如果是add操作，UpdateRequest包含所需add的doc
	CollectionAdminRequest
	CoreAdminRequest
	DirectXmlRequest
	DocumentAnalysisRequest
	FieldAnalysisRequest
	GenericSolrRequest
	LukeRequest
	QueryRequest
	SolrPing
	
	
## SolrResponse
	SimpleSolrResponse
	SolrResponseBase




## add 操作


    DefaultClientConnectionOperator.openConnection(OperatedClientConnection, HttpHost, InetAddress, HttpContext, HttpParams) line: 168	
    ManagedClientConnectionImpl.open(HttpRoute, HttpContext, HttpParams) line: 304	
    DefaultRequestDirector.tryConnect(RoutedRequest, HttpContext) line: 611	
    DefaultRequestDirector.execute(HttpHost, HttpRequest, HttpContext) line: 446	
    SystemDefaultHttpClient(AbstractHttpClient).doExecute(HttpHost, HttpRequest, HttpContext) line: 882	
    SystemDefaultHttpClient(CloseableHttpClient).execute(HttpUriRequest, HttpContext) line: 82	
    SystemDefaultHttpClient(CloseableHttpClient).execute(HttpUriRequest) line: 107	
    SystemDefaultHttpClient(CloseableHttpClient).execute(HttpUriRequest) line: 55	
    HttpSolrClient.executeMethod(HttpRequestBase, ResponseParser) line: 480	
    HttpSolrClient.request(SolrRequest, ResponseParser, String) line: 241	
    HttpSolrClient.request(SolrRequest, String) line: 230	
    UpdateRequest(SolrRequest<T>).process(SolrClient, String) line: 150	
    HttpSolrClient(SolrClient).add(String, SolrInputDocument, int) line: 174	
    HttpSolrClient(SolrClient).add(String, SolrInputDocument) line: 139	
    HttpSolrClient(SolrClient).add(SolrInputDocument) line: 153	
    ClauseSolr.main(String[]) line: 44	



## soft VS hard commit
参考 zotero/conf-core/solrconfig.xml.pdf
