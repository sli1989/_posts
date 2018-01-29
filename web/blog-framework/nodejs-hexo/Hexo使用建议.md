---
title: hexo使用建议
tag: ["hexo"]
---


## 核心思想

- 利用submodule管理blog  
> 模块化，解耦合，易整合。hexo本身就是模块化很好的例子。cli server分离，主hexo与theme分离。
- 先fork再add submodule


**细节**
主仓库
- `themes/` 每个theme是一个子仓库
- `source/post/`设置为一个子仓库
- `source/demos/`下包含多个子仓库
- `source/games`下包含多个子仓库


**模块搭建&整合流程**

```bash
# 1. fork hexo-starter 作为blog主仓库
$ git clone --recursive git@github.com:xsung/hexo-starter.git blog

# 2. fork theme & add submodule
$ cd blog/themes/
$ git submodule add git@github.com:xsung/hexo-theme-next.git next

# 3. fork _post & add submodule
$ git submodule add git@github.com:xsung/_posts.git


# 4. fork project-u-like & add submodule
$ mkdir blog/source/games/ && cd blog/source/games/
$ git submodule add git@github.com:xsung/2048.git

# 5. push到blog主仓库 (整合)
cd blog/
git commit -m "add submodules hexo-theme-next source/_post games/2048"
git push -u origin master

```

> Note: 如果你嫌fork太多，那么可以开一个github小号，管理这些fork。
github主账号只放deploy版本。

实例：
- [x] [Dev Repository](https://github.com/xsung/blog-dev/)
- [x] [Deployed Repository](https://github.com/xu-song/xu-song.github.io/) is deployed by Hexo from `Dev Repository`
- [x] [Demo Site](http://xusong.vip) hosts the `Deployed Repository`


## push (提交更改)
- 每个module独立push
```bash
# 1. commit changes from all submodules (e.g. _posts)
$ cd _posts
$ commit & push

# 2. commit changes from blog-dev
$ cd blog
$ commit & push
```


## pull & merge (整合)

```bash
# 2. pull latest of all git submodules
$ cd blog
$ git submodule update --recursive --remote  # 这个命令会造成HEAD detached
$ git pull --recurse-submodules
# reference https://stackoverflow.com/questions/1030169/easy-way-to-pull-latest-of-all-git-submodules

```

## clone & deploy
```bash
$ git clone --recursive git@github.com:xsung/blog-dev.git blog
$ npm install hexo --save  # install node_modules dependency
$ hexo s
$ hexo d
```
