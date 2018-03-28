---
title: 关于Monkey Patch猴子补丁
keywords: ["mokey patch","猴子补丁"]
---

# 简介

## 定义

以下是维基百科对猴子补丁的定义

> The term monkey patch refers to dynamic modifications of a class or module at runtime, motivated by the intent to patch existing third-party code as a workaround to a bug or feature which does not act as desired.

<!-- 在动态语言中， -->
所谓的猴子补丁，是指在运行时修改类或模块，而不去改变源码，达到hot patch的目的。

猴补丁（英语：Monkey patch）是一种很脏的编程技巧，用拼凑代码的方法修改程序逻辑。

Monkey patching 只能在动态语言中实现。比如Python类的方法其实也只是一个属性，方便运行时修改，所以用Python做猴子补丁非常方便。

Changing a method at runtime instead of updating the object definition is one example。


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

## 简单示例

### 对属性 打补丁
以下来自wikpedia示例。
利用猴子补丁，动态修改math标准库中Pi的默认值。(这里仅修改了attributes，也可以对某些method进行重写)

```py
>>> import math
>>> math.pi
3.141592653589793
>>> math.pi = 3  # 给标准库打补丁，即运行时修改math的pi属性
>>> math.pi
3
>>> ================================ RESTART ================================
>>> import math
>>> math.pi
3.141592653589793
```

### 对方法 打补丁
```py
class Foo(object):
    def bar(self):
        print 'Foo.bar'

def bar(self):  # 这是补丁
    print 'Modified bar'

Foo().bar()
Foo.bar = bar  # 给Foo的bar方法打补丁，即运行时修改类的方法
Foo().bar()
```
由于Python中的名字空间是开放，通过dict来实现，所以很容易就可以达到patch的目的。


## 实际应用案例

## socket的热补丁

用过gevent就会知道,会在最开头的地方gevent.monkey.patch_all();把标准库中的thread/socket等给替换掉.这样我们在后面使用socket的时候可以跟平常一样使用,无需修改任何代码,但是它变成非阻塞的了.

## SQL注入攻击

网页和数据库

## Zope、Plone中的安全补丁

> In Zope and Plone, security patches are often delivered using dynamic class modification, but they are called hot fixes.
> -- wikipedia

很多安全补丁也是一种猴子补丁，只不过叫法不同而已。

## Eventlet Patcher

现在我们先来看一下eventlet中的Patcher的调用代码吧，这段代码对标准的ftplib做monkey patch，将eventlet的GreenSocket替换标准的socket。

```py
from eventlet import patcher  
# *NOTE: there might be some funny business with the "SOCKS" module  
# if it even still exists  
from eventlet.green import socket  
patcher.inject('ftplib', globals(), ('socket', socket))  
del patcher  
```

Eventlet中大量使用了该技巧，以替换标准库中的组件，比如socket。

未完待续，参考 https://blog.csdn.net/seizef/article/details/5732657

## 从Gevent学习猴子补丁的设计

异步协程工具Gevent是python上面最有名也支持面最广通用性最好的协程工具,它底层基于greenlet,而且可以通过使用猴子补丁将标准库中的同步模块自动的转换成异步.同时他也提供了方便的并发模型和常用的web服务器工具.

gevent能够 修改标准库里面大部分的阻塞式系统调用，包括socket、ssl、threading和 select等模块，而变为协作式运行。

```py
>>> import socket
>>> print(socket.socket)     # monkey patch前
<class 'socket._socketobject'>
>>>
>>> from gevent import monkey # monkey patch后
>>> monkey.patch_socket()
>>> print(socket.socket)
<class 'gevent._socket2.socket'>  # 改变了标准socket库

>>> import select        # monkey patch前
>>> print(select.select)  #  select()轮询的阻塞调用
<built-in function select>
>>>
>>> monkey.patch_select() # monkey patch后
>>> print(select.select) # select()轮询的异步调用
<function select at 0x7fb8a7239d70>
```

例如，Redis的python绑定一般使用常规的tcp socket来与redis-server实例通信。 通过简单地调用gevent.monkey.patch_all()，可以使得redis的绑定协作式的调度 请求，与gevent栈的其它部分一起工作。

这让我们可以将一般不能与gevent共同工作的库结合起来，而不用写哪怕一行代码。 虽然猴子补丁仍然是邪恶的(evil)，但在这种情况下它是“有用的邪恶(useful evil)”。

### patch_all

除了socket外,gevent还可以为其他的模块打补丁,一起打补丁可以使用

patch_all(socket=True, dns=True, time=True, select=True, thread=True, os=True, ssl=True, httplib=False,subprocess=True, sys=False, aggressive=True, Event=False, builtins=True, signal=True) 函数

我们可以看到像socket,dns,time,selectthread,os, ssl, httplib,subprocess, sys, aggressive, Event, builtins, signal模块都可以打上补丁,打上以后,他们就是非阻塞的了.


### 核心协程模块greenlet

```py
import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)  # 这行的作用是什么？
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
```
输出
```py
Running in foo
Explicit context to bar
Explicit context switch to foo again
Implicit context switch back to bar
[<Greenlet at 0x7fb8a72c3eb0>, <Greenlet at 0x7fb8a72c3a50>]
```

### `gevent.sleep`与`time.sleep`的区别
- gevent is a cooperative analog to the threading module. When using gevent.sleep it you would never use time.sleep.  So no example is needed.

- time.sleep would suspend the entire process, blocking all greenlet threads.

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

### C



### C++

C++ 类有哪个方法是编译时确定好的, 没法打开类, 对象属于哪个类是 new 对象的代码确定好的, 既然 new 的代码在编译时确定了, 再载入补丁库也修改不了 (除非搞缓冲区溢出攻击...)

比如python中可以math.Pi=3。

### java

java强大的反射，即使`属性`或`方法`被设置为了`private final`也可以动态更改。讲道理也可以动态补丁。


### 总结

不是脚本语言的专利……是语言设计留不留口的问题？

## 猴子补丁的坑


# 参考
- [Monkey patch | wikipedia](https://en.wikipedia.org/wiki/Monkey_patch)
- [what-is-monkey-patching | StackOverflow](https://stackoverflow.com/questions/5626193/what-is-monkey-patching)
- 待看 《松本行弘的程序世界》专门有一章讲了猴子补丁的设计
- [猴子补丁是动态语言的专利么？](https://ruby-china.org/topics/17619)
- [猴子补丁和热更新](http://blog.hszofficial.site/TutorialForPython/%E5%85%83%E7%BC%96%E7%A8%8B/%E7%8C%B4%E5%AD%90%E8%A1%A5%E4%B8%81%E5%92%8C%E7%83%AD%E6%9B%B4%E6%96%B0.html)
