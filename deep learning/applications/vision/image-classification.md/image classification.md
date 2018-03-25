---
title: 图像分类--模型汇总
date: 2018-01-01
---

## image classification



|  model     |  简介 |  | conv_padding |  conv_activation | pooling   | code | 备注|
| :-------- | -----:| ----:|--------:|--------:|:--: |
| LeNet5 |  3个卷积层+2个pooling层 |  | valid |  sigmoid |  |  |
| AlexNet |  8层 |   | same | ReLU  | Overlapping Pooling|
| VGG-19 |  19层 |  | same | ReLU | | [keras](https://github.com/fchollet/deep-learning-models/blob/master/vgg19.py) |
| GoogLeNet | 22层 | |
| ResNet |  | 152层  |  |  | | [keras](https://github.com/fchollet/deep-learning-models/blob/master/resnet50.py) |



conv2d的VALID方式不会在原有输入的基础上添加新的像素
