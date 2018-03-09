


jQuery是js的lib。增加了$符号。

AngularJS 通过新的属性和表达式扩展了 HTML。看上去像html模板解析器。{{name}}。还有php解析器，html模板的python解析器

AngularJS 表达式写在双大括号内：{{ expression }}。

AngularJS 表达式把数据绑定到 HTML，这与 ng-bind 指令有异曲同工之妙。

AngularJS 将在表达式书写的位置"输出"数据。



# AngularJS 1

http://www.runoob.com/angularjs/angularjs-tutorial.html

AngularJS 通过新的属性和表达式扩展了 HTML。

AngularJS 可以构建一个单一页面应用程序（SPAs：Single Page Applications）。


Angular 1

# Angular 2


Angular2.x与Angular1.x 的区别类似 Java 和 JavaScript 或者说是雷锋与雷峰塔的区别，
- Angular2不是从Angular1升级过来的，Angular2是`重写`的，所以他们之间的差别比较大，
- Angular2使用了javascript的超集`Typescript`，所以angular1和angular2从设定之初就是不一样的；
- Angular1.x在设计之初主要是针对pc端的，对移动端支持较少（当然也有其他一些衍生框架如ionic），而Angular2是设计包含移动端的；
- Angular 1的核心概念是`$scope`，但是angular2中没有$scope，angular2使用zone.js来记录监测变化；
- Angular 1 中的控制器在angular2中不再使用，也可以说控制器在angular2中被‘Component’组件所替代：


Angular2 的核心灵魂只有一个，那就是组件化（Component），而其它那些细碎的东西，比如 Service、Route、Pipe，都是 utils 而已



angular需要借助nodejs在后台把.ts编译成.js

# 关系

## Angular和node的关系

## angular 必须依赖node吗？ 我看ts解析要用到node的。

> 运行npm start的时候  ts会编译成js 然后提供一个web server给你跑 。你可以用其他工具编译  放在tomcat上跑也可以的。  不用Node也可以

可以不依赖，可以不用node编译，比如用grunt-ts编译。
官方教程用的是node
webpack这类依赖

Angular 1应该完全不依赖node，因为不支持`Typescript`。


还有其他的编译工具，


## angular是服务端渲染还是浏览器端渲染

都有
- 浏览器端渲染，比如{{ }}  
- 服务端编译 .ts转.js    (less和ts等，浏览器端都不识别，都需要在服务器端编译好)
