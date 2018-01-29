

## 先提问题





1. fork starter  # 可查看diff，可pull from master，可new branch
2. clone recursive
3. add submodule， theme-next (fork theme)
4. add submodule for source/post  // 作为自己的主blog仓库
5. add submodule for source/demos  // 可再包含多个submodule
5. add submodule for source/games  // 也许要独立layout，可再包含多个submodule


是不是fork的比较多，那么可以开一个github小号，管理这些fork。
github大号，只放deploy版本。

实例：我的小号。


**push** 每个module单独管理
**clone** 一次git clone --recursive 下载所有dev

## push
模块化 push

```bash
git clone --recursive git@github.com:xsung/hexo-starter.git blog
cd blog/themes/
git submodule add git@github.com:xsung/hexo-theme-next.git next

cd ..
git add .
git commit -m "add submodule hexo-theme-next"
git push -u origin master
# add other submodule

git submodule add git@github.com:xsung/2048.git


```

## 下载和部署。
so easy

```bash
$ git clone --recursive git@github.com:xsung/blog-dev.git blog
$ npm install hexo --save  # install node_modules dependency

$ hexo s

$ hexo d
```
hexo




## 优势

- 解耦合，模块化。各模块单独管理。比如博客一个仓库，每个game单独管理，每个demo单独管理。
- 最终整合为一个仓库，方便clone setup deploy。


## hexo

hexo本身就是模块化很好的例子。cli server分离，主hexo与theme分离。
