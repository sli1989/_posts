---
title: java系列 - Atomic
keywords:
  - java
abbrlink: 89c32f49
categories:
  - programing
  - lan
  - java
  - jdk
  - jdk
date: 2017-02-02 00:00:00
---
## 简介

- 原子量和普通变量相比，主要体现在读写的线程安全上。对原子量的是原子的(比如多线程下的共享变量i++就不是原子的)，由CAS操作保证原子性。对原子量的读可以读到最新值，由volatile关键字来保证可见性。
- 原子量多用于数据统计(如接口调用次数)、一些序列生成(多线程环境下)以及一些同步数据结构中


- atomic是基于底层硬件的CAS做的
- 区别于HashTable等线程安全类，这里面没有锁


## 以AtomicLong为例

### java源码

	// 1. from AtomicLong.java (rt.jar:java.util.concurrent.atomic.AtomicLong)
    public final boolean compareAndSet(long expect, long update) {
        return unsafe.compareAndSwapLong(this, valueOffset, expect, update);
    }

    // 2. from Unsafe.java (rt.jar:sun.misc.Unsafe)
    public final native boolean compareAndSwapLong(Object o, long offset, long expected, long x);

### native方法的C++实现

	// 3. from hotspot/src/share/vm/prims/unsafe.cpp (openjdk)
	static JNINativeMethod methods[] = {
	{CC"compareAndSwapLong", CC"("OBJ"J""J""J"")Z",      FN_PTR(Unsafe_CompareAndSwapLong)},
	...
	}
	...
	UNSAFE_ENTRY(jboolean, Unsafe_CompareAndSwapLong(JNIEnv *env, jobject unsafe, jobject obj, jlong offset, jlong e, jlong x))
	  UnsafeWrapper("Unsafe_CompareAndSwapLong");
	  Handle p (THREAD, JNIHandles::resolve(obj));
	  jlong* addr = (jlong*)(index_oop_from_field_offset_long(p(), offset));
	  if (VM_Version::supports_cx8())  
	    return (jlong)(Atomic::cmpxchg(x, addr, e)) == e;  // 主要实现
	  else { // 如果不支持cx8，那么就需要用到ObjectLocker锁
	    jboolean success = false;
	    ObjectLocker ol(p, THREAD);
	    if (*addr == e) { *addr = x; success = true; }
	    return success;
	  }
	UNSAFE_END

It is a JNI wrapper for the CAS API, with memory barriers for IA64 architecture.

It is an atomic operation which means no other processor can change the value of dest whilst the operation executes.

**Atomic::cmpxchg(x, addr, e)**
CAS需要三个参数 address,old_value, new_value.
modern CPU is required for this process.

CAS has its weakness as ABA problem, so memory barrier is necessary here to ensure the CAS is still correct in multithread environment.

- native的实现

### Atomic::cmpxchg方法的分支

依赖于OS & CPU & 32bit/64bit. 所以JVM在这里产生了分支

	// 4. from  hotspot/src/share/vm/runtime/atomic.cpp
	# include "atomic_windows_x86.inline.hpp"
	# include "atomic_linux_x86.inline.hpp"     // x86生产商有Intel, AMD, IBM等
	# include "atomic_solaris_sparc.inline.hpp" // Solaris系统，sparc处理器(都是sun的)
	# include "atomic_linux_sparc.inline.hpp"   // linux系统，sparc处理器
	...


linux_x86中：

	// from openjdk/hotspot/os_cpu/linux_x86/vm/atomic_linux_x86.inline.hpp
	#ifdef AMD64

	inline jlong    Atomic::cmpxchg    (jlong    exchange_value, volatile jlong*    dest, jlong    compare_value) {
	  bool mp = os::is_MP();
	  __asm__ __volatile__ (LOCK_IF_MP(%4) "cmpxchgq %1,(%3)"
	                        : "=a" (exchange_value)
	                        : "r" (exchange_value), "a" (compare_value), "r" (dest), "r" (mp)
	                        : "cc", "memory");
	  return exchange_value;
	}

	#else // !AMD64
	inline jlong    Atomic::cmpxchg    (jlong    exchange_value, volatile jlong*    dest, jlong    compare_value) {
	  return _Atomic_cmpxchg_long(exchange_value, dest, compare_value, os::is_MP());
	}
	#endif // AMD64


windows_x86中

	// from openjdk\hotspot\src\os_cpu\windows_x86\vm
	#ifdef AMD64
	inline jlong    Atomic::cmpxchg    (jlong    exchange_value, volatile jlong*    dest, jlong    compare_value) {
	  return (*os::atomic_cmpxchg_long_func)(exchange_value, dest, compare_value);
	}

	#else // !AMD64
	inline jlong    Atomic::cmpxchg    (jlong    exchange_value, volatile jlong*    dest, jlong    compare_value) {
	  int mp = os::is_MP();
	  jint ex_lo  = (jint)exchange_value;
	  jint ex_hi  = *( ((jint*)&exchange_value) + 1 );
	  jint cmp_lo = (jint)compare_value;
	  jint cmp_hi = *( ((jint*)&compare_value) + 1 );
	  __asm {
	    push ebx
	    push edi
	    mov eax, cmp_lo
	    mov edx, cmp_hi
	    mov edi, dest
	    mov ebx, ex_lo
	    mov ecx, ex_hi
	    LOCK_IF_MP(mp)
	    cmpxchg8b qword ptr [edi]
	    pop edi
	    pop ebx
	  }
	}
	#endif // AMD64

其他平台...




可以看出，当CPU支持时，最终确实是直接用cmpxchg相关指令实现的。


### ObjectLocker锁

这是synchronized锁吗？

## Why would you use a CAS function?


## 名词解释

- Solaris：原是太阳微系统公司研制的类Unix操作系统，在Sun公司被Oracle并购后，称作Oracle Solaris。早期的Solaris主要用于Sun工作站上

- saparc: sun公司开发的处理器，用于Sun工作站等上。Solaris在SPARC上拥有强大的处理能力和硬件支持(相对Intel x86平台)

- cx8:

- ObjectLocker:



## 疑问

- i = i + 1不是原子操作吗？为什么AtomicLong.incrementAndGet()的实现要这么复杂?直接用i = i + 1实现不行吗？(见《java并发编程实战》18页)

- \#include <atomic\> C++自带的实现与atomic_linux_x86.inline.hpp有什么区别？应该前者是后者的进一步封装吧？

- 这个native方法的实现为什么在JVM层而不在jdk层？JVM是用来run byte code的。这里的JVM代码是用来run哪个byte code呢？

- 这里生成的byte code是啥样的？


## 再挖掘




## 参考

- (http://stackoverflow.com/questions/7169961/can-anyone-interpret-this-c-code-from-openjdk6-into-plain-english)
