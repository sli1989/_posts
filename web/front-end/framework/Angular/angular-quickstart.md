---
title: Angular typescript快速入门教程 - Hello Angular
date: 2018-03-26
keywords: ["angular","front-end","前端架构"]
tags: ["angular","front-end","前端架构"]
---



# 简介

Angular 是由谷歌开发与维护一个开发跨平台应用程序的框架，同时适用于手机与桌面。

其模板基于双向UI数据绑定。数据绑定是一种自动方法，在模型改变时更新视图，以及在视图改变时更新模型。




## 流程简介

https://github.com/angular/quickstart
https://angular.io/guide/quickstart

1. 浏览器默认请求`index.html`
1. `index.html`调用`main.js`
1. `main.js`调用`app.component.js`
1. `app.component.js`扫描html，发现有`my-app`标签，将字符串`<h1>Hello {{name}}</h1>`动态插入到`my-app`元素里。
1. `angular的js`扫描html，发现了`{{name}}`，向后台发送一个动态请求 (好像是在js中的hard code)


## 流程分解

### 入口 index.html

以下是`index.html`，其中调用了`main.js`

```html
<!-- src/index.html -->
<html>
  <head>
    <title>Angular QuickStart</title>
    <base href="/">   <!-- 如果想双击运行html的话，需要去掉这行，并加入angular依赖 -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="styles.css">

    <!-- IE 需要 polyfill -->
    <script src="node_modules/core-js/client/shim.min.js"></script>

    <script src="node_modules/zone.js/dist/zone.js"></script>
    <script src="node_modules/systemjs/dist/system.src.js"></script>

    <!-- 这里是Angular的入口js文件 -->
    <script src="systemjs.config.js"></script>
    <script>
      System.import('main.js').catch(function(err){ console.error(err); });
    </script>
  </head>

  <body>
    <!-- 使用 AppComponent 组件 -->
    <my-app>Loading AppComponent content here ...</my-app>
  </body>
</html>
```

在`main.ts`中设置断点，会看到页面是这样子的。

<img src="/images/raw/Web - frontend - Angular - quickstart.png"></img>

### main.ts


`main.ts`调用 AppModule模块，会创建AppModule类。(由Angular的NgModuleFactory创建)
```js
// src/main.ts
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';
platformBrowserDynamic().bootstrapModule(AppModule);
```



### AppModule 模块

`AppModule`模块的声明如下。其中调用了`AppComponent`组件，即首先创建`AppComponent`类。(由Angular的ComponentFactory创建)
```js
// src/app/app.module.ts
import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent }  from './app.component';

// NgModule指令实现数据的双向绑定
@NgModule({
  imports:      [ BrowserModule ],
  declarations: [ AppComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
```

### AppComponent 组件

`AppComponent` 组件会对html中的`my-app`标签进行渲染，返回`template`中指定的元素。

以下是`AppComponent`组件的声明


```js
// src/app/app.component.ts
import { Component } from '@angular/core';
// 通过 Component 装饰器和自定义组件类来创建自定义组件
@Component({ // 定义组件的元信息
  selector: 'my-app', // 用于定义组件在HTML代码中匹配的标签
  template: `<h1>Hello {{name}}</h1>`, // 定义组件内嵌视图。利用 {{}} 插值表达式实现数据绑定。这是单向绑定吧？
  // 双向绑定：<input [(ngModel)]="todo.text">
})
// 定义组件类
export class AppComponent  { name = 'Angular'; }  
```


其中`{{name}}`变量是在浏览器端渲染。

值得注意的是这里的`template`。
Angular模板基于双向UI数据绑定。在模型改变时自动更新视图，以及在视图改变时自动更新模型。其HTML模板在浏览器中编译。
比如这里的`<h1>Hello {{name}}</h1>`。






# 工作流程


```yml
{
  "name": "angular-quickstart",
  "version": "1.0.0",
  "description": "QuickStart package.json from the documentation, supplemented with testing support",
  "scripts": {
    "build": "tsc -p src/", # 采用的tsc编译器，node自带的ts编译器。也可以采用webpack，
    "build:watch": "tsc -p src/ -w",
    "build:e2e": "tsc -p e2e/",  #  end-to-end tests.
    "serve": "lite-server -c=bs-config.json",  # 轻量级node静态文件服务器，默认会读取当前目录下的bs-config.js或者bs-config.json文件做为配置导入
    "serve:e2e": "lite-server -c=bs-config.e2e.json",
    "prestart": "npm run build",
    "start": "concurrently \"npm run build:watch\" \"npm run serve\"", #  runs the compiler and a server at the same tim
    "pree2e": "npm run build:e2e",
    "e2e": "concurrently \"npm run serve:e2e\" \"npm run protractor\" --kill-others --success first",
    "preprotractor": "webdriver-manager update",
    "protractor": "protractor protractor.config.js",
    "pretest": "npm run build",
    "test": "concurrently \"npm run build:watch\" \"karma start karma.conf.js\"",
    "pretest:once": "npm run build",
    "test:once": "karma start karma.conf.js --single-run",
    "lint": "tslint ./src/**/*.ts -t verbose"
  },
  "keywords": [],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "@angular/common": "~4.3.4",
    "@angular/compiler": "~4.3.4",
    "@angular/core": "~4.3.4",
    "@angular/forms": "~4.3.4",
    "@angular/http": "~4.3.4",
    "@angular/platform-browser": "~4.3.4",
    "@angular/platform-browser-dynamic": "~4.3.4",
    "@angular/router": "~4.3.4",
    "angular-in-memory-web-api": "~0.3.0",
    "systemjs": "0.19.40",
    "core-js": "^2.4.1",
    "rxjs": "5.0.1",
    "zone.js": "^0.8.4"
  },
  "devDependencies": {
    "concurrently": "^3.2.0",
    "lite-server": "^2.2.2",
    "typescript": "~2.1.0",
    "canonical-path": "0.0.2",
    "tslint": "^3.15.1",
    "lodash": "^4.16.4",
    "jasmine-core": "~2.4.1",
    "karma": "^1.3.0",
    "karma-chrome-launcher": "^2.0.0",
    "karma-cli": "^1.0.1",
    "karma-jasmine": "^1.0.2",
    "karma-jasmine-html-reporter": "^0.2.2",
    "protractor": "~4.0.14",
    "rimraf": "^2.5.4",
    "@types/node": "^6.0.46",
    "@types/jasmine": "2.5.36"
  },
  "repository": {}
}
```

# 疑问

1. 这个project，如何不依赖node，直接双击在浏览器运行？
1. 这里的{{name}}是绑定的js中写死的静态变量。如何绑定后台的一个动态变量？


# 其他angular入门教程

- 首推教程 Angular 2 教程 http://www.runoob.com/angularjs2/angularjs2-tutorial.html  可直接双击html执行
- Angular 4 教程 https://www.w3cschool.cn/angular/
