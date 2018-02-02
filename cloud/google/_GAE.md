
## GAE简介

- PaaS: Platform-as-a-Service（平台即服务）
- GAE支持Node.js java python PHP Go Ruby
- 浏览器访问google，需要用翻墙（我用的代理）
- 但是本地开发，需要Google Cloud SDK。而且需要连接google cloud。需要vpn了。（囧）
那就本地开发，把代码上传到git，然后clone到GAE



## GAE的云端shell

### 配置&默认环境
- Debian GNU/Linux 8
- 10G硬盘(可用3.2G) 2G内存
- python2.7
- OpenJDK 1.7
- 我勒个草，GAE是提供的SaaS还是IaaS？
-

## 搭建pyton应用

- yaml

git clone https://github.com/GoogleCloudPlatform/appengine-try-python-flask.git $TUTORIALDIR

测试应用使用了 Flask  Web 框架。

- 部署应用 gcloud app deploy app.yaml --project my-first-project-164507
Deploying to URL: [https://my-first-project-164507.appspot.com
- 部署完后，就能直接访问url了

### 本地应用开发

- 下载 Google Cloud SDK 并在本地进行开发

- 构建您的下一个应用：了解如何将 App 引擎与其他云端平台产品结合使用




## java
使用 App Engine Maven 插件将一个示例 Java  应用部署至 Google App 引擎

- src/main/webapp/WEB-INF/appengine-web.xml 文件即web app中的web.xml文件
- 采用的jetty作为web server
- git clone https://github.com/GoogleCloudPlatform/appengine-try-java.git $TUTORIALDIR

- mvn appengine:run  编译，测试应用，能够本地预览了
- mvn appengine:deploy 部署应用
https://my-first-project-java-164508.appspot.com/


### 编程指南

/home/acmcqu087378/src/xu-song/java_gae_quickstart-2017-04-13-19-54/target/appengine-try-java-1.0
/home/acmcqu087378/src/xu-song/java_gae_quickstart-2017-04-13-19-54/target/appengine-try-java-1.0/WEB-INF/classes/



## 免费

- 配额每 24 小时重置一次
- 前端实例使用小时数	 0.25 实例小时（上限为 28 实例小时）
- 传出带宽	         0.000089 GB（上限为 1 GB）
- 云端存储A类操作次数  0（上限为 0.02）

- 注册免费试用，即可获得 300 美元的赠金，并可在 12 个月内试用 Google 云端平台提供的所有功能


### 免费版限制:
如果不花钱的话……
socket模块无法使用。也就是说，凡是用到import socket的东西都会出错。
每天流量1GB，北京时间下午4点重置。urlfetch每分钟22M，传入传出带宽每分钟56M……所以GoAgent翻墙会有流量限制，而且这并不应当由GoAgent背锅。
详细的资源限制可以到GAE控制面板的“配额”哪里查看。


### 功能支持

- 网址抓取（URL Fetch）：访问互联网上的资源，抓取检索数据。
- 邮件（Mail）： GAE可以利用基于Gmail的基础设施来发送电子邮件。
- Memcache缓存：高性能的内存缓存保障，对于那些不需要持久性存储和事务功能的数据（例如临时数据或从数据存储区复制到缓存以进行高速访问的数据）很有用。
- 图像操作（Image Manipulation）：使用该 API，您可以对 JPEG 和 PNG 格式的图像进行缩放、裁剪、旋转和翻转，还能使用预先定义的算法提升图片的质量。
- 计划任务和任务队列（Scheduled Tasks & Task Queues）：允许将任务计划为按指定间隔运行，这些任务通常称为Cron job。另外可以通过在一个队列插入任务（以Web Hook的形式）来实现后台处理，GAE会根据调度方面的设置来安排这个队列里面的任务执行。


### GAE新的收费模式——process-instance-hour

同AWS（Amazon Web Services）相比，GAE按照的是process-instance-hour收费模式，而AWS则是按照machine-instance-hour收费。这一点对开发人员相当重要，在AWS里，可以并行运行几十个进程，而在GAE中，当进程在等待I/O传输的过程中仍在收取费用。

这也意味着，在对支持的语言进行编译时，更少的CPU消耗时间等于更少的钱。但同时也意味着，运行多个进程等待的时间更长，收取的费用更高，对于Python开发者而言，这绝对不是一个好消息，因为Python开发往往需要多线程处理多个Web请求。从这个角度来看，GAE每个进程实例每小时0.08美元的收费要比AWS机器为实例0.085美元的收费似乎更为昂贵。

## 成功案例：
适用于搭一些
- 已经成功搭了一个html游戏 https://xu-song.appspot.com/games/towerdefense/
- 做一个online word2vec(中英文) &&  online-doc2vec
- 做一个online ocr
- 做一个online image caption/classification
- 做一个online NLC 情感分析 QA
- 做一个online crawler
- 做一个online 提醒，（提醒备忘录，提醒股票买卖，提醒生日，提醒天气预报）
- 做一个反向代理，入口为https://xu-song.appspot.com/。/pythonapp/代理到python的web服务，javaapp/代理到java后台服务。
- 做一个online alphago
- 做一个online德州扑克（开源没）

### 经常访问的站点，不要放在GAE，耗流量
比如博客，gitlab服务，


## 其他
