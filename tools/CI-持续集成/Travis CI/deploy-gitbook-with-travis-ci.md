---
title: 利用travis自动构建Gitbook静态页面，并自动部署到Github Page
tags:
  - travis
  - gitbook
  - 自动化部署
  - github pages
keywords:
  - travis
  - gitbook
  - github
  - 自动化部署
  - github pages
  - personal access token
abbrlink: a8e526f0
date: 2018-03-20 00:00:00
---

# 目的

实现 Gitbook - Github仓库 - Github Pages 三方同步。

- 修改Gitbook，实现 Github自动同步 + 自动部署静态页面到Github Pages
- 修改Github仓库，实现Gitbook自动同步 + 自动部署静态页面到Github Pages


Gitbook自身已经实现了与Github仓库的同步，现在的问题是，如何实现自动部署静态页面到Github Pages。

当然有很多实现方式，这里我们介绍利用Travis CI自动部署Github Pages。

# Travis CI


Travis CI原理就是当你每次提交commit到在github后，它会自动检测你的提交，同时根据的配置文件，生成一个Linux虚拟机来运行你的命令，通常这些命令用于测试，构建等。在我们的要求下，就可以用它运行一些hexo g d之类的命令来自动生成、部署我静态网页。

1. 博客提交修改后push到github
1. github通知travis ci项目需要构建
  - 这里需要配置：
1. travis ci立马安排构建
  - 这里需要.travis.yml
1. 构建完成后将结果push到github的gh-pages分支
  - 这里需要github访问权限。即personal access token
  - 把token设置到.travis.yml环境变量中，安全起见，最好加密
  - [travis环境变量的定义与加密](https://docs.travis-ci.com/user/environment-variables)
1. vps利用git钩子将结果部署到web容器


$ npm install travis-encrypt -g
$  travis-encrypt -r username/repository GH_TOKEN=[the token you created before] -a


$ travis-encrypt -r ESbook/TCP-IP GH_TOKEN=6ad73f4597162bf335caaeef3e1138b77645dd5c -a
# GH_TOKEN
XpJ36JE64TJCwGQ5ZxxWosn64Rhwq3OGOqNJhjKUyeGPlj9B+fNPAqBmP+YTLxB5nRpoLv5UsK62Qw15Of02iZcoO50H8qBrb2cWNEW3z2+Ih12JoeN5qJi4MTShT6ePbwH7Tvid27wosswuYH2+O4hvSQR13WwsHqCPDmzno6Zni+Unt8tya0etSkRqS81hKbHTItL0fOQiDpVIK2GrUioqPAbDV2TNBZfas8EENmSfZMRjHV6BYaOY/ZQg8qx3UuPSnGLU6pmiv9pcaiths4LNBoHb71+Rm87E+FffI6sHtmqrKn9NoW5sEsiiIAUusYQE5woQsn46+uc8lgjlx+1DGBxPstQwvTQNcu8HWzoN0lxlnIYMTWTj/aoUBmc90/Do1GPlpSP9/vONrU2ljfyfKlxxwbUdvHg8pvfU09QsWtTRAqfSjrH305nHOCPKWQgeYv0zbgTqRq/zKh5xTS+iaU6R+VscxFTCnktQaCG1oB6VMSBsU6YjvG5KcY7UZHiyF/fPTRFIH/LtT6iX9DpGlvc3NBb/mA4ERcEvMp/1Bgs7rqHVML+luhwKBwqeivilz0VRajK5JQxBmMeuJ4cDVt/yJuwGjf72chKa8Y909/iwAKm5wJ/FAEKvv7wl1aZJyOFdWEW6n/6u63+6VQy1YF/6aSodbkQcvO/o8qw=





git remote add origin 'https://f6884617cab7ada45740e5034604e3e82e4ac722@github.com/ESbook/TCP-IP.git'

博客：http://blog.csdn.net/qq8427003/article/details/64921201
应用实例 https://github.com/8427003/book/blob/master/deploy-to-github.sh

实例&博客：https://github.com/steveklabnik/automatically_update_github_pages_with_travis_example

博客：https://shawnho.me/2017/11/23/deploy-hexo-blog-with-travis-ci/

# 疑问

## 为什么要采用personal access token？为什么不采用ssh验证？

HTTPS URLs和SSH URLs对应的是两套完全独立的权限校验方式，主要的区别就是HTTPS URLs采用账号密码进行校验，SSH URLs采用SSH秘钥对进行校验。

采用personal access token的方式来访问gitub，目的是代替密码输入。

如果要采用ssh，需要把travis主机的ssh key加入到github中。这样确实能够方便部署，免密码验证，但是存在风险。因为travis主机是很多人共用的，同一个主机加很多github的ssh会存在多账户权限风险。（我猜的）。即使每个github账号对应一个虚机或者docker，不方便多主机CDN。

## 为什么要travis encrypt？
因为公开personal access token，就基本等同于公开github密码。任何人可以通过用户名+token获得github的相应权限，github中的项目有被恶意篡改，删除的风险。

travis encrypt对token进行加密，该密文仅travis能够识别。

##
