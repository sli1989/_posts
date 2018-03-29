---
title: 文件管理工具 - Everthing原理 之 还没看懂
date: 2018-03-26
keywords: ["Everthing","文件管理"]
tags: ["Everthing","文件管理"]
---

# 简介

Everything is an Awesome Utility that Locates Files and Folders Instantly in Windows

`Everything`仅支持windows系统的NTFS硬盘格式(不支持FAT、FAT32)。`Everything`默认对文件名、文件大小、日期以及其它某些meta data建索引，可[关闭某些字段索引来加速](https://www.voidtools.com/support/everything/indexes/#optimizing_for_smallest_memory_foot_print)。

- 建索引很快
  - 数据库文件 Everything.db。 这是什么类型的数据库？自定义的吗？
- 搜索超快
  - 怎样建的索引？咋这么快？建了个hash索引？倒排索引？
- 实时性好
  - 怎样获取的新文件列表？大量的临时文件要不要索引？

`Everything`功能如此强大，让人不禁对其工作原理产生强烈的好奇心。
但是，`Everthing`官方**未开源**，这对想学习其工作原理的程序员来说是个bad news。官方提供[SDK](http://www.voidtools.com/support/everything/sdk/)不知能否看出一些原理逻辑。待看


## 啊哈，有相关开源项目

微软某成员(疑似轮子哥)在codeplex开源了一个类似everything的个人项目[`everythingSZ`](https://archive.codeplex.com/?p=everythingsz)。以下介绍EverythingSZ的原理。



# 原理


Everything搜索文件很快，是利用的NTFS分区的USN功能.



原理：
- 读取NTFS下的USN日志文件
  - [UsnOperator类源码](https://github.com/BitMindLab/everything/blob/master/UsnOperation/UsnOperator.cs)
- 根据USN继续查询；
- 根据文件编号继续查询；
- 创建USN（激活USN状态）；
- NTFS的Change Journal（更改日志）的方法实现监控功能


> 未采用 FileSystemWatcher 监听文件变化。(everthing不是采用的这个window api)


## 如何建索引


## 如何监听文件变化

这属于操作系统 & 文件系统的范畴。

### Windows
即利用windows api。

以下几种方式：
1. FindFirstChangeNotification
  - 无法获取是哪一个文件发生了改变。
1. ReadDirectoryChangesW
  - 据说变化量大又密集时，丢失通知现象很严重
1. FileSystemWatcher
  - 貌似是对ReadDirectoryChangesW的封装
1. NTFS的Change Journal（更改日志）
  - Change Journal是标卷上一个特殊的文件，系统将其隐藏，所以用资源管理器或者CMD Shell都看不到，当文件系统中的文件或者目录发生改变时，就会向日志中追加记录。[参考](https://blog.csdn.net/arrowzz/article/details/75304091)
  - 通过读取和监控USN（后面会讲）而不是扫描文件来构建索引，所以搜索速度飞快


Everything采用了第四种方式，即利用了NTFS系统的Change Journal特性。

### Linux

- inotify 命令
  - 是Linux自带的监控inode变动的函数
  - 文档 man 7 inotify）
-

# 其它疑问

## linux下有没有类似的工具
比linux下的find命令快，比locate命令实时性好。

[见stackexchange](https://unix.stackexchange.com/questions/31063/is-there-a-file-search-engine-like-everything-in-linux)

# 参考 & 待看

- [EverythingSZ源码 - 轮子哥推荐 | Github C#](https://github.com/BitMindLab/everything)
- [探索Everything背后的技术（USN和MFT）| Github](https://github.com/yuzhengyang/Everything)
-  [NTFS系列](https://blog.csdn.net/column/details/16576.html)
- [密切关注你的NTFS驱动器 | CSDN](https://blog.csdn.net/xexiyong/article/details/17200827)
-
