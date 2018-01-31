---
title: 关于gist
date: 2018-01-26 03:08:53
tags: git
categories:
- tools
- git
---

## gist简介
### 官方描述
> Gists are a great way to share your work. You can share single files, parts of files, or full applications.

关键词: `share`, `single`, `parts`。gist的定位就在这几个词里。

### 详解
- 为了强调`single`和`parts`，gist对git进行阉割，禁用了directory功能。(貌似还禁用了pull功能)
- 为了强调`share`，在原来`Clone`的基础上，额外引入了`Embed`和`Share`两个功能。其中`Embed`(嵌入)实现了仅通过一行JS就能分享到网站(share your work in your website)


- 既然要`share`，那就不能没有feedback，这就像作presentation有问答环节一样。于是加入了`comments`功能。

### Gist背后的Git库

创建的每一个Gist的背后都对应着一个Git版本库

## gist 推荐用法

**推荐用法**
1. 图片文件不放gist
    - gist不支持directory，file&image最好放在其他地方。
    - 最省事的方法：1. 在comment里upload image  2. 在gist doc中引用 3. 删除1中的comment
1. 先在comments里写好doc
    - 主doc不支持markdown preview
    - 主doc有提交慢。因为主doc具有版本管理功能，comments不需要。所以频繁改动状态的doc也最好在comments里写，成形后再放入repo。
1. 用embed js的方式发布gist
    - 解决了多个blog的同步问题
    - 节省blog服务器存储空间
1. host站点不支持嵌入js怎么办？
    - 知乎、博客、github.io都不支持js

**禁忌用法**
两个终端同时修改同一个comment，会已最后提交的为准，有内容丢失的风险（不可逆）。

## gist 代码片段用法


**片段的优势体现在**：
- embed。比如一篇博客里面，要贴个代码片段，可直接引用gist。
- 据说搜索也有优势



### gistBox / cacher 用法

### 技巧

**文件排序**： 根据文件名的ascii排序，数字> 大写> 小写
**快捷键**：用Ctrl或者Cmd按着鼠标多处点击进行多选!用中键或者alt进行拖动实现拉选!

## 缺陷
- 主doc不能preview
- gist embed方式嵌入页面，样式固定，不能自适应网站主题。另外背景是白色，不能融入网站的主题背景。
-

## 疑问

**为什么要偏要对gist设置private和anonymous？git和wiki却没有，设计初衷是什么？**


**为什么gist不开放directory？**
阉割了这个功能，图片的放置就稍微复杂点了。

**gist不提供Pull Request功能？**


## 类似组件
bitbucket的Snippets。 不提供`embed`嵌入方式

## reference
- http://www.worldhello.net/gotgithub/06-side-projects/gist.html
