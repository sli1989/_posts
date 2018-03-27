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



## 原理


Everything搜索文件很快，是利用的NTFS分区的USN功能.



原理：
- 读取NTFS下的USN日志文件
- 根据USN继续查询；
- 根据文件编号继续查询；
- 创建USN（激活USN状态）；
- 使用 FileSystemWatcher 监听文件变化
-

# 其它疑问

## linux下有没有类似的工具
比linux下的find命令快，比locate命令实时性好。


[参考](https://unix.stackexchange.com/questions/31063/is-there-a-file-search-engine-like-everything-in-linux)

# 参考 & 待看

- [轮子哥推荐的用C#写的everythingSZ](https://github.com/BitMindLab/everything)
- [探索Everything背后的技术（USN和MFT）](https://github.com/yuzhengyang/Everything)
- [密切关注你的NTFS驱动器](https://blog.csdn.net/xexiyong/article/details/17200827)
