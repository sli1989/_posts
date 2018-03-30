---
title: Angular2中的一些概念
keywords:
  - angular
  - front-end
  - 前端架构
tags:
  - angular
  - front-end
  - 前端架构
abbrlink: 84fd5459
categories:
  - web
  - front-end
  - framework
  - Angular
date: 2018-03-26 00:00:00
---
## 运行环境

由于目前各种环境（浏览器或 Node）暂不支持ES6的代码，所以需要一些shim和polyfill（IE需要）让ES6写的代码能够转化为ES5形式并可以正常运行在浏览器中。

<img src="http://www.runoob.com/wp-content/uploads/2016/09/toolchain.jpg"> </img>


从上图可以看出在 Es5 浏览器下需要以下模块加载器：
- systemjs - 通用模块加载器，支持AMD、CommonJS、ES6等各种格式的JS模块加载。
- es6-module-loader - ES6模块加载器，systemjs会自动加载这个模块。
- traceur - ES6转码器，将ES6代码转换为当前浏览器支持的ES5代码，systemjs会自动加载 这个模块。


## 组件和模块的区别

组件(Component)和模块(Module)又是一对容易混淆的名词，也常常被用来相互替换。


### 模块

模块相当于是一个namespace，或者package，表示的是一堆功能单元的集合。

Angular应用都是模块化的，

- 命名空间：
  在JavaScript中，最高级别的函数外定义的变量都是全局变量（这意味着所有人都可以访问到它们）。也正因如此，当一些无关的代码碰巧使用到同名变量的时候，我们就会遇到“命名空间污染”的问题。
- 可维护性：
  命名空间的隔离实现了每个模块的独立性。良好设计的模块会尽量与外部的代码撇清关系，以便于独立对其进行改进和维护。可复用性也好



### 组件
一般来说，一个组件就是一个用于控制视图模板的JavaScript类。

从设计上来看，组件强调复用，模块强调职责(内聚、分离)，或者说组件是达到可复用要求的模块。




# 习题

原生javascript(ES5)不支持模块化，类难道不起到了隔离作用吗？
原生JavaScript并不支持类，虽然最新的ES6里引入了Class不过还不普及。

没有内置的模块化系统，可以使用第三方模块系统。


疑问，angular4 是否有cdn？cdn只看到了1 和 2。

# 参考

[JavaScript 模块化入门Ⅰ：理解模块](https://zhuanlan.zhihu.com/p/22890374)
