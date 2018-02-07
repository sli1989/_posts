
## 简介
java.lang.System.java


## 跟踪arraycopy

public static native void arraycopy(Object src,  int  srcPos, Object dest, int destPos, int length);


### System.c



	// jdk/src/share/native/java/lang/System.c

	/* Only register the performance-critical methods */
	static JNINativeMethod methods[] = {
	    {"currentTimeMillis", "()J",              (void *)&JVM_CurrentTimeMillis},
	    {"nanoTime",          "()J",              (void *)&JVM_NanoTime},
	    {"arraycopy",     "(" OBJ "I" OBJ "II)V", (void *)&JVM_ArrayCopy},
	};



### jvm.cpp

	// src/share/vm/prims/jvm.cpp

	JVM_ENTRY(void, JVM_ArrayCopy(JNIEnv *env, jclass ignored, jobject src, jint src_pos,
	                               jobject dst, jint dst_pos, jint length))
	  JVMWrapper("JVM_ArrayCopy");
	  // Check if we have null pointers
	  if (src == NULL || dst == NULL) {
	    THROW(vmSymbols::java_lang_NullPointerException());
	  }
	  arrayOop s = arrayOop(JNIHandles::resolve_non_null(src));
	  arrayOop d = arrayOop(JNIHandles::resolve_non_null(dst));
	  assert(s->is_oop(), "JVM_ArrayCopy: src not an oop");
	  assert(d->is_oop(), "JVM_ArrayCopy: dst not an oop");
	  // Do copy
	  Klass::cast(s->klass())->copy_array(s, src_pos, d, dst_pos, length, thread);
	JVM_END