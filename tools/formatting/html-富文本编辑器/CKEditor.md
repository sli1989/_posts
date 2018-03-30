---
title: 经典的web编辑器--CKEditor
categories:
  - web
  - tools
abbrlink: fae97115
date: 2018-02-23 00:00:00
tags:
---


# 快速搭建CKEditor

[CKEditor CDN](https://cdn.ckeditor.com/)



```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>CKEditor</title>
		<script src="https://cdn.ckeditor.com/4.8.0/standard/ckeditor.js"></script>
	</head>
	<body>
		<textarea name="editor1"></textarea>
		<script>
			CKEDITOR.replace( 'editor1' );
		</script>
	</body>
</html>
```
保存为html，双击打开即可。
[Online Demo](https://blog.eson.org/demos/ckeditor/)


# 源码

https://github.com/ckeditor/ckeditor-dev

## CKFinder

没有CKFinder，CKEditor作为一个编辑器，也是可以正常使用的，但是无法在编辑器里浏览服务器上的用户上传文件。所以要整合CKFinder。

需要后台服务器。(用于文件上传、存储)。支持java php .net等语言

# 其他编辑器
- Tinymce
- 为知笔记也不错，但不开源

## 参考

https://www.ibm.com/developerworks/cn/web/1012_moying_ckeditor/index.html
