---
title: "静态博客框架比较"
date: 2018-01-25 03:08:53
keywords: ["blog","framework","博客","框架"]
tags: ["blog","framework"]
categories:
- web
- blog-framework
---


## overview

比较流行的一些静态博客框架，比较流行的有Jekyll，Hexo，Simple，Octopress，Pelican以及Lo·gecho等等.



- **Hexo**（Node.js写的，编译速度比前两者快）<br>
优势：轻量静态博客，与以上相比速度更快，适合博客内容很多的用户。可以从多个平台（比如wp，joomla）移植博客。可以使用绝大多数octopress插件<br>
缺点：需要在本地更新博客 <br>
安装：较简单

- **Jekyll** 更活跃，github官方指定。像黑客一样写作。可以通过http://prose.io直接写博客。<br>
缺点： 模板基于liquid template engine，更改较复杂，安装稍复杂 <br>
**Jekyll的一个最大优势** ：Github自动构建和部署，用户基本只需维护md文件；而hexo等博客需要本地编译成html，然后再上传到Github。
<details>
  <summary>Github原文</summary>
  <p> Jekyll's simplified build process with GitHub Pages is one of the biggest advantages of using Jekyll instead of other static site generators. GitHub Pages manages your site's build process with a single push to your site's publishing branch.<br>
  -- 来自 Github官网 https://help.github.com/articles/about-github-pages-and-jekyll/</p>
</details>
- **Hakyll**   Haskell <br>
  示例：  http://colah.github.io <br>
  为什么都喜欢`ll`结尾？
- **Octopress** Jekyll的再开发

|             | jekyll | hexo  |
|-------------|--------|-------|
| contributor | 751    | 115   |
| star        | 32983  | 20441 |
|             |        |       |


搜索 hexo 迁移 jekll，搜到的都是
从Jekyll迁移到Hexo， why？

https://acris.me/ 的title字体



## 参考
- https://www.zhihu.com/question/21981094
- https://www.slant.co/topics/329/~best-solutions-for-a-personal-blog
