---
title: java系列 - Object
keywords:
  - java
abbrlink: 1c98e0dc
categories:
  - programing
  - lan
  - java
  - jdk
  - jdk
date: 2017-02-02 00:00:00
---
## 架构

- Object.java(rt.jar) 调用 jdk的native方法(Object.c)。
- native方法 调用hotspot jvm的方法(jvm.cpp)。

## Object.java

- java source版本：oracle 1.7

Object 还有隐形的构造函数.
new Object();
new Object[int]; // 在ArrayList的构造函数中用到了

疑问：
###  为什么Object.java中看不到构造函数
编译器为它生成了构造函数
### 为什么在stack trace中看不到调用Object.<init>


有7个native方法。

- private static native void registerNatives();
- protected native Object clone() throws CloneNotSupportedException;
- public final native Class<?> getClass();
- public native int hashCode();
- public final native void notify();
- public final native void notifyAll();
- public final native void wait(long timeout) throws InterruptedException;


- 但是构造函数是怎样实现的呢？(见jvm目录的init.md)


由于Object类中有JNI方法调用，按照JNI的规则，应当生成JNI 的头文件。
在此目录下执行javah -jni java.lang.Object 指令，将生成一个java_lang_Object.h头文件(自动生成的header，没什么意义)




## Object.c

- source版本：openjdk-7-fcs-src-b147-27_jun_2011
- 路径: openjdk\jdk\src\share\native\java\lang\Object.c
- 没有Object.h

Object.c

    /*-
     *      Implementation of class Object
     *
     *      former threadruntime.c, Sun Sep 22 12:09:39 1991
     */

    #include <stdio.h>
    #include <signal.h>
    #include <limits.h>

    #include "jni.h"
    #include "jni_util.h"
    #include "jvm.h"

    #include "java_lang_Object.h"

    // JVM_这些函数是在jvm.c中实现的
    static JNINativeMethod methods[] = {
        {"hashCode",    "()I",                    (void *)&JVM_IHashCode},  //  返回int
        {"wait",        "(J)V",                   (void *)&JVM_MonitorWait}, // 返回void，参数是long
        {"notify",      "()V",                    (void *)&JVM_MonitorNotify},  // 返回void
        {"notifyAll",   "()V",                    (void *)&JVM_MonitorNotifyAll}, // 返回void
        {"clone",       "()Ljava/lang/Object;",   (void *)&JVM_Clone}, // 返回Ojbect
    };

    JNIEXPORT void JNICALL
    Java_java_lang_Object_registerNatives(JNIEnv *env, jclass cls)
    {
        (*env)->RegisterNatives(env, cls,
                                methods, sizeof(methods)/sizeof(methods[0]));
    }

    JNIEXPORT jclass JNICALL
    Java_java_lang_Object_getClass(JNIEnv *env, jobject this)
    {
        if (this == NULL) {
            JNU_ThrowNullPointerException(env, NULL);
            return 0;
        } else {
            return (*env)->GetObjectClass(env, this);
        }
    }

其中JNINativeMethod的结构体如下:

    typedef struct {
        char *name; // Java中函数的名字
        char *signature; // signature 方法签名，描述了函数的参数和返回值
        void *fnPtr;  // native实现的函数指针，指向C函数
    } JNINativeMethod;



## 跟踪 hashcode



    // jvm.h 路径: openjdk\hotspot\src\share\vm\prims\jvm.h
    JNIEXPORT jint JNICALL
    JVM_IHashCode(JNIEnv *env, jobject obj);


    // jvm.cpp 路径: openjdk\hotspot\src\share\vm\prims\jvm.cpp
    JVM_ENTRY(jint, JVM_IHashCode(JNIEnv* env, jobject handle))
      JVMWrapper("JVM_IHashCode");
      // as implemented in the classic virtual machine; return 0 if object is NULL
      return handle == NULL ? 0 : ObjectSynchronizer::FastHashCode (THREAD, JNIHandles::resolve_non_null(handle)) ;
    JVM_END


FastHashCode才是真正计算hashcode的代码

