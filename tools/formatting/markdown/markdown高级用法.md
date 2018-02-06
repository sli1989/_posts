---
title: Advanced Markdown tips
date:
---


## Overview

本文主要介绍markdown嵌入html标签的用法
- `<summary>`
- `<img>`


## 折叠块


你和猪，打一种动物
<details>
  <summary>点击展开答案</summary>
  <p> 象</p>
</details>


## click事件


## 图片样式
alignment & scale & hover_text

<img title="hover" alt=="alternate_text" align="middle" width="50" height="50" src="http://www.fillmurray.com/100/100" href="">


## 写注释(不在页面显示)

- 方式一: 采用html注释 <!-- 这里不会显示  -->
- 方式二: 直接采用<标签   <ss这里不会显示>

推荐方式一

## 问题

### 是否支持嵌入js？

### 是否支持Markdown Inside HTML Blocks?
[部分支持](https://stackoverflow.com/questions/29368902/how-can-i-wrap-my-markdown-in-an-html-div)
- [x] `<div> *Emphasized* text. </div>`
- [ ] `<div> ## dfd </div>`
