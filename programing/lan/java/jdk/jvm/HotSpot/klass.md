---
title: java hotspot虚拟机 - class文件
keywords:
  - java
abbrlink: 3a5d7b99
date: 2017-02-02 00:00:00
---

## oop-klass model概述

HotSpot JVM并没有根据Java实例对象直接通过虚拟机映射到新建的C++对象，而是设计了一个oop-klass model。

当我们在写Java代码的时候，我们会面对着无数个接口，类，对象和方法。但我们有木有想过，Java中的这些对象、类和方法，在HotSpot JVM中的结构又是怎么样呢？HotSpot JVM底层都是C++实现的，那么Java的对象模型与C++对象模型之间又有什么关系呢？今天就来分析一下HotSpot JVM中的对象模型：oop-klass model，它们的源码位于openjdk-8/openjdk/hotspot/src/share/vm/oops文件夹内。

那么为何要设计这样一个一分为二的对象模型呢？这是因为HotSopt JVM的设计者不想让每个对象中都含有一个vtable（虚函数表），所以就把对象模型拆成klass和oop，其中oop中不含有任何虚函数，而klass就含有虚函数表，可以进行method dispatch。这个模型其实是参照的 Strongtalk VM 底层的对象模型。


jdk版本：openjdk-7-fcs-src-b147-27_jun_2011
源码路径：openjdk\hotspot\src\share\vm\oops\

在oopsHierarchy.hpp里定义了oop和klass各自的体系。
这是oop的体系：

	typedef class oopDesc*                            oop;
	typedef class   instanceOopDesc*            instanceOop;
	typedef class   methodOopDesc*                    methodOop;
	typedef class   constMethodOopDesc*            constMethodOop;
	typedef class   methodDataOopDesc*            methodDataOop;
	typedef class   arrayOopDesc*                    arrayOop;
	typedef class     objArrayOopDesc*            objArrayOop;
	typedef class     typeArrayOopDesc*            typeArrayOop;
	typedef class   constantPoolOopDesc*            constantPoolOop;
	typedef class   constantPoolCacheOopDesc*   constantPoolCacheOop;
	typedef class   klassOopDesc*                    klassOop;
	typedef class   markOopDesc*                    markOop;
	typedef class   compiledICHolderOopDesc*    compiledICHolderOop;

## 概述，代码架构
klass.cpp
oop.cpp
arrayKlass.cpp
arrayOop.cpp
instanceKlass.cpp
instanceOop.cpp  // #include "oops/oop.hpp"
methodKlass.cpp

// A methodOop represents a Java method.
// #include "oops/constantPoolOop.hpp"#include "oops/instanceKlass.hpp" #include "oops/oop.hpp"
methodOop.cpp  

methodDataKlass.cpp
methodDataOop.cpp
objArrayKlass.cpp
objArrayOop.cpp

symbol.cpp


## 一句话名词解释
- oop：
Ordinary Object Pointer（普通对象指针），oop.h中定义了oopDesc类(没有oop这个类)

oop* 有这个而东东啊

- Desc：
即Describe， {name}Desc classes describe the format of Java objects so the fields can be accessed from C++
- oopDesc:
oop对象的类型其实是oopDesc*。在Java程序运行的过程中，每创建一个新的对象，在JVM内部就会相应地创建一个对应类型的oop对象。各种oop类的共同基类为oopDesc类。

- oop-klass model：



### Klass
一个Klass对象代表一个类的元数据（相当于java.lang.Class对象）。它提供：
language level class object (method dictionary etc.)
provide vm dispatch behavior for the object

所有的函数都被整合到一个C++类中。
Klass对象的继承关系：xxxKlass <:< Klass <:< Metadata <:< MetaspaceObj

klass对象的布局如下：
来自klass.hpp

	// A Klass is the part of the klassOop that provides:
	//  1: language level class object (method dictionary etc.)
	//  2: provide vm dispatch behavior for the object
	// Both functions are combined into one C++ class. The toplevel class "Klass"
	// implements purpose 1 whereas all subclasses provide extra virtual functions
	// for purpose 2.

	// One reason for the oop/klass dichotomy in the implementation is
	// that we don't want a C++ vtbl pointer in every object.  Thus,
	// normal oops don't have any virtual functions.  Instead, they
	// forward all "virtual" functions to their klass, which does have
	// a vtbl and does the C++ dispatch depending on the object's
	// actual type.  (See oop.inline.hpp for some of the forwarding code.)
	// ALL FUNCTIONS IMPLEMENTING THIS DISPATCH ARE PREFIXED WITH "oop_"!

	//  Klass layout:
	//    [header        ] klassOop
	//    [klass pointer ] klassOop
	//    [C++ vtbl ptr  ] (contained in Klass_vtbl)
	//    [layout_helper ]
	//    [super_check_offset   ] for fast subtype checks
	//    [secondary_super_cache] for fast subtype checks
	//    [secondary_supers     ] array of 2ndary supertypes
	//    [primary_supers 0]
	//    [primary_supers 1]
	//    [primary_supers 2]
	//    ...
	//    [primary_supers 7]
	//    [java_mirror   ]
	//    [super         ]
	//    [name          ]
	//    [first subklass]
	//    [next_sibling  ] link to chain additional subklasses
	//    [modifier_flags]
	//    [access_flags  ]
	//    [verify_count  ] - not in product
	//    [alloc_count   ]
	//    [last_biased_lock_bulk_revocation_time] (64 bits)
	//    [prototype_header]
	//    [biased_lock_revocation_count]


### oop

oop类型其实是oopDesc*。在Java程序运行的过程中，每创建一个新的对象，在JVM内部就会相应地创建一个对应类型的oop对象。各种oop类的共同基类为oopDesc类。

JVM内部，一个Java对象在内存中的布局可以连续分成两部分：instanceOopDesc和实例数据。instanceOopDesc和arrayOopDesc又称为对象头。

instanceOopDesc对象头包含两部分信息：Mark Word 和 元数据指针(Klass*)：


	// from oop.hpp
	// oopDesc is abstract.
	// (see oopHierarchy for complete oop class hierarchy)
	class oopDesc {
	  friend class VMStructs;
	 private:
	  volatile markOop  _mark;  // mark word
	  union _metadata {    // metadata
	    wideKlassOop    _klass;
	    narrowOop       _compressed_klass;
	  } _metadata;
	  ...


- Mark word: // 存储对象的hashCode或锁信息等。
- Klass*  // 存储到对象类型数据的指针




## 基础知识：

### C++ vtbl pointer：

### 虚函数
ss



## 参考
[深入探究JVM | klass-oop对象模型研究](http://www.sczyh30.com/posts/Java/jvm-klass-oop/)
