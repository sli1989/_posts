---
title: Gitbook自动化部署到Github Pages的方案汇总
date: 2018-03-20
tags: ["travis-ci","自动化部署","持续集成","gitbook"]
---



## 采用shell命令

- 参考一：
http://sangsoonam.github.io/2016/08/02/publish-gitbook-to-your-github-pages.html
- 参考二：https://tonydeng.github.io/gitbook-zh/gitbook-howtouse/publish/gitpages.html
- 参考三：http://yangjh.oschina.io/gitbook/UsingPages.html

## 封装成node module

借鉴 hexo deploy命令


## 采用web hook

这是 Github 提供的一种机制，使应用能与 Github 通讯。这种机制实际上就是 Pub/Sub，当 Github 监测到资源（如仓库）有变化就往预先设定的 URL 发送一个 POST 请求（Pub），告知变化情况，而后接收变化的服务器（Sub）即可做一些额外的事情。


这个思路需要有一个服务器并启动一个服务来接收 Github 的请求。这里又有种不同的策略，这两种策略都是基于源码放置在 Github 的前提。第一个是源码将最终文档直接部署在这台服务器上（如使用 Nginx），当接收到 Github 通知直接编译更新到服务器指定的文件夹下即可。另一种策略是当服务器接收到通知后编译更新，而后将编译后的版本提交到 Github 仓库的 gh-pages 分支，让 Github 做 Host。

## 采用git hook

貌似必须要自己搭建git server。


## CI工具

持续集成（英语：Continuous integration，缩写CI）是一种软件工程流程，是将所有软件工程师对于软件的工作副本持续集成到共用主线（mainline）的一种举措。
持续集成的提出主要是为解决软件进行系统集成时面临的各项问题，极限编程称这些问题为集成地狱（integration hell）。

常用工具 travis-ci  Jenkins


Jenkins是一个持续集成工具，相当于一个构建调度平台，围绕着scm，ssh, ant,maven插件，进行构建操作。
理论上来讲，有合适的插件，大部分自动化行为都可以在jenkins平台上展开。
使用Jenkins 来触发和调度，在Jenkins构建执行shell脚本来进行分发和安装，测试，可以部署成流水线的方式，依次运行






已实现
