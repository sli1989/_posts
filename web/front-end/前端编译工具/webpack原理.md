---
title: webpack原理
date: 2018-03-25
---

webpack是一个js打包工具，不一个完整的前端构建工具。它的流行得益于模块化和单页应用的流行。webpack提供扩展机制，在庞大的社区支持下各种场景基本它都可找到解决方案。本文的目的是教会你用webpack解决实战中常见的问题。




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
```json
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


## webpack原理


### webpack核心概念
- `entry` 一个可执行模块或库的入口文件。
- `chunk` 多个文件组成的一个代码块，例如把一个可执行模块和它所有依赖的模块组合和一个 chunk 这体现了webpack的打包机制。
- `loader` 文件转换器，例如把es6转换为es5，scss转换为css。
- `plugin` 插件，用于扩展webpack的功能，在webpack构建生命周期的节点上加入扩展hook为webpack加入功能。
