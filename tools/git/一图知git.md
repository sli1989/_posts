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
- Blobs:   即files

**文件状态**
- Untrack file：新文件，从未被add的文件。下一步操作往往是`git add`或者加入`.gitignore`中
-

**changes **
- Changes to be committed
- Changes not staged for commit

**操作**
stage操作：git add
commit操作：git commit

**指针**
指针指向实体
- HEAD指针
  - 正常状态: 指向一个<branch> (确切说是named branch)
  - Detached HEAD: 指向了anonymous branch，即<commit>
  - null: 不可能出现这个状态
- master

**HEAD指针状态**


**实体**
hash
<commit>、<branch>、<tree-ish>、<start point>什么区别？
能写master~吗？能写 jkjdka~吗？

参考 https://stackoverflow.com/questions/23303549/what-are-commit-ish-and-tree-ish-in-git

## 上图


<img src="image/raw/git-graph-mid.svg?sanitize=true" height="110%" width="110%">



有点紧凑，建议放大看

## 看图说话

**入门**：
[git add](https://git-scm.com/docs/git-add) : 读取工作区文件，写入暂存区 (1个箭头代表1个写操作)

**进阶**：

[git checkout \<branch\>](https://git-scm.com/docs/git-checkout): 移动本地仓库中的HEAD指针到指定branch，更新index，更新工作区文件 (3个箭头)

[git reset --soft](https://git-scm.com/docs/git-reset)：撤销指定commit，移动HEAD (不涉及工作区、暂存区、远程仓库的操作)

soft mixed hard三个参数的区别也一目了然
...

## [所有涉及更改index区域的操作](https://git-scm.com/docs/git-commit)
- git add
- git rm
- by listing files as arguments to the commit command (without --interactive or --patch switch), in which case the commit will ignore changes staged in the index, and instead record the current content of the listed files (which must already be known to Git);

- by using the -a switch with the commit command to automatically "add" changes from all known files (i.e. all files that are already listed in the index) and to automatically "rm" files in the index that have been removed from the working tree, and then perform the actual commit;

- by using the --interactive or --patch switches with the commit command to decide one by one which files or hunks should be part of the commit in addition to contents in the index, before finalizing the operation. See the “Interactive Mode” section of git-add[1] to learn how to operate these modes.


## 逆向操作(undo)

```
git add                 # 加入index
git reset –mixed HEAD   # 撤销index  对不，是checkout吗？

git commit              #
git reset –soft HEAD~   # 撤销尚未push的commit

git add + git commit    #


git push    
push不支持撤销操作       # 如何撤销已经push的commit？

git push –force         # 覆盖远程仓库提交历史(太狠)
                        # 参考 https://www.borfast.com/blog/2014/10/19/how-to-undo-a-git-push---force-and-undelete-things/
git rm file             # 删除文件和index
git checkout HEAD file  # 恢复文件和index (index中已经没有该文件的信息，只能从仓库的HEAD中恢复文件)

git rm -r dir           # 删除整个目录及相应index
git checkout HEAD dir   # 恢复

git add −p
git reset −p

git stash
git stash pop


```

两个git add 会怎样？会merge为一个吧？git add + rm 前面的add的changes就完全丢了吧？

If you don't have `uncommited changes` for removed files, the


如何撤销已经push的commit？

如何撤销已经force push的commit？

https://www.borfast.com/blog/2014/10/19/how-to-undo-a-git-push---force-and-undelete-things/



Reset



## 关于该图的改进

- 捡重要的命令放 (init clone不要放)
- 布局，整体，有点丑


## 待看


https://github.com/geeeeeeeeek/git-recipes/blob/master/sources/%E6%A3%80%E5%87%BA%E4%BB%A5%E5%89%8D%E7%9A%84%E6%8F%90%E4%BA%A4.md

[代码合并：Merge、Rebase 的选择](https://github.com/geeeeeeeeek/git-recipes/blob/master/sources/%E4%BB%A3%E7%A0%81%E5%90%88%E5%B9%B6Merge%E8%BF%98%E6%98%AFRebase.md)
[重写项目历史](https://github.com/geeeeeeeeek/git-recipes/blob/master/sources/%E9%87%8D%E5%86%99%E9%A1%B9%E7%9B%AE%E5%8E%86%E5%8F%B2.md)
[常见工作流比较](https://github.com/geeeeeeeeek/git-recipes/blob/master/sources/%E5%B8%B8%E8%A7%81%E5%B7%A5%E4%BD%9C%E6%B5%81%E6%AF%94%E8%BE%83.md)



## 参考
- https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch/292359
- [官方doc](https://git-scm.com/docs)
- [图解git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html)

## 待续
