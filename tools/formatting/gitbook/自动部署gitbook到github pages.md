



## 采用shell命令

- 参考一：
http://sangsoonam.github.io/2016/08/02/publish-gitbook-to-your-github-pages.html
- 参考二：https://tonydeng.github.io/gitbook-zh/gitbook-howtouse/publish/gitpages.html
- 参考三：http://yangjh.oschina.io/gitbook/UsingPages.html

## 封装成node package

借鉴 hexo deploy命令


## 采用web hook

这是 Github 提供的一种机制，使应用能与 Github 通讯。这种机制实际上就是 Pub/Sub，当 Github 监测到资源（如仓库）有变化就往预先设定的 URL 发送一个 POST 请求（Pub），告知变化情况，而后接收变化的服务器（Sub）即可做一些额外的事情。


这个思路需要有一个服务器并启动一个服务来接收 Github 的请求。这里又有种不同的策略，这两种策略都是基于源码放置在 Github 的前提。第一个是源码将最终文档直接部署在这台服务器上（如使用 Nginx），当接收到 Github 通知直接编译更新到服务器指定的文件夹下即可。另一种策略是当服务器接收到通知后编译更新，而后将编译后的版本提交到 Github 仓库的 gh-pages 分支，让 Github 做 Host。

## 采用git hook


## travis ci