### FastHashCode
这是hashCode()的具体实现

    // 路径: openjdk\hotspot\src\share\vm\runtime\synchronizer.cpp

    intptr_t ObjectSynchronizer::FastHashCode (Thread * Self, oop obj) {
      if (UseBiasedLocking) {
        // NOTE: many places throughout the JVM do not expect a safepoint
        // to be taken here, in particular most operations on perm gen
        // objects. However, we only ever bias Java instances and all of
        // the call sites of identity_hash that might revoke biases have
        // been checked to make sure they can handle a safepoint. The
        // added check of the bias pattern is to avoid useless calls to
        // thread-local storage.
        if (obj->mark()->has_bias_pattern()) {
          // Box and unbox the raw reference just in case we cause a STW safepoint.
          Handle hobj (Self, obj) ;
          // Relaxing assertion for bug 6320749.
          assert (Universe::verify_in_progress() ||
                  !SafepointSynchronize::is_at_safepoint(),
                 "biases should not be seen by VM thread here");
          BiasedLocking::revoke_and_rebias(hobj, false, JavaThread::current());
          obj = hobj() ;
          assert(!obj->mark()->has_bias_pattern(), "biases should be revoked by now");
        }
      }

      // hashCode() is a heap mutator ...
      // Relaxing assertion for bug 6320749.
      assert (Universe::verify_in_progress() ||
              !SafepointSynchronize::is_at_safepoint(), "invariant") ;
      assert (Universe::verify_in_progress() ||
              Self->is_Java_thread() , "invariant") ;
      assert (Universe::verify_in_progress() ||
             ((JavaThread *)Self)->thread_state() != _thread_blocked, "invariant") ;

      ObjectMonitor* monitor = NULL;
      markOop temp, test;
      intptr_t hash;
      markOop mark = ReadStableMark (obj);

      // object should remain ineligible for biased locking
      assert (!mark->has_bias_pattern(), "invariant") ;

      if (mark->is_neutral()) {
        hash = mark->hash();              // this is a normal header 对象的hashcode存储在对象头里
        if (hash) {                       // if it has hash, just return it 注意这里有个cache，对于同一个Ojbect，第一次调用Object.hashCode将会执行实际的计算并记入cache，以后直接从cache中取出。
          return hash;
        }
        hash = get_next_hash(Self, obj);  // allocate a new hash code
        temp = mark->copy_set_hash(hash); // merge the hash code into header
        // use (machine word version) atomic operation to install the hash
        test = (markOop) Atomic::cmpxchg_ptr(temp, obj->mark_addr(), mark);
        if (test == mark) {
          return hash;
        }
        // If atomic operation failed, we must inflate the header
        // into heavy weight monitor. We could add more code here
        // for fast path, but it does not worth the complexity.
      } else if (mark->has_monitor()) {
        monitor = mark->monitor();
        temp = monitor->header();
        assert (temp->is_neutral(), "invariant") ;
        hash = temp->hash();
        if (hash) {
          return hash;
        }
        // Skip to the following code to reduce code size
      } else if (Self->is_lock_owned((address)mark->locker())) {
        temp = mark->displaced_mark_helper(); // this is a lightweight monitor owned
        assert (temp->is_neutral(), "invariant") ;
        hash = temp->hash();              // by current thread, check if the displaced
        if (hash) {                       // header contains hash code
          return hash;
        }
        // WARNING:
        //   The displaced header is strictly immutable.
        // It can NOT be changed in ANY cases. So we have
        // to inflate the header into heavyweight monitor
        // even the current thread owns the lock. The reason
        // is the BasicLock (stack slot) will be asynchronously
        // read by other threads during the inflate() function.
        // Any change to stack may not propagate to other threads
        // correctly.
      }

      // Inflate the monitor to set hash code
      monitor = ObjectSynchronizer::inflate(Self, obj);
      // Load displaced header and check it has hash code
      mark = monitor->header();
      assert (mark->is_neutral(), "invariant") ;
      hash = mark->hash();  // 取出缓存
      if (hash == 0) {
        hash = get_next_hash(Self, obj);  // 实际计算
        temp = mark->copy_set_hash(hash); // merge hash code into header
        assert (temp->is_neutral(), "invariant") ;
        test = (markOop) Atomic::cmpxchg_ptr(temp, monitor, mark);
        if (test != mark) {
          // The only update to the header in the monitor (outside GC)
          // is install the hash code. If someone add new usage of
          // displaced header, please update this code
          hash = test->hash();
          assert (test->is_neutral(), "invariant") ;
          assert (hash != 0, "Trivial unexpected object/monitor header usage.");
        }
      }
      // We finally get the hash
      return hash;
    }


