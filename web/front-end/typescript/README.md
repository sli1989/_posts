


# 简介

TypeScript 是 JavaScript 的强类型版本。然后在编译期去掉类型和特有语法，生成纯粹的 JavaScript 代码。由于最终在浏览器中运行的仍然是 JavaScript，所以 TypeScript 并不依赖于浏览器的支持，也并不会带来兼容性问题。

TypeScript大大提高了JavaScript的编程效率。

官方中文文档：https://zhongsp.gitbooks.io/typescript-handbook/content/


TypeScript提供了一些检查来保证安全以及帮助分析你的程序。


TypeScript提供了一些检查来保证安全以及帮助分析你的程序。

在某些情况下TypeScript没法确定某些值的类型。 那么TypeScript会使用 any 类型
代替。 这对代码转换来讲是不错，但是使用 any 意味着失去了类型安全保障，并
且你得不到工具的支持。

## 优点

- 强类型，可读性好


# 编译器

## tsc命令

```sh
$ npm install -g typescript
```

以上命令会在全局环境下安装 tsc 命令，安装完成之后，我们就可以在任何地方执行 tsc 命令了。

编译一个 TypeScript 文件很简单：
```sh
tsc hello.ts
```

## ts-loader

## awesome-typescript-loader
这是TypeScript loader for Webpack，简称 ATL

```sh
$ npm install awesome-typescript-loader source-map-loader
```

awesome-typescript-loader 是一个TypeScript的加载器，结合 source-map-loader 方便调试。在webpack中用到

`与ts-loader的区别`

# Typescript特性

ATL能够加速编译

## 编译期类型检查

```js
let isDone: boolean = false;  // let 关键字：块作用域。 var：可以在包含它们的函数外访问
isDone = 11;  // 编译器会提示 [ts] 不能将类型“11”分配给类型“boolean”
```

```js
let isDone = false;
isDone = 11;  // 编译器会提示 [ts] 不能将类型“11”分配给类型“boolean”
```

## 接口 & 继承

TypeScript的核心原则之一是对值所具有的结构进行类型检查。在TypeScript里，接口的作用就是为这些类型命名和
为你的代码或第三方代码定义契约。

# 缺陷

let isDone: boolean = false; 这样写看着多蛋疼。
对比
- boolean isDone = false  # 这就不是动态类型了
- var isDone = false  # 动态类型，但缺乏编译器检查

# 疑问

## 为什么javascript不融合typescript特征，比如编译期类型检查，继承等？



## python也没有编译期类型检查，是否也要加个python type script？


## ts后缀和tsx后缀什么区别？

jsx对应tsx

## js为什么不引入所有ts的特性？

当可选静态类型（接近）进入 ES 标准时，TS 基本就等于 JS 了

参考 https://www.zhihu.com/question/61398011
