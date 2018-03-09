

```sh
$ node -v
```


## nodejs

node.js是javascript的一种运行环境，是对Google V8引擎进行的封装。是一个服务器端的javascript的解释器。


Node 只是一个平台（platform），不是语言。



## npm

npm是Node.js的包管理工具（package manager）。
为啥我们需要一个包管理工具呢？因为我们在Node.js上开发时，会用到很多别人写的JavaScript代码。如果我们要使用别人写的某个包，每次都根据名称搜索一下官方网站，下载代码，解压，再使用，非常繁琐。于是一个集中管理的工具应运而生：大家都把自己开发的模块打包后放到npm官网上，如果要使用，直接通过npm安装就可以直接用，不用管代码存在哪，应该从哪下载。

更重要的是，如果我们要使用模块A，而模块A又依赖于模块B，模块B又依赖于模块X和模块Y，npm可以根据依赖关系，把所有依赖的包都下载下来并管理起来。否则，靠我们自己手动管理，肯定既麻烦又容易出错。


npm已经在Node.js安装的时候顺带装好了

### 对比其他包管理器

- npm在不使用-g参数时，默认把package安装在当前目录的node_modules下，`不会污染系统环境`。
- pip虽然可以指定安装目录，但是如果要换目录安装，你还需要更新配置文件（麻烦）。python的包安装要不污染环境，需要其它的工具实现。这样也有优势，可以共享，不占用磁盘空间。
  - 对于pip的使用，可以在virtualenv建立的虚拟环境下安装包，不会污染环境
- package.json的写起来比setup.py爽……

### npm和nodejs的关系
npm是nodejs的包管理工具，npm随nodejs一同安装 (从 Node.js 0.6.3 开始，npm 集成到了 Node.js 的安装包里面)

两者的关系相当于 pip -> python 或 gem -> ruby 或
maven 和 Java 之间的关系

##
