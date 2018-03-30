---
title: OCR
abbrlink: dab63ff1
date: 2018-03-27 00:00:00
---


[OCR文字识别用的是什么算法？--知乎](https://www.zhihu.com/question/20191727)


# 流程

General OCR一般包含两步:
1. detection-->找到包含文字的区域(proposal);
1. 接着利用radon hough变换 等方法 进行文本校正。
1. 通过投影直方图分割出单行的文本的图片。


1. classification-->识别区域中的文字。


framework是: CNN + LSTM + CTC。这个framework加上residue network + stn可以把通用的数据集刷的非常高。


## detection

先说detection models, 近两年比较热门的object detection model有 faster-rcnn(https://arxiv.org/pdf/1506.01497.pdf) 和 yolo(http://pjreddie.com/media/files/papers/yolo.pdf), 两个模型都是基于CNN给出proposed regions 同时对object region进行分类。 其中yolo比faster-rcnn的速度更快，但是在accuracy上有些损失。

比较著名的是Ian goodfellow在13年提出的multi-digit number classification

另一类比较常用的方法是RNN/LSTM/GRU + CTC,


# 开源工具&代码
https://github.com/tesseract4java/jtesseract


开源包: [tesseract 很赞](https://github.com/tesseract-ocr/tesseract)


最好的模型，竟然是lstm？https://github.com/tesseract-ocr/tessdata_best
