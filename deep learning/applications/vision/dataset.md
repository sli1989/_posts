---
title: 计算机视觉--常用数据库
date: 2017-12-12
---

## summary


|  dataset     |  im_size |  class*num|download | task | example code  | pretrained_model|  state of art | 实例图片 | 备注|
| :-------- | -----:| ----:|--------:|--------:|:--: |
| mnist   | 28*28 | 70000| |  | | | | | |
| [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) | 32x32 | 10*6000|  ||  | ||![d](https://www.cs.toronto.edu/~kriz/cifar-10-sample/automobile5.png "汽车") |  Alex,Hinton发布，超小图片|
| [CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html) |32x32 170M |100*600|
| [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/) (05-12) | 2GB ||[voc2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar)| |
| [coco](http://mscoco.org/)  	| || 40GB|
| [imagenet2012](http://image-net.org/challenges/LSVRC/2012/index) |尺寸不固定，但多数比较清晰 | [1000类](http://image-net.org/challenges/LSVRC/2012/browse-synsets)，训练集1.2m，验证集50k,测试集100k| | | | | | 层级标签| AlexNet |
| [imagenet2016](http://www.image-net.org/about-stats)||1400多万幅图片，涵盖2万多个类别 1TB|||
| places   | ||
|  |
| 12306 | 约80*80 |  | | | |  |12306图片比cifar数据库大多了 |






[分类结果汇总](http://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html)

task_code:
1. 图像分类（image classification）
1. 目标检测（object detection）
1. 目标识别（object recognition）
1. 语义分割（semantic segmentation）
1. 实例分割（instance segmentation）

## 来自pytorch vision github的data

LSUN <http://lsun.cs.princeton.edu>`_ dataset
Local Image Descriptors Data <http://phototour.cs.washington.edu/patches/default.htm>`_ Dataset.
SEMEION <http://archive.ics.uci.edu/ml/datasets/semeion+handwritten+digit>`_ Dataset.
STL10 <https://cs.stanford.edu/~acoates/stl10/>`_ Dataset.
SVHN <http://ufldl.stanford.edu/housenumbers/>`_ Dataset.





##
