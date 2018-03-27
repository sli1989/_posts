---
title: java hotspot虚拟机 - init方法
date: 2017-02-02
keywords: ["java"]
---

## 初始化方法
在编译生成class文件时，会自动产生两个方法，一个是类的初始化方法<clinit>, 另一个是实例的初始化方法<init>
<clinit>：在jvm第一次加载class文件时调用，包括静态变量初始化语句和静态块的执行
<init>:在实例创建出来的时候调用，包括调用new操作符；调用Class或java.lang.reflect.Constructor对象的newInstance()方法；调用任何现有对象的clone()方法；通过java.io.ObjectInputStream类的getObject()方法反序列化。


## init的实现
是由jvm实现的，以下是hotspot jvm实现的版本

openjdk\hotspot\src\share\vm\oops\instanceKlass.cpp
openjdk\hotspot\src\share\vm\oops\instanceKlassKlass.cpp

为什么叫


## 名词解释
- oops原来不是Object Oriented Programming，实际指的是 Ordinary Object Pointer（普通对象指针）。它用来表示对象的实例信息，看起来像个指针实际上是藏在指针里的对象。而klass则包含 元数据和方法信息，用来描述Java类。

- Klass
- KlassKlass



## 参考



(见JVM规范8中的2.9节)
