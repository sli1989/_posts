---
title: 关于Monkey Patch猴子补丁
keywords: ["mokey patch","猴子补丁"]
---

# 简介

## 定义
以下是维基百科对猴子补丁的定义
> The term monkey patch refers to dynamic modifications of a class or module at runtime, motivated by the intent to patch existing third-party code as a workaround to a bug or feature which does not act as desired.


所谓的猴子补丁，是指在动态语言中，不去改变源码而对功能进行动态(运行时)修改，达到hot patch的目的。

Monkey patching 只能在动态语言中实现。比如Python类的方法其实也只是一个属性，方便运行时修改，所以用Python做猴子补丁非常方便。

Changing a method at runtime instead of updating the object definition is one example。

为什么？静态语言不行呢。
比如java里

## 名字来源

1，这个词原来为Guerrilla Patch，杂牌军、游击队，说明这部分不是原装的，在英文里guerilla发音和gorllia(猩猩)相似，再后来就写了monkey(猴子)。
2，还有一种解释是说由于这种方式将原来的代码弄乱了(messing with it)，在英文里叫monkeying about(顽皮的)，所以叫做Monkey Patch。


<!-- Applications -->
# 示例/应用场景

维基百科总结了4种应用场景

- Replace methods / attributes / functions at runtime, e.g. to stub out a function during testing;
- Modify/extend behaviour of a third-party product without maintaining a private copy of the source code;
- Apply a patch at runtime to the objects in memory, instead of the source code on disk;
- Distribute security or behavioural fixes that live alongside the original source code (an example of this would be distributing the fix as a plugin for the Ruby on Rails platform).

## wikpedia示例

利用猴子补丁，动态修改math标准库中Pi的默认值。(这里仅修改了attributes，也可以对某些method进行重写)

```python
>>> import math
>>> math.pi
3.141592653589793
>>> math.pi = 3
>>> math.pi
3
>>> ================================ RESTART ================================
>>> import math
>>> math.pi
3.141592653589793
```

## SQL注入攻击

网页和数据库

## Zope、Plone中的安全补丁

> In Zope and Plone, security patches are often delivered using dynamic class modification, but they are called hot fixes.
> -- wikipedia

很多安全补丁也是一种猴子补丁，只不过叫法不同而已。



# 从Gevent学习猴子补丁的设计


Eventlet中大量使用了该技巧，以替换标准库中的组件，比如socket。

## 猴子补丁 与 SocketIO

用过gevent就会知道,会在最开头的地方gevent.monkey.patch_all();把标准库中的thread/socket等给替换掉.这样我们在后面使用socket的时候可以跟平常一样使用,无需修改任何代码,但是它变成非阻塞的了.

我看到猴子补丁，是从Gevent中看到的。SocketIO服务器发送数据，浏览器端并非实时接收，而是批量接收 (跟过马路有点像，凑够一波发送一次)。

这里涉及到buffer和flush。

- https://github.com/miguelgrinberg/Flask-SocketIO/issues/106
- https://github.com/miguelgrinberg/Flask-SocketIO/issues/141


没看懂的部分，后面再看。
>  That is really the only way to make this work when you use gevent, threading is cooperative so you have to release the CPU so that other tasks associated with the server get a chance to run and flush the messages. Any chance you haven't monkey patched the standard library?
> --- Flask-SocketIO的作者miguelgrinberg link

## 猴子补丁与 import json,

之前做的一个游戏服务器,很多地方用的import json,后来发现ujson比自带json快了N倍,于是问题来了,难道几十个文件要一个个把import json改成import ujson as json吗?
其实只需要在进程startup的地方monkey patch就行了.是影响整个进程空间的.
同一进程空间中一个module只会被运行一次.

# 习题

## 猴子补丁是动态语言的专利么？

使用猴子补丁的条件主要是可以打开类、可以重定义现有属性、方法。修改类方法的指针，或者属性

### C++

C++ 类有哪个方法是编译时确定好的, 没法打开类, 对象属于哪个类是 new 对象的代码确定好的, 既然 new 的代码在编译时确定了, 再载入补丁库也修改不了 (除非搞缓冲区溢出攻击...)

比如python中可以math.Pi=3。

### java
类的静态属性和方法，只要不定义为final，也能动态更改啊。

# 参考
- [Monkey patch | wikipedia](https://en.wikipedia.org/wiki/Monkey_patch)
- [what-is-monkey-patching | StackOverflow](https://stackoverflow.com/questions/5626193/what-is-monkey-patching)
- 待看 《松本行弘的程序世界》专门有一章讲了猴子补丁的设计
- [猴子补丁是动态语言的专利么？](https://ruby-china.org/topics/17619)
