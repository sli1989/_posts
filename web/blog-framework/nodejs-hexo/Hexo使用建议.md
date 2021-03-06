---
title: 【hexo的正确打开方式】使用方式推荐
tag:
  - hexo
categories:
  - web
  - blog-framework
  - nodejs-hexo
abbrlink: d3c1b8ca
date: 2018-01-25 03:08:53
---
## 核心思想



- 利用submodule管理blog  
> 模块化，解耦合，易整合。hexo本身就是模块化很好的例子。cli server分离，主hexo与theme分离。generator deployer render分离。推荐一个模块化比较好的例子 https://github.com/distillpub

- 先fork再add submodule
>

- 利用branch管理自己的project和需要PR的project
> 主要目的也是为了不和自己的修改绞在一起产生混乱。比如我从next仓库fork到我自己的仓库，然后我做了一些只用于我自己的个性化修改，这时候我的master分支和远程master分支之间的变动越来越大了。
然后我碰到一个适用于所有人的变动，这时候想提交个pr，最好的方式显然是切换到远程master分支，然后做修改，之后提交到一个新的分支，再然后就可以去github上提交pr了，不会把自己master上的一些修改混到里面
不过如果自己master和远程master始终保持完全一致的话倒是可以直接提交到自己master上，然后直接用自己master分支提交pr


**细节**
主仓库
- `themes/` 每个theme是一个子仓库  (经常pull一下主题，有很多新功能和bug-fix。不用为了增加某些功能而自己改模板源文件，比如busuanzi，disqus的lazy_load)
- `source/post/`设置为一个子仓库  (可多终端同步文章)
- `source/demos/`下包含多个子仓库
- `source/public` 如果文件可以被渲染的话，会经过解析然后储存到 public 文件夹，否则会直接拷贝到 public 文件夹。
- `source/games`下包含多个子仓库



**模块搭建&整合流程**

```bash
# 1. fork hexo-starter 作为blog主仓库
$ git clone --recursive git@github.com:xsung/hexo-starter.git blog

# 2. 添加 submodule
# 2.1 fork theme & add submodule
$ cd blog/themes/
$ git submodule add git@github.com:xsung/hexo-theme-next.git next

# 2.2 fork _post & add submodule
$ git submodule add git@github.com:xsung/_posts.git


# 2.3 fork project-u-like & add submodule
$ mkdir blog/source/games/ && cd blog/source/games/
$ git submodule add git@github.com:xsung/2048.git

# 检查是否添加成功
$ vi .gitmodules

# 3. push到blog主仓库 (整合)
cd blog/
git commit -m "add submodules hexo-theme-next source/_post games/2048"
git push -u origin master

```

> Note: 如果你嫌fork太多，那么可以开一个github小号，管理这些fork。
github主账号只放deploy版本。

实例：
- [x] [Dev Repository](https://github.com/xsung/blog-dev/#submodule) Main project for all submodules
- [x] [Deployed Repository](https://github.com/xu-song/xu-song.github.io/) is deployed by Hexo from `Dev Repository`
- [x] [Demo Site](http://xusong.vip) hosts the `Deployed Repository`


## push (提交更改)
- 每个module独立push
```bash
# 1. commit changes from all submodules (e.g. _posts)
$ cd _posts
$ commit & push

# 2. commit changes from blog-dev
$ cd blog
$ commit & push
```


## clone & setup
```bash
$ git clone --recursive URL
$ cd blog-dev
$ npm install --production
```

## pull & merge (整合)

```bash
# 2. pull latest of all git submodules
$ cd blog
$ git submodule update --recursive --remote  # 这个命令会造成HEAD detached
$ git pull --recurse-submodules
# reference https://stackoverflow.com/questions/1030169/easy-way-to-pull-latest-of-all-git-submodules

```
貌似不work啊，submodule的pull不work

```sh
$ git pull && git submodule init && git submodule update && git submodule status
```
这个work

## clone & deploy
```bash
$ git clone --recursive git@github.com:xsung/blog-dev.git blog
$ npm install hexo --save  # install node_modules dependency
$ hexo s
$ hexo d
```

## 从官方更新模块（操作较少）

比如，theme-next有些新功能，那么需要更新到自己的blog中。

### 方式一：
```bash
$ git remote add upstream https://github.com/theme-next/hexo-theme-next.git
$ git fetch upstream
$ git checkout master
$ git rebase upstream/master  # 或merge,推荐merge
$ git merge upstream/master
```

### 方式二(推荐用法)：
在[theme的github界面](https://github.com/xsung/hexo-theme-next)pull & merge



### 参考:
[stackoverflow](https://stackoverflow.com/questions/7244321/how-do-i-update-a-github-forked-repository)




## 其他操作建议
- 每个post都加date，不然每次编辑文档，时间都会变动
- draft 可以放在`_draft`目录下，当然我更习惯放在`_post/`中，文件名`_`开头即可，或者整个目录`_`开头。
- 文件名不要经常变动(因为会改变url)，title和path可以随时改动


## 非法操作
- 在`Deployed Repository`人工提交。(除非你不用hexo d命令，或不用hexo)
-
