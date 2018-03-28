---
title: java系列 - Thread
date: 2017-02-02
keywords: ["java"]
---

## 疑问

### Java的线程是如何创建的，是直接调用OS的API，还是有自己的“抽象线程”？
java线程是映射到操作系统的内核线程上的

## 跟踪Thread.start()

java

	// Thread.java
	public synchronized void start() {
	    group.add(this);
	    ...
        start0();
        ...
	}

	private native void start0();


native方法hotspot源码

	// openjdk\jdk\src\share\native\java\lang\Thread.c
	static JNINativeMethod methods[] = {
	    {"start0",           "()V",        (void *)&JVM_StartThread},
	   ...
	};


	// openjdk\hotspot\src\share\vm\prims\jvm.cpp
	JVM_ENTRY(void, JVM_StartThread(JNIEnv* env, jobject jthread))
	  JVMWrapper("JVM_StartThread");
	  JavaThread *native_thread = NULL;
	  ...
	  native_thread = new JavaThread(&thread_entry, sz); // 重点
	  ...
	  Thread::start(native_thread); // 重点
	JVM_END



	// openjdk\hotspot\src\share\vm\runtime\thread.cpp
	JavaThread::JavaThread(ThreadFunction entry_point, size_t stack_sz) :
	  Thread() {
	   ...
	   os::create_thread(this, thr_type, stack_sz);
	   // 可以看出java线程是映射到操作系统的内核线程上的
	   ...
	}

	void Thread::start(Thread* thread) {
		...
	    os::start_thread(thread);
	  }
	}


	// 在hotspot\src\os目录下可以看到windows, linux, solaris和posix的实现，先检查linux\vm\os_linux.cpp

	bool os::create_thread(Thread* thread, ThreadType thr_type, size_t stack_size) {
	  ...
	  int ret = pthread_create(&tid, &attr, (void* (*)(void*)) java_start, thread);  // linux中调用的pthread，POSIX中的api
	  ...
	}
