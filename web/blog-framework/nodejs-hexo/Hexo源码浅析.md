---
title: Hexo源码系列 之 入门
keywords:
  - hexo
  - 源码
tags:
  - hexo
  - 源码
categories:
  - web
  - blog-framework
  - nodejs-hexo
abbrlink: 70d0eddc
date: 2018-01-25 03:08:53
---

# 首先

为什么要看源码呢？因为想自己更便捷高效的管理博客，比如
- 如何更新Hexo。(需要看`hexo init`的源码，因为该命令隐藏了`hexo-starter`项目)
- 如何更新theme。某些bug-fix&新功能。(需要借助git的submodule来高效管理)
- 如何自己实现一个新功能(比如添加edit button，添加URL哈希。需要了解模板原理)


源码不用细看，看个大概能满足自己的需求就够了。

本文仅介绍[Hexo基础包](https://github.com/hexojs/hexo-starter)，[扩展包](hexo.io/plugins)可参考【Hexo插件系列】博客。

# 查看Hexo和Plugin版本


首先看一下自己的Hexo和Plugin版本，因为不同的版本是不同的实现。版本号是次要的，主要看是不是同一种包。比如`hexo-deployer-git`和`hexo-deployer-rsync`在执行`hexo d`命令时方式就不同。详见[官方文档](https://hexo.io/docs/deployment.html)

查看`package.json`文件的依赖项。
```yml
"dependencies": {
  "hexo": "^3.7.0", # https://github.com/hexojs/hexo/  hexo仅仅是一个module而已，用于...
  "hexo-generator-archive": "^0.1.5",  # generator最复杂
  "hexo-generator-category": "^0.1.3",
  "hexo-generator-index": "^0.2.1",
  "hexo-generator-tag": "^0.2.0", # nodejs的模板引擎，有EJS、Jade、Swig、Haml。theme-next采用的swig
  "hexo-renderer-ejs": "^0.3.1",
  "hexo-renderer-stylus": "^0.3.3",
  "hexo-renderer-marked": "^0.3.2",  # markdown的render engine，即`.md`转`html`
  "hexo-server": "^0.3.1"
}
```
也可用以下命令查看版本：
```sh
$ npm ls --depth 0
```

> 更新各个模块，命令 npm update

- hexo-cli，
  - 提供hexo init、hexo help、hexo version命令
- hexo
  - hexo new
  - hexo generate
- hexo plugin，即node依赖
  - hexo server
  - hexo deploy
  - 其他命令

# 回顾Hexo搭建流程

以下来自[官方文档](https://github.com/hexojs/hexo/blob/master/README.md)


```sh
# 1. Installation
$ npm install hexo-cli -g

# 2. Setup your blog
$ hexo init blog
$ cd blog

# 3. Start the server
$ hexo server

# 4. Create a new post
$ hexo new "Hello Hexo"

# 5. Generate static files
$ hexo generate
```


# 流程详解

## 1. npm install

npm是nodejs的包管理器，管理javascript lib
hexo-cli是nodejs的一个包，用于运行hexo命令。(有cli难道还有server？)

npm list -g 能够看到安装路径。一般在/usr/lib/node_modules/ 或者/usr/local/lib/node_modules/

## 2. hexo init
`hexo init`命令做了什么？
### 答案
`hexo init`等价于以下两行shell命令。
```sh
# 1. Cloning hexo-starter to blog
$ git clone --recursive https://github.com/hexojs/hexo-starter.git blog
# 2. Install dependencies
$ npm install --production
```

看到这里，就够用。如果自己的hexo项目是老版本的，可以在这个仓库pull更新(虽然更新很少)。
如果对追寻答案的过程感兴趣，可以继续往下看。

### 追寻答案的旅程 - optional

**首先看一下hexo**

```sh
$ which hexo
/usr/bin/hexo

$ cat /usr/bin/hexo
#!/usr/bin/env node
'use strict';
require('../lib/hexo')();
```


这里你会发现，hexo命令是nodejs脚本。 `../lib/hexo`对应的是`usr/lib/hexo`，然而没有path。

```sh
$ ls -l /usr/bin/hexo
 /usr/bin/hexo -> ../lib/node_modules/hexo-cli/bin/hexo
```

原来`/usr/bin/hexo`是个符号链接，链接到nodejs的modules目录里。

```sh
$ cat /usr/lib/node_modules/hexo-cli/bin/hexo
#!/usr/bin/env node
'use strict';
require('../lib/hexo')();
```

即`hexo`命令对应的是`/usr/lib/node_modules/hexo-cli/lib/hexo.js`文件。


hexo找到了，init命令呢？讲道理应该是个package.json下的script。

原生`hexo-cli`提供了4个命令，都在`hexo-cli/lib/console`路径下。

```
$ hexo help
$ hexo init
$ hexo version
$ hexo index
```

扩展命令通过`hexo-cli/lib/extends.console.js`实现。


**hexo init 命令**


**`init.js`核心代码**

路径`hexo-cli/lib/console/init.js`

```js
var GIT_REPO_URL = 'https://github.com/hexojs/hexo-starter.git';
// 1. git clone --recursive https://github.com/hexojs/hexo-starter.git blog
log.info('Cloning hexo-starter to'
spawn('git', ['clone', '--recursive', GIT_REPO_URL, target]);
removeGitDir(target);
removeGitModules(target);
// 2. npm install --production
log.info('Install dependencies');
spawn(npmCommand, ['install', '--production']);
```

实际上吧，如果hexo的log打印出来`GIT_REPO_URL`就更清晰，非要藏起来等人挖掘。


**参考**

- [hexo-starter项目](https://github.com/hexojs/hexo-starter)
- [hexo.js源码 | hexo-cli 项目](https://github.com/hexojs/hexo-cli/blob/master/lib/hexo.js)
- [hexo init 命令源码 | hexo-cli 项目](https://github.com/hexojs/hexo-cli/blob/master/lib/console/init.js)

## 3. hexo server

这个不属于hexo-cli了。
[hexo server命令源码](https://github.com/hexojs/hexo-server/blob/master/lib/server.js)

暂没兴趣，应该就是启了个nodejs HttpServer。待看

- 额外的逻辑是，如果没generate，先调一下 hexo g

但是偶尔出现的bug来源于`hexo s`，这里的逻辑还需要看一下。


## 4. hexo new



## 5. hexo generate

生成器（Generator）[官方文档](https://hexo.io/zh-cn/api/generator.html)

这个好麻烦，看不动了。这么多`generator`和`render`。

放个链接 https://github.com/hexojs/hexo-generator-index ，貌似主要先看这个。


### generator

generates static files

### render 模板引擎

[官方文档](https://hexo.io/zh-cn/api/renderer.html)

https://hexo.io/zh-cn/api/rendering.html

模板引擎的作用，就是将界面与数据分离。最简单的原理是将模板内容中指定的地方替换成数据，实现业务代码与逻辑代码分离。


生成静态文件。将我们的数据和界面相结合生成静态文件的过程。会遍历主题文件中的 source 文件夹（js、css、img 等静态资源），然后建立索引，然后根据索引生成 pubild 文件夹中，此时的 publid 文件是由 html、 js、css、img 建立的纯静态文件可以通过 index.html 作为入口访问你的博客。


其中 _layout.swig 是通用模板，里面引入了 head、footer 等公共组件，然后在其他的模板中会引入这个 _layout.swig 通用模板，比如 post.swig 模板


- .md解析成html
- .swig渲染为html

### 数据的填充

数据的填充主要是 hexo -g 的时候将数据传递给 swig 模板，然后再由 swig 模板填充到 HTML 中。



## 6. hexo deploy
deploy到底干了什么？执行了git push？

deploy配置
```yml
# Deployment
## Docs: https://hexo.io/docs/deployment.html
deploy:
- type: git
  repo: git@github.com:xu-song/xu-song.github.io.git
  branch: master
```

部署主要是根据在 _config.yml 中配置的 git 仓库或者 coding 的地址，将 public 文件上传至 github 或者 coding 中。然后再根据上面的 github 提供的 pages 服务呈现出页面。当然你也可以直接将你生成的 public 文件上传至你自己的服务器上。

**deploy.js核心源码**：https://github.com/hexojs/hexo-deployer-git/blob/master/lib/deployer.js#L83
```js
git('add', '-A');  // 对publc目录中执行add操作。
git('commit', '-m', message);
git('push', '-u', repo.url, 'HEAD:' + repo.branch, '--force');
```
即等价于以下几个命令(通常情况下)
```sh
$ rm -rf .deploy_git  # log.info('Clearing .deploy_git folder...');
$ cp -rf public .deploy_git # log.info('Copying files from public folder...');
$ cd .deploy_git

$ git add -A
$ git commit -m "Site updated: 2018-01-30 *:*:*" #某时间
$ git push -u origin HEAD:master --force
```

上面命令使用--force选项，强制push到远程主机，会使远程主机更新的版本被覆盖。所以不要在deploy之后的仓库做提交，要在dev仓库提交。

实例：
- [x] [Dev Repository](https://github.com/xsung/blog-dev/#submodule) Main project for all submodules
- [x] [Deployed Repository](https://github.com/xu-song/xu-song.github.io/) is deployed by Hexo from `Dev Repository`
- [x] [Demo Site](http://xusong.vip) hosts the `Deployed Repository`




**参考**

- [hexo deploy官方文档](https://hexo.io/docs/deployment.html)
- [hexo deploy.js源码](https://github.com/hexojs/hexo-deployer-git/blob/master/lib/deployer.js)
- http://cherryblog.site/hexo-4.html
- [深入理解 Hexo](http://cherryblog.site/hexo-4.html)
- [hexo是怎么工作的](http://coderunthings.com/2017/08/20/howhexoworks/)
## 7. Hexo 的模板引擎
这个`render`讲道理应该是在`hexo g`的时候调用的。 待看
