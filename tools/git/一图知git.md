---
title: 一图知git
date: 2018-01-26 03:08:53
tags: git
categories: "git"
---





## 简介

首先，这不是一个git命令教程，这是一个用于快速理解git命令的辅助文档。

用了git几年了，每次遇到疑难杂症都要现查，归其原因，是不了解git命令背后到底做了什么。

于是决定整理一下思路。


## 术语

- 工作区：working_directory，working_tree，workspace
- 暂存区：staged, index
- 本地仓库： local_repository, local_commit_history
- 远程仓库：remote_repository

- 快照：snapshot




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


## 关于该图的改进

- 捡重要的命令放 (init clone不要放)
- 布局，整体，有点丑








## reference
- https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch/292359
- https://git-scm.com/docs
- [图解git]http://marklodato.github.io/visual-git-guide/index-zh-cn.html

## 待续
