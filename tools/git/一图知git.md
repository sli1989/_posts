---
title: 一图知git
date: 2018-01-26 03:08:53
tags: git
categories:
- tools
- git
---





## 简介

首先，这不是一个git命令教程，这是一个用于快速理解git命令的辅助文档。

用了git几年了，每次遇到疑难杂症都要现查，归其原因，是不了解git命令背后到底做了什么。

于是决定整理一下思路。


## 术语

**存储位置**
- 工作区：working_directory，working_tree，workspace
- 暂存区：stage, index  (加入到暂存区的更改：staged/indexed changes, add changes to stage/index)
- 本地仓库： local_repository, local_commit_history，history
- 远程仓库：remote_repository

- 快照：snapshot

文件状态
- Untrack file：新文件，从未被add的文件。下一步操作往往是`git add`或者加入`.gitignore`中
-

**changes**
- Changes to be committed
- Changes not staged for commit

**指针**
指针指向实体
- HEAD
  - Detached HEAD：指anonymous branch，即只要不指向named branch都算detached
- master

**实体**
hash




## 直接上图吧


<img src="https://raw.githubusercontent.com/xsung/doc/master/git-graph-mid.svg?sanitize=true" height="110%" width="110%">



有点紧凑，建议放大看

## 看图说话

**入门**：
[git add](https://git-scm.com/docs/git-add) : 读取工作区文件，写入暂存区 (1个箭头代表1个写操作)

**进阶**：

[git checkout \<branch\>](https://git-scm.com/docs/git-checkout): 移动本地仓库中的HEAD指针到指定branch，更新index，更新工作区文件 (3个箭头)

[git reset --soft](https://git-scm.com/docs/git-reset)：撤销指定commit，移动HEAD (不涉及工作区、暂存区、远程仓库的操作)

soft mixed hard三个参数的区别也一目了然
...

## 正逆向操作，对比

stage操作：git add
undo stage：git reset –mixed

git reset −p
git add −p


commit操作：git commit
undo commit：git reset –soft

push操作：
undo push:

force push操作：git push –force
undo force push:

rm操作：
undo rm：



## 关于该图的改进

- 捡重要的命令放 (init clone不要放)
- 布局，整体，有点丑








## 参考
- https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch/292359
- [官方doc](https://git-scm.com/docs)
- [图解git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html)

## 待续
