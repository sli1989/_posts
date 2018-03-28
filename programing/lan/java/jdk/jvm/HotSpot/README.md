## HotSpot Runtime Overview

This section introduces key concepts associated with the major subsystems of the HotSpot runtime system. The following topics are covered:

- Command-Line Argument Processing
- VM Lifecycle
- VM Class Loading
- Bytecode Verifier and Format Checker
- Class Data Sharing
- Interpreter
- Java Exception Handling
- Synchronization
- Thread Management
- C++ Heap Management
- Java Native Interface (JNI)
- VM Fatal Error Handling
- References
- Further Reading


		


## JNI

我目前比较关注JNI


## FAQ
OpenJDK VS OracleJDK
- Oracle JDK与OpenJDK里的JVM都是HotSpot VM。从源码层面说，两者基本上是同一个东西。

Oracle未公开的JVM包含
- Java Flight Recorder的内部实现，
- OpenJDK的其它平台的port，例如Oracle自己的ARM、PPC版HotSpot VM。


## download


HotSpot http://openjdk.java.net/groups/hotspot/

download:


如果不想下载，可以直接在http://hg.openjdk.java.net/ 上浏览源代码(选jdk,然后点browse)

##