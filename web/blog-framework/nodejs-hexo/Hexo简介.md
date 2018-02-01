---
title: Hexo简介
date: 2018-01-25 03:08:53
tag: ["hexo"]
categories:
- web
- blog-framework
---

## Hexo剖析

中文文档：https://hexo.io/zh-cn/docs/
官方主题库：https://hexo.io/themes/
next主题：https://github.com/theme-next


## Hexo原理综述

markdown到html的旅程
- 模板渲染
- 模板渲染


## hexo文件结构


```python
├── _config.yml     # 站点配置文件
├── db.json     # database
├── node_modules  # 安装的插件以及hexo所需的一些node.js模块
├── package.json  # 应用程序信息，配置hexo运行需要的js包
├── public     # deploy时生成，最终所见网页的所有内容
├── scaffolds  # 模板文件夹，hexo默认包含以下三种布局(layout)    https://hexo.io/zh-cn/docs/writing.html
│     ├──draft.md   # hexo new draft <title> 会在source/_drafts目录下生成md文件
│     ├──page.md  # hexo new page <title> 在source目录下
│     └──post.md   # hexo new post <title>  在source/_posts目录下生成md文件
├── source    # 资源文件夹。除 posts 文件夹之外，开头命名为 (下划线)的文件 / 文件夹和隐藏的文件将会被忽略。Markdown 和 HTML 文件会被解析并放到 public 文件夹，而其他文件会被拷贝过去。
│     ├── _draft  # 除 _posts 文件夹之外，开头命名为 _ (下划线)的文件 / 文件夹和隐藏的文件将会被忽略
│     └── _posts  #
│             └──  hello-world.md
└── themes   #主题文件夹
      ├──
      └──next
          ├──
          ├──
          ├──
          ├──

```


## 详解clean

```sh
$ hexo clean --debug

INFO  Deleted database.       # 清空 db.json
INFO  Deleted public folder.  # 删除public目录
```

## 详解hexo g
每次运行 hexo g 命令，hexo(node.js程序)会遍历你的 source 目录，建立索引，根据你 theme 文件夹的主题生成页面到 public 文件夹。这时 public 文件夹就是一个纯由 html javascript css 等内容制作的博客，而这些恰好能在 git pages 识别



## 详解deploy

最后 hexo d 将 public 文件夹的内容复制到临时目录，以 git 方式 push 到 github 的指定项目的指定分支，由 github 进行显示


首次deploy
```sh
$ hexo d --debug

# 1. 首先加载plugin和theme
DEBUG Config loaded: ~/xs/blog/_config.yml
DEBUG Plugin loaded: hexo-generator-category

# 2. 开始转化html
INFO  Start processing

# 2.1 处理404页面
DEBUG Processed: source/404.html  # 404不需要theme
DEBUG Processed: 404.html

# 2.2 加载主题，处理source目录下的.md .html
DEBUG Theme config loaded.
DEBUG Processed: _config.yml  # 这个也需要处理？
DEBUG Processed: source/css/main.styl  # 处理source目录下所有文件，包括js image md
DEBUG Processed: layout/archive.swig   # 处理layout languages等

DEBUG Generator: page  # 还包括post category archive index tag

# 3. 生成html，存储在public目录
INFO  Files loaded in 796 ms  #
DEBUG Rendering page: 404.html
DEBUG Rendering post: 2018/01/25/hello-world/index.html
DEBUG Rendering archive: archives/index.html
DEBUG Rendering index: index.html

# 4. deploy: 创建git repo，在public中拷贝文件，并push
INFO  Deploying: git
Initialized empty Git repository   # git init
INFO  Copying files from public folder...  # 从public复制到.deploy_git目录
INFO  Copying files from extend dirs...
INFO  Deploy done: git  # commit & push 已完成
DEBUG Database saved

```

## 详解hexo server


hexo s --debug


## hexo的模板引擎,Rendering HTML

模板引擎的作用，就是将界面与数据分离。最简单的原理是将模板内容中指定的地方替换成数据，实现业务代码与逻辑代码分离。

source 文件夹理解为数据库，而theme文件夹相当于 界面。 hexo g 就将我们的数据和界面相结合生成静态文件 public。

Hexo 的模板引擎是默认使用 ejs 编写的，同类型的东西还有很多，比如jade，swig。

next选用的swig

##




## reference
http://coderunthings.com/2017/08/20/howhexoworks/