### get_next_hash -- 这才是核心代码
又调用的get_next_hash()

    // 路径: openjdk\hotspot\src\share\vm\runtime\synchronizer.cpp
    static inline intptr_t get_next_hash(Thread * Self, oop obj) {
      intptr_t value = 0 ;
      if (hashCode == 0) {
         // This form uses an unguarded global Park-Miller RNG,
         // so it's possible for two threads to race and generate the same RNG.
         // On MP system we'll have lots of RW access to a global, so the
         // mechanism induces lots of coherency traffic.
         value = os::random() ;
      } else
      if (hashCode == 1) {
         // This variation has the property of being stable (idempotent)
         // between STW operations.  This can be useful in some of the 1-0
         // synchronization schemes.
         intptr_t addrBits = intptr_t(obj) >> 3 ;
         value = addrBits ^ (addrBits >> 5) ^ GVars.stwRandom ;
      } else
      if (hashCode == 2) {
         value = 1 ;            // for sensitivity testing
      } else
      if (hashCode == 3) {
         value = ++GVars.hcSequence ;
      } else
      if (hashCode == 4) {
         value = intptr_t(obj) ;
      } else {
         // Marsaglia's xor-shift scheme with thread-specific state
         // This is probably the best overall implementation -- we'll
         // likely make this the default in future releases.
         unsigned t = Self->_hashStateX ;
         t ^= (t << 11) ;
         Self->_hashStateX = Self->_hashStateY ;
         Self->_hashStateY = Self->_hashStateZ ;
         Self->_hashStateZ = Self->_hashStateW ;
         unsigned v = Self->_hashStateW ;
         v = (v ^ (v >> 19)) ^ (t ^ (t >> 8)) ;
         Self->_hashStateW = v ;
         value = v ;
      }

      value &= markOopDesc::hash_mask;
      if (value == 0) value = 0xBAD ;
      assert (value != markOopDesc::no_hash, "invariant") ;
      TEVENT (hashCode: GENERATE) ;
      return value;
    }


hashCode()并不是简单的返回内存地址。
OpenJDK一共实现了5中不同的计算hash值的方法，通过
这段代码中hashCode进行切换。其中hashCode == 4的是直接使用地址的（前面的实验说明OpenJDK默认情况下并没有使用这种方式，或许可以通过运行/编译时参数进行选择）。

###


### 结论

前面通过JNI验证已经能够得到很显然的结论，hashCode返回的并不一定是对象的（虚拟）内存地址，具体取决于运行时库和JVM的具体实现。






## 跟踪wait


    JNIEXPORT void JNICALL
    JVM_MonitorWait(JNIEnv *env, jobject obj, jlong ms);


    // 路径: openjdk\hotspot\src\share\vm\prims\jvm.cpp
    JVM_ENTRY(void, JVM_MonitorWait(JNIEnv* env, jobject handle, jlong ms))
      JVMWrapper("JVM_MonitorWait");
      Handle obj(THREAD, JNIHandles::resolve_non_null(handle));
      assert(obj->is_instance() || obj->is_array(), "JVM_MonitorWait must apply to an object");
      JavaThreadInObjectWaitState jtiows(thread, ms != 0);
      if (JvmtiExport::should_post_monitor_wait()) {
        JvmtiExport::post_monitor_wait((JavaThread *)THREAD, (oop)obj(), ms);
      }
      ObjectSynchronizer::wait(obj, ms, CHECK);
    JVM_END

## 跟踪notify

    JNIEXPORT void JNICALL
    JVM_MonitorNotify(JNIEnv *env, jobject obj);


    // 路径: openjdk\hotspot\src\share\vm\prims\jvm.cpp
    JVM_ENTRY(void, JVM_MonitorNotify(JNIEnv* env, jobject handle))
      JVMWrapper("JVM_MonitorNotify");
      Handle obj(THREAD, JNIHandles::resolve_non_null(handle));
      assert(obj->is_instance() || obj->is_array(), "JVM_MonitorNotify must apply to an object");
      ObjectSynchronizer::notify(obj, CHECK);
    JVM_END

