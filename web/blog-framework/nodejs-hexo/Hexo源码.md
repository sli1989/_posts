---
title: Hexo源码浅析
tag: ["hexo","源码"]
---

## 简介


最好带着问题往下看。




## Hexo官方文档

[]官方文档](https://github.com/hexojs/hexo/blob/master/README.md)

``` bash
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


## 详解

### 1. npm install

npm是nodejs的包管理器，管理javascript lib
hexo-cli是nodejs的一个包，用于运行hexo命令。(有cli难道还有server？)

npm list -g 能够看到安装路径。一般在/usr/lib/node_modules/ 或者/usr/local/lib/node_modules/

### 2. hexo init
hexo init命令做了什么？
直接放**答案**。
```bash
# 1. git clone --recursive https://github.com/hexojs/hexo-starter.git blog
INFO  Cloning hexo-starter to blog

# 2. npm install --production
INFO  Install dependencies
```
主要就做了一个git clone，看到这里就已经够用了。
如果对追寻答案的过程感兴趣，可以继续往下看。

**追寻答案** - optinal

首先看一下hexo。

```bash
$ which hexo
/usr/bin/hexo

$ cat /usr/bin/hexo
#!/usr/bin/env node
'use strict';
require('../lib/hexo')();
```


这里你会发现，hexo命令是nodejs脚本。 `../lib/hexo`对应的是`usr/lib/hexo`，然而没有path。

```bash
$ ls -l /usr/bin/hexo
 /usr/bin/hexo -> ../lib/node_modules/hexo-cli/bin/hexo
```

原来`/usr/bin/hexo`是个符号链接，链接到nodejs的modules目录里。

```bash
cd /usr/lib/node_modules/hexo-cli/bin/hexo

```

- [hexo命令 源文件](https://github.com/hexojs/hexo-cli/blob/master/lib/hexo.js)
- [hexo init命令 源文件](https://github.com/hexojs/hexo-cli/blob/master/lib/console/init.js)


`init.js`主要代码:
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

实际上吧，如果hexo的log打印出来`GIT_REPO_URL`，就更清晰。

另外，不建议把.git删掉。因为删掉后就不能对比自己改动了哪。保保留可以通过git diff命令查看自己的改动，错误的改动，方便还原。

个人建议采用以下命令代替`hexo init`：
```bash
git clone --recursive https://github.com/hexojs/hexo-starter.git blog
npm install --production
```


### 3. hexo server

这个不属于hexo-cli了。
[hexo server命令源码](https://github.com/hexojs/hexo-server/blob/master/lib/server.js)

暂没兴趣，应该就是启了个nodejs HttpServer。待看

- 额外的逻辑是，如果没generate，先调一下 hexo g



### 4. hexo new



### 5. hexo generate

这里比较重要


## reference
http://cherryblog.site/hexo-4.html
