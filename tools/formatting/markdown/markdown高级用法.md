---
title: Advanced Markdown tips
date:
---



## Overview

<!--
## Inline HTML

You can also use raw HTML in your Markdown, and it'll mostly work pretty well.

-->

本文主要介绍markdown嵌入html标签的用法。(有些markdown render不支持内嵌html)
- `<summary>`
- `<img>`


## 折叠块 `<summary>`


你和猪，打一种动物
<details>
  <summary>点击展开答案</summary>
  <p> 象</p>
</details>

源码：
```
<details>
  <summary>点击展开答案</summary>
  <p> 象</p>
</details>
```

## click事件


## 图片样式
markdown的语法不支持图片大小，位置等样式。
```md
![Alt text](图片链接 "optional title")
```
所以可采用`<img>`标签

```html
<img title="hover" alt=="alternate_text" align="middle" width="50" height="50" src="http://www.fillmurray.com/100/100">
```

<img title="hover" alt=="alternate_text" align="middle" width="50" height="50" src="http://www.fillmurray.com/100/100">


## 文本对齐

> 学而不思则罔，思而不学则殆  <div style="text-align:right" >-- 《论语》</div>

```html
<div style="text-align:right" >-- 《论语》</div>
```

## 写注释
不在页面显示，一般写给自己看，或者写给编辑者看(比如提交issue的模板中附带的注释)

- 方式一: 采用html注释标签    `<!-- 这里不会显示  -->`
- 方式二: 直接采用<标签   `<这里不会显示>`

推荐方式一

## code block

正确上设置code block的highlight。


常用的 bash


diff标签很好用
```diff
public class Hello1
{
   public static void Main()
   {
-      System.Console.WriteLine("Hello, World!");
+      System.Console.WriteLine("Rock all night long!");
   }
}
```

## Section links


##

## 问题

### 是否支持嵌入js？


### 是否支持Markdown Inside HTML Blocks?

> Markdown in HTML does not work very well  --来自官方文档

[部分支持](https://stackoverflow.com/questions/29368902/how-can-i-wrap-my-markdown-in-an-html-div)


- [x] `<div> *Emphasized* text. </div>`
- [ ] `<div> ## dfd </div>`


## 参考



[官方文档]https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

http://xusong.vip/demos/ckeditor/
