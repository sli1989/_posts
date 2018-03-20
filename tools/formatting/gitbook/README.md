
# setup

npm install gitbook-cli -g




# 常用命令
```sh
# install plugins from registry
gitbook install

$ gitbook init # 创建书。generate two files:README.md and SUMMARY.md.

$ gitbook buid # 编译为静态网页，实际上也是gitbook插件。默认编译到_book目录下

$ gitbook serve
```

# Gitbook目录结构
GitBook使用简单的目录结构。在 SUMMARY （即 SUMMARY.md 文件）中列出的所有 Markdown / Asciidoc 文件将被转换为 HTML。多语言书籍结构略有不同。

一个基本的 GitBook 电子书结构通常如下：


```sh
.
├── book.json  # 配置数据 (optional)
├── README.md  # 电子书的前言或简介 (required)
├── SUMMARY.md  # 电子书目录 (optional)
├── chapter-1/
| ├── README.md
| └── something.md
└── chapter-2/
  ├── README.md
  └── something.md
```

参考 https://www.imooc.com/article/22889

# ebook & PDF

生成pdf依赖calibre (其实只需要ebook-convert这个工具). 输出格式可以是 PDF, ePub 或 MOBI.

https://toolchain.gitbook.com/ebook.html

```sh
# Generate a PDF file
$ gitbook pdf ./ ./mybook.pdf

# Generate an ePub file
$ gitbook epub ./ ./mybook.epub

# Generate a Mobi file
$ gitbook mobi ./ ./mybook.mobi
```

# 插件

https://toolchain.gitbook.com/plugins/

安装 disqus 插件

# TODO

gitbook deploy 命令，自动部署到
