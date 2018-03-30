---
title: OCR引擎-Tesseract-OCR简介
keywords:
  - Tesseract
  - OCR
tags:
  - Tesseract
  - OCR
category:
  - OCR
abbrlink: 1ff2cbf2
categories:
  - deep learning
  - applications
  - vision
  - OCR
  - Tesseract-OCR
date: 2018-03-17 00:00:00
---
# Tesseract简介&历史

Tesseract(/'tesərækt/) 意思是四维超正方体（英语：tesseract）或正八胞体。下图来自维基百科，是一个正八胞体绕着两个四维空间中互相正交的平面进行双旋转时的透视投影。

<img title="这不是Tesseract-OCR的logo" src="https://upload.wikimedia.org/wikipedia/commons/5/55/8-cell-simple.gif"></img>


Tesseract-OCR是一个开源的OCR引擎，具有悠久的历史。
惠普公司的布里斯托尔实验室在1984-1994年开发完成。起初作为惠普的平板扫描仪的文字识别引擎。Tesseract在1995年UNLV OCR字符识别准确性测试中拔得头筹，受到广泛关注。后来HP放弃了OCR市场。在1994年以后，Tesseract的开发就停止了。

在2005年，HP将Tesseract贡献给开源社区。美国内华达州信息技术研究所获得该源码，同时，Google开始对Tesseract进行功能扩展及优化。目前，Tesseract作为开源项目发布在Google Project上，重获新生。Tesseract的最新版本是3.02，它支持60种以上的语言，提供一个引擎和一个命令行工具。


- [github-官网](https://github.com/tesseract-ocr/tesseract)
- [官方文档-wiki](https://github.com/tesseract-ocr/tesseract/wiki)

# 安装

sudo apt-get install tesseract-ocr

sudo apt-get install tesseract-ocr-eng tesseract-ocr-chi-sim


[Tesseract:安装与命令行使用](http://www.zmonster.me/2015/04/17/tesseract-install-usage.html)



# 使用

```sh
# 查看可用的 "语言"
$ tesseract --list-langs
```

## Tesseract识别图片

```sh
# from a TIFF image with Tesseract OCR
$ tesseract test.png test
```

## Tesseract识别tiff
```sh
# 识别tiff文档，默认是英语
$ tesseract test.tiff test

# 识别非英语文档
tesseract test.tiff -l [lan] test.txt
```

## Tesseract识别pdf

步骤:
```sh
# 1. 转换pdf到tiff(或其他格式)

# 2.
```



```sh
$ tesseract test.pdf test
Tesseract Open Source OCR Engine v3.02 with Leptonica
Error in pixReadStream: Unknown format: no pix returned
Error in pixRead: pix not read
Unsupported image type.
```
tesseract不能直接识别pdf，一般需要借助工具转化成tiff，然后再识别。


```sh
$ convert test.pdf test.tiff
$ tesseract test.tiff test
Tesseract Open Source OCR Engine v3.02 with Leptonica
Error in pixReadFromTiffStream: can't handle bpp > 32
Error in pixReadStreamTiff: pix not read
Error in pixReadStream: tiff: no pix returned
Error in pixRead: pix not read
Unsupported image type.
```
tesseract不能够读取bpp > 32的tiff文件。因此我们转为8bit的tiff文件。

```sh
$ convert test.pdf -depth 8 test.tiff
$ tesseract test.tiff output

```
现在能够正常识别了。

# 训练

参考 https://www.jianshu.com/p/31afd7fc5813

## 准备训练集



# 评价

- 图像预处理
Tesseract目的不是作为OCR软件，而仅仅是`OCR engine`。Tesseract在图像预处理方面很弱，如果想得到比较好的识别效果，需要使用者[自己做图片预处理](https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality)。然而一般多数OCR软件都会集成图片预处理模块，比如Nuance。

估计怕做的太好，让商业软件










#
