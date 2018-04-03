

hexo-renderer-pandoc


# 简介

## pandoc是什么？

pandoc是一个标记语言(也可以说排版语言)转换器。可以将一种标记语言(如markdown、textile、tex、latex、html、epub等)转换到另一种标记语言。

常见的markdown引擎有
- markdown_strict (original unextended markdown) 原生markdown
- pandoc’s extended markdown
- markdown_phpextra (PHP Markdown Extra extended markdown)
- markdown_github (github extended markdown) 即GFW(Github Flavored Markdown)
- markdown_mmd (MultiMarkdown)。


hexo markdown渲染引擎和mathjax冲突问题，因此安装hexo-renderer-pandoc。这会替换掉hexo自带的markdown引擎。

这个插件依赖pandoc




```
pandoc -s -o output.html source/_posts/demo/test.md
```


## 其他类似插件

hexo-math和hexo-renderer-mathjax来实现，


## 常见错误

### 1.

```sh
$ pandoc -s -o output.html OSM-export-plain-text.txt
pandoc: YAML header is not an object "source" (line 130, column 1)
pandoc: YAML header is not an object "source" (line 17, column 1)
$
```

原因是文档内部有`---`，会与front matter的符号混淆。应该跟插件无关，是pandoc的原因。

参考：https://github.com/olivierkes/manuskript/issues/124


##
