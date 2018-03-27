---
title: Angular快速入门教程 - Hello Angular
date: 2018-03-26
keywords: ["angular","front-end","前端架构"]
tags: ["angular","front-end","前端架构"]
---


## 教程



在 Angular 中，通过 Component 装饰器和自定义组件类来创建自定义组件。
创建 AppComponent 组件`./src/app/app.component.ts`
```js
import { Component } from '@angular/core';
// 定义组件的元信息
@Component({
  selector: 'my-app', // 用于定义组件在HTML代码中匹配的标签
  template: `<h1>Hello {{name}}</h1>`, // 定义组件内嵌视图。使用 {{}} 插值语法实现数据绑定(插值表达式)
})
// 定义组件类
export class AppComponent  { name = 'Angular'; }  
```



### 声明 AppComponent 组件



```js
import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';

@NgModule({
  imports:      [ BrowserModule ],
  declarations: [ AppComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
```

使用 AppComponent 组件


index.html入口
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Angular QuickStart</title>
    <base href="/">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="styles.css">

    <!-- Polyfill(s) for older browsers -->
    <script src="node_modules/core-js/client/shim.min.js"></script>

    <script src="node_modules/zone.js/dist/zone.js"></script>
    <script src="node_modules/systemjs/dist/system.src.js"></script>

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
