---
title: webpack原理
date: 2018-03-25
tags: ["webpack","构建工具"]
---

webpack是一个js打包工具，不是一个完整的前端构建工具。它的流行得益于模块化和单页应用的流行。webpack提供扩展机制，在庞大的社区支持下各种场景基本它都可找到解决方案。






### webpack核心概念
- `entry` 一个可执行模块或库的入口文件。Webpack 执行构建的第一步将从 Entry 开始
- `Module`：模块，在 Webpack 里一切皆模块，一个模块对于着一个文件。Webpack 会从配置的 Entry 开始递归找出所有依赖的模块。
- `chunk` 多个文件组成的一个代码块，例如把一个可执行模块和它所有依赖的模块组合和一个 chunk 这体现了webpack的打包机制。
- `loader` 文件转换器，例如把es6转换为es5，scss转换为css。
- `plugin` 插件，用于扩展webpack的功能，在webpack构建生命周期的节点上加入扩展hook为webpack加入功能。

Webpack 启动后会从 Entry 里配置的 Module 开始递归解析 Entry 依赖的所有 Module。
每找到一个 Module 就会根据配置的 Loader 规则去找出对应的转换规则立即对 Module 进行转换后，再解析出当前 Module 依赖的 Module。
这些模块会以 Entry 为单位进行分组，一个 Entry 和其所有依赖的 Module 被分到一个组也就是一个 Chunk。最后 Webpack 会把所有的 Chunk 转换成文件输出。
在整个流程中 Webpack 会在恰当的时候执行 Plugin 里定义的逻辑。

## webpack构建流程

从启动webpack构建到输出结果经历了一系列过程，它们是：

1. 解析webpack配置参数，合并从shell传入和webpack.config.js文件里配置的参数，生产最后的配置结果。
1. 注册所有配置的插件，好让插件监听webpack构建生命周期的事件节点，以做出对应的反应。
1. 从配置的entry入口文件开始解析文件构建AST语法树，找出每个文件所依赖的文件，递归下去。
1. 在解析文件递归的过程中根据文件类型和loader配置找出合适的loader用来对文件进行转换。
1. 递归完后得到每个文件的最终结果，根据entry配置生成代码块chunk。
1. 输出所有chunk到文件系统。

需要注意的是，在构建生命周期中有一系列插件在合适的时机做了合适的事情，比如UglifyJsPlugin会在loader转换递归完后对结果再使用UglifyJs压缩覆盖之前的结果。

## webpack原理

1. 一切皆模块<br>
正如js文件可以是一个“模块（module）”一样，其他的（如css、image或html）文件也可视作模 块。因此，你可以require('myJSfile.js')亦可以require('myCSSfile.css')。这意味着我们可以将事物（业务）分割成更小的易于管理的片段，从而达到重复利用等的目的。
1. 按需加载<br>
传统的模块打包工具（module bundlers）最终将所有的模块编译生成一个庞大的bundle.js文件。但是在真实的app里边，“bundle.js”文件可能有10M到15M之大可能会导致应用一直处于加载中状态。因此Webpack使用许多特性来分割代码然后生成多个“bundle”文件，而且异步加载部分代码以实现按需加载。

## example

示例文件 webpack.config.js
```js
/**
 * @author: @AngularClass
 */

/**
 * Look in ./config folder for webpack.dev.js
 */
switch (process.env.NODE_ENV) {
  case 'prod':
  case 'production':
    module.exports = require('./config/webpack.prod')({env: 'production'});
    break;
  case 'test':
  case 'testing':
    module.exports = require('./config/webpack.test')({env: 'test'});
    break;
  case 'dev':
  case 'development':
  default:
    module.exports = require('./config/webpack.dev')({env: 'development'});
}
```

tsconfig.webpack.json
```yml
{
  "compilerOptions": {
    "target": "es5",
    "module": "es2015",
    "moduleResolution": "node",
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "allowSyntheticDefaultImports": true,
    "sourceMap": true,
    "noEmit": true,
    "noEmitHelpers": true,
    "importHelpers": true,
    "strictNullChecks": false,
    "lib": [
      "es2015",
      "dom"
    ],
    "baseUrl": ".",
    "paths": {
      "@angular/*": ["node_modules/@angular/*"]
    },
    "typeRoots": [
      "node_modules/@types"
    ],
    "types": [
      "hammerjs",
      "node"
    ]
  },
  "exclude": [
    "node_modules",
    "client/dist",
    "client/src/**/*.spec.ts",
    "client/src/**/*.e2e.ts"
  ],
  "awesomeTypescriptLoaderOptions": {
    "forkChecker": true,
    "useWebpackText": true
  },
  "angularCompilerOptions": {
    "genDir": "./compiled",
    "skipMetadataEmit": true
  },
  "compileOnSave": false,
  "buildOnSave": false,
  "atom": {
    "rewriteTsconfig": false
  }
}
```


## 参考

https://github.com/gwuhaolin/blog/issues/4

[深入浅出 Webpack](http://webpack.wuhaolin.cn/)


##
