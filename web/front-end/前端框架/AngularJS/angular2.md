---
title: Angular2原理浅析
date: 2018-03-26
keywords: ["angular","front-end","前端架构"]
tags: ["angular","front-end","前端架构"]
---

## 教程
https://angular.io/guide/quickstart

https://github.com/angular/quickstart

https://www.w3cschool.cn/angular


## 组件和模块的区别

组件(Component)和模块(Module)又是一对容易混淆的名词，也常常被用来相互替换。

从设计上来看，组件强调复用，模块强调职责(内聚、分离)，或者说组件是达到可复用要求的模块。


在AngularJS中，有module的概念，但是它这个module，跟我们通常在AMD里面看到的module是完全不同的两种东西，大致可以相当于是一个namespace，或者package，表示的是一堆功能单元的集合。
