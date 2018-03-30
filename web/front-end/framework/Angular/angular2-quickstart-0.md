---
title: Angular 2 JavaScript 入门
abbrlink: 5a499450
date: 2018-03-28 00:00:00
---






[教程链接](http://www.runoob.com/angularjs2/angularjs2-javascript-setup.html)


首先是不掺杂typescript，更能熟悉angular其工作原理。


# 运行
1. 下载源码
1. npm install
1. 双击html即可。无须借助node server，更容易理解前端框架






## 执行顺序
1. npm start启动lite-server，默认加载index.html。或直接双击index.html
1. 浏览器加载index.html
1. 浏览器依次加载并执行 app.component.js、app.module.js、main.js
  1. 执行app.component.js，将app.component匿名函数加入到window.app中。并未调用constructor
  1. 执行app.module.js，将app.module匿名函数加入到window.app中
  1. 执行main.js，
1. main.js调用app.AppModule，即调用app.module匿名函数。其中会调用constructor
1. app.module调用app.AppComponent，即调用app.component匿名函数，返回template

# 细节

## index.html

```html
<html>

  <head>
	<meta charset="utf-8">
    <title>Angular 2 实例 - 菜鸟教程(runoob.com)</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="styles.css">

    <!-- 1. 载入库 -->
    <!-- IE 需要 polyfill -->
    <script src="node_modules/core-js/client/shim.min.js"></script>

    <script src="node_modules/zone.js/dist/zone.js"></script>
    <script src="node_modules/reflect-metadata/Reflect.js"></script>

    <script src="node_modules/rxjs/bundles/Rx.js"></script>
    <script src="node_modules/@angular/core/bundles/core.umd.js"></script>
    <script src="node_modules/@angular/common/bundles/common.umd.js"></script>
    <script src="node_modules/@angular/compiler/bundles/compiler.umd.js"></script>
    <script src="node_modules/@angular/platform-browser/bundles/platform-browser.umd.js"></script>
    <script src="node_modules/@angular/platform-browser-dynamic/bundles/platform-browser-dynamic.umd.js"></script>

    <!-- 2. 载入 'modules'
   顺序不能乱，因为main.js依赖app.module.js，app.module.js依赖app.component.js -->
    <script src='app/app.component.js'></script>
    <script src='app/app.module.js'></script>
    <script src='app/main.js'></script>

  </head>

  <!-- 3. 显示应用 -->
  <body>
    <my-app>Loading...</my-app>
  </body>

</html>
```


## main.js

定义了一个匿名函数，参数为`app`

第二个括号用于调用该匿名函数，并传入参数。

```js
(function(app) {
  document.addEventListener('DOMContentLoaded', function() {
    ng.platformBrowserDynamic
      .platformBrowserDynamic()
      .bootstrapModule(app.AppModule);  // 依赖AppModule类
  });
})(window.app || (window.app = {}));
```

## app.module.js


定义了一个匿名函数，参数为`app`。
```js
(function(app) {
  app.AppModule =  // // 创建一个Angular Module对象，并赋值给对app
    ng.core.NgModule({
      imports: [ ng.platformBrowser.BrowserModule ],
      declarations: [ app.AppComponent ],
      bootstrap: [ app.AppComponent ]
    })
    .Class({
      constructor: function() {}
    });
})(window.app || (window.app = {}));
```



## app.component.js

定义了一个匿名函数，参数为`app`

```js
(function(app) {
  app.AppComponent =  // 创建一个Angular Component对象
    ng.core.Component({
      selector: 'my-app',
      template: '<h1>我的第一个 Angular 应用</h1>'
    })
    .Class({
      constructor: function() {}
    });
})(window.app || (window.app = {}));
```


## package.json
用于npm install的依赖和npm start的脚本。

```json
{
  "name": "angular2-quickstart",
  "version": "1.0.0",
  "scripts": {
    "start": "npm run lite",
    "lite": "lite-server"
  },
  "license": "ISC",
  "dependencies": {
    "@angular/common": "2.0.0",
    "@angular/compiler": "2.0.0",
    "@angular/core": "2.0.0",
    "@angular/forms": "2.0.0",
    "@angular/http": "2.0.0",
    "@angular/platform-browser": "2.0.0",
    "@angular/platform-browser-dynamic": "2.0.0",
    "@angular/router": "3.0.0",
    "@angular/upgrade": "2.0.0",

    "core-js": "^2.4.1",
    "reflect-metadata": "^0.1.3",
    "rxjs": "5.0.0-beta.12",
    "zone.js": "^0.6.23",

    "angular2-in-memory-web-api": "0.0.20",
    "bootstrap": "^3.3.6"
  },
  "devDependencies": {
    "concurrently": "^2.0.0",
    "lite-server": "^2.2.0"
  }
}
```
