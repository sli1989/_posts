---
title: Webpack
---

# 简介

Webpack这个工具可以将你的所有代码和可选择地将依赖捆绑成一个单独
的 .js 文件。


# 安装

```sh
# 全局安装webpack
$ npm install -g webpack

# webpack 已经将 webpack 命令行相关的内容都迁移到 webpack-cli，所以除了 webpack 外，我们还需要安装 webpack-cli：
$ npm install webpack-cli -D -g

# 查看版本
$ npx webpack --version
```

# 配置文件

根目录下新建`webpack.config.js`

webpack


# 打包

```sh
$ sh
```


 webpack 4 引入的，有俩种模式，development 与 production，默认为 production - 其实还有一个隐藏的 none 模式


# Webpack的核心原理

1. 一切皆模块<br>
正如js文件可以是一个“模块（module）”一样，其他的（如css、image或html）文件也可视作模 块。因此，你可以require('myJSfile.js')亦可以require('myCSSfile.css')。这意味着我们可以将事物（业务）分割成更小的易于管理的片段，从而达到重复利用等的目的。
1. 按需加载<br>
传统的模块打包工具（module bundlers）最终将所有的模块编译生成一个庞大的bundle.js文件。但是在真实的app里边，“bundle.js”文件可能有10M到15M之大可能会导致应用一直处于加载中状态。因此Webpack使用许多特性来分割代码然后生成多个“bundle”文件，而且异步加载部分代码以实现按需加载。

# 参考

https://github.com/chemdemo/chemdemo.github.io/issues/13