## 跟踪clone


    JNIEXPORT jobject JNICALL
    JVM_Clone(JNIEnv *env, jobject obj);


    // 路径: openjdk\hotspot\src\share\vm\prims\jvm.cpp
    JVM_ENTRY(jobject, JVM_Clone(JNIEnv* env, jobject handle))
      JVMWrapper("JVM_Clone");
      Handle obj(THREAD, JNIHandles::resolve_non_null(handle));
      const KlassHandle klass (THREAD, obj->klass());
      JvmtiVMObjectAllocEventCollector oam;


## 跟踪 getClass

## 跟踪



### 参考
http://blog.csdn.net/xusiwei1236/article/details/45152201

## byte code

- 通过编译后的jar包(即class文件)，查看byte code.
- 运行 javap -c java.lang.Object > a.txt，得到以下的byte code

如果执行不成功，看看是否把jdk的lib加入到了classpath:


    Compiled from "Object.java"
    public class java.lang.Object {
      public java.lang.Object();  // 什么都不干？不需要调用<init>吗？
        Code:
           0: return        

      public final native java.lang.Class<?> getClass();

      public native int hashCode();

      public boolean equals(java.lang.Object);
        Code:
           0: aload_0       
           1: aload_1       
           2: if_acmpne     9
           5: iconst_1      
           6: goto          10
           9: iconst_0      
          10: ireturn       

      protected native java.lang.Object clone() throws java.lang.CloneNotSupportedException;

      public java.lang.String toString();
        Code:
           0: new           #1                  // class java/lang/StringBuilder
           3: dup           
           4: invokespecial #2                  // Method java/lang/StringBuilder."<init>":()V           // 注意这里，调用了<init>
           7: aload_0       
           8: invokevirtual #3                  // Method getClass:()Ljava/lang/Class;
          11: invokevirtual #4                  // Method java/lang/Class.getName:()Ljava/lang/String;
          14: invokevirtual #5                  // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
          17: ldc           #6                  // String @
          19: invokevirtual #5                  // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
          22: aload_0       
          23: invokevirtual #7                  // Method hashCode:()I
          26: invokestatic  #8                  // Method java/lang/Integer.toHexString:(I)Ljava/lang/String;
          29: invokevirtual #5                  // Method java/lang/StringBuilder.append:(Ljava/lang/String;)Ljava/lang/StringBuilder;
          32: invokevirtual #9                  // Method java/lang/StringBuilder.toString:()Ljava/lang/String;
          35: areturn       

      public final native void notify();

      public final native void notifyAll();

      public final native void wait(long) throws java.lang.InterruptedException;

      public final void wait(long, int) throws java.lang.InterruptedException;
        Code:
           0: lload_1       
           1: lconst_0      
           2: lcmp          
           3: ifge          16
           6: new           #10                 // class java/lang/IllegalArgumentException
           9: dup           
          10: ldc           #11                 // String timeout value is negative
          12: invokespecial #12                 // Method java/lang/IllegalArgumentException."<init>":(Ljava/lang/String;)V
          15: athrow        
          16: iload_3       
          17: iflt          26
          20: iload_3       
          21: ldc           #13                 // int 999999
          23: if_icmple     36
          26: new           #10                 // class java/lang/IllegalArgumentException
          29: dup           
          30: ldc           #14                 // String nanosecond timeout value out of range
          32: invokespecial #12                 // Method java/lang/IllegalArgumentException."<init>":(Ljava/lang/String;)V
          35: athrow        
          36: iload_3       
          37: ldc           #15                 // int 500000
          39: if_icmpge     52
          42: iload_3       
          43: ifeq          56
          46: lload_1       
          47: lconst_0      
          48: lcmp          
          49: ifne          56
          52: lload_1       
          53: lconst_1      
          54: ladd          
          55: lstore_1      
          56: aload_0       
          57: lload_1       
          58: invokevirtual #16                 // Method wait:(J)V
          61: return        

      public final void wait() throws java.lang.InterruptedException;
        Code:
           0: aload_0       
           1: lconst_0      
           2: invokevirtual #16                 // Method wait:(J)V
           5: return        

      protected void finalize() throws java.lang.Throwable;
        Code:
           0: return        

      static {};
        Code:
           0: invokestatic  #17                 // Method registerNatives:()V
           3: return        
    }




C:\Program Files\java\jdk1.7.0_67\jre\lib\rt>

## 其他
* object header: it's JVM dependent， 具体参考JVM


## 扩展阅读

- [Object.hashCode()的返回值到底是不是对象内存地址](http://www.voidcn.com/blog/xusiwei1236/article/p-35249.html)
