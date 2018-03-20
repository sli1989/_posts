---
title: 开源密码管理工具

---


最棒的密码应该是长长的，任何可能的字符的随机或者伪随机组合，每个使用场景都用不同的密码。但对一个普通人而言怎么可能记住上百甚至上千个他们创建的独立的账户密码呢？简短的答案是：不能。甚至不管是在现实世界或者数码世界不应该明文记录下任何一个密码。

或许最简单地保存这些复杂、唯一密码的方法是使用密码管理器，它提供了一种访问这些强密码的简单方式。虽然像 LastPass 这样商业解决方案很受欢迎，但是还有一些开源方案。另外对于密码，可以审计你的密码管理器的源码也是很重要的，因为它可以确保你的密码被正确地加密，并且没有后门。

# 开源软件

开源软件，任何人都能审计它的代码，这样就增加了它的安全性。

选开源，还可以是不是看看源码。

## KeePass

KeePass 是一个 GPLv2 授权的密码管理器，主要设计用于 Windows ，但是同样可以在其它平台运行。KeePass 提供多个强加密选项、便于导出、多用户密钥、高级搜索特性等等。其为桌面用途设计，也有可以直接运行在浏览器中的插件，并且如果你想要在不同的机器间随身携带你的密码，它可以运行在 U 盘中。想要了解更多 KeePass 信息，你可以从在 Ricardo Frydman 的这篇旧贴中找到。

KeePassX，是 KeePass 的 Linux 移植版本，是另一个你可以考虑的项目。KeePassX 与 KeePass 2 密码文件兼容，并且已经被移植到不同的操作系统上。事实上，KeePass 的非官方版本列表覆盖了日常使用的所有系统。


尽管LastPass算是最好的密码管理器之一了，但有些人就是信不过云端的管理器。
KeePass能够把你的账号密码存储在本地，然后通过Dropbox传到云端，这样就能在多个设备上同步访问。
KeePass还支持多种加密方式，默认是AES-256加密，你也可以选择Twofish 256-bit加密。

https://github.com/keepassx/keepassx
插件： https://github.com/pfn/keepasshttp

## Padlock

Padlock 是一个最近新进的开源密码管理器。目前在 Windows、iOS、Android 上可用，Linux 版本正在开发中，Padlock 被设计成为了一个“极简风”的密码管理器。它的源码以 GPLv3 授权的形式发布在 Github 上。项目同样也正在开发一个云后端，同样是开源的，这对那些厌烦了管理密码文件或者在多台电脑间设置同步的人而言是一个很好的补充。


## Passbolt

Passbolt 是另一个相对较新的选择，它有 Firefox 和 Chrome 的插件，支持移动设备，还有正在开发的命令行。它基于 OpenPGP，你可以查看在线的一些功能演示（虽然这需要你安装浏览器插件）。以 AGPLv3 授权发布，你可以在 Github 上查看它的源码或者浏览一下项目的路线图来了解下目前和将来计划的功能。

使用一款你信任的密码管理器以及用复杂的密码并不能代替其他安全预防措施，它也不是万无一失的。但是对于许多用户而言，它是让你的数字生活保持安全的很重要的一部分。这些的确不是唯一的选择。还有一些更老的选择，比如 Clipperz 和 Password Safe，还有我有兴趣想尝试一下的基于 web 的工具 RatticDB。



# 与商业软件对比

## LastPass密码管理器(跨平台)

LastPass是个很出色的密码管理软件，它有拓展，有手机app，有桌面软件，能够支持所有浏览器和操作系统。

LastPass能够加密你的个人信息和账号密码，还提供多种两步验证方式。

Windows版的LastPass Password Manager免费使用，如果要使用指纹识别则需要购买高级版。



# 在线密码管理器

## passwords.google.com

 Chrome有一个内置的密码管理工具，能够存储你在用Chrome时的所有密码。所有的这些密码通过Google账号同步，在你各个设备的Chrome浏览器上都可使用。

##


# 评论

- 一直用Dropbox + KeePass 全平台同步，真的很推荐




# 参考
https://linux.cn/article-8055-1.html

https://www.howtogeek.com/240255/password-managers-compared-lastpass-vs-keepass-vs-dashlane-vs-1password/
