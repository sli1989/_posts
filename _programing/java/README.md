## JVM JRE JDK java_language

他们的关系，见[java doc](http://docs.oracle.com/javase/7/docs/)

### JVM
- JVM is Java Virtual Machine -- the JVM actually runs Java bytecode.
- The JVM doesn't understand Java source code, that's why you compile your *.java files to obtain *.class files that contain the bytecodes understandable by the JVM. It's also the entity that allows Java to be a "portable language" (write once, run anywhere). Indeed there are specific implementations of the JVM for different systems (Windows, Linux, MacOS, see the wikipedia list..), the aim is that with the same bytecodes they all give the same results.
- Java 虚拟机是整个 Java 平台的基石，是 Java 技术用以实现硬件无关与操作系统无关的关键部分，是 Java 语言生成出极小体积的编译代码的运行平台，是保障用户机器免于恶意代码损害的保护屏障。
- Java 虚拟机可以看作是一台抽象的计算机。如同真实的计算机那样，它有自己的指令集以及
各种运行时内存区域。
- Java 虚拟机与 Java 语言并没有必然的联系，它只与特定的二进制文件格式——Class 文件格式所关联。
Class文件中包含了 Java 虚拟机指令集（或者称为字节码、 Bytecodes）和符号表，还有一些其他辅助信息。 (来自《java虚拟机规范》)
- 不仅使用 Java 编译器可以把 Java 代码编译成存储字节码的 Class 文件，使用 JRuby 等其他语言的编译器也可以把程序代码编译成 Class 文件，虚拟机并不关心 Class 的来源是什么语言，只要它符合一定的结构，就可以在 Java 中运行。

### JRE
- JRE is Java Runtime Environment -- is what you need to run a Java program and contains a JVM, among other things.
- The Java Runtime Environment (JRE) provides the libraries, the Java Virtual Machine, and other components to run applets and applications written in the Java programming language. In addition, two key deployment technologies are part of the JRE: Java Plug-in, which enables applets to run in popular browsers; and Java Web Start, which deploys standalone applications over a network. It is also the foundation for the technologies in the Java 2 Platform, Enterprise Edition (J2EE) for enterprise software development and deployment. The JRE does not contain tools and utilities such as compilers or debuggers for developing applets and applications.

### JDK
- JDK is Java Developer Kit -- the JDK is what you need to compile Java source code.
- The JDK is a superset of the JRE, and contains everything that is in the JRE, plus tools such as the compilers and debuggers necessary for developing applets and applications.


OpenJDK is a specific JDK implementation.


### openJDK

https://github.com/openjdk-mirror
http://hg.openjdk.java.net/jdk7u



## javac

疑问： java反编译，竟然能还原行号(还原空行)，还原变量名，好牛逼是吧。怎么做到的？



带着这些疑问，我们进入下面的学习。


### javac -help

	用法: javac <options> <source files>
	其中, 可能的选项包括:
	  -g                         生成所有调试信息
	  -g:none                    不生成任何调试信息
	  -g:{lines,vars,source}     只生成某些调试信息(注意这里,行号、变量名、)
	  -nowarn                    不生成任何警告
	  -verbose                   输出有关编译器正在执行的操作的消息
	  -deprecation               输出使用已过时的 API 的源位置
	  -classpath <路径>            指定查找用户类文件和注释处理程序的位置
	  -cp <路径>                   指定查找用户类文件和注释处理程序的位置
	  -sourcepath <路径>           指定查找输入源文件的位置
	  -bootclasspath <路径>        覆盖引导类文件的位置
	  -extdirs <目录>              覆盖所安装扩展的位置
	  -endorseddirs <目录>         覆盖签名的标准路径的位置
	  -proc:{none,only}          控制是否执行注释处理和/或编译。
	  -processor <class1>[,<class2>,<class3>...] 要运行的注释处理程序的名称; 绕过默
	认的搜索进程
	  -processorpath <路径>        指定查找注释处理程序的位置
	  -d <目录>                    指定放置生成的类文件的位置
	  -s <目录>                    指定放置生成的源文件的位置
	  -implicit:{none,class}     指定是否为隐式引用文件生成类文件
	  -encoding <编码>             指定源文件使用的字符编码
	  -source <发行版>              提供与指定发行版的源兼容性
	  -target <发行版>              生成特定 VM 版本的类文件
	  -version                   版本信息
	  -help                      输出标准选项的提要
	  -A关键字[=值]                  传递给注释处理程序的选项
	  -X                         输出非标准选项的提要
	  -J<标记>                     直接将 <标记> 传递给运行时系统
	  -Werror                    出现警告时终止编译
	  @<文件名>                     从文件读取选项和文件名


### eclipse的编译设置

compiler的设置可以点project->properties->java Compiler->configure workspace settings->compliances and classfiles

	1. Add variable attributes to generated class files (used by the debugger)
	将变量属性添加至生成的类文件（调试器需要）：
	 
	2. Add line number attributes to generated class files (used by the debugger)
	将行号属性添加至生成的类文件（调试器需要）：
	 
	3. Add source file name to generated class file (used by the debugger)
	将源文件名添加至生成的类文件（调试器需要）
	 
	4. Preserve unused (never read) local variables
	保留从未使用过的局部变量。


示例1

public class Test {
	int nice = 1;
	String good = "good";
	public static void main(String args[]) {
		int abc = 10;
		String bnice = "hi";
		{
			int cde = 1;
			String dfd = "ddd";
		}
		
	}

}


反编译出来的源代码(eclipse四个编译选项都不勾选)

	public class Test
	{
	  int nice = 1;
	  String good = "good";

	  public static void main(String[] paramArrayOfString)
	  {
	  }
	}

### 常见的编译&debug问题

- JDK source在debug的时候无法观察局部变量的值
    - sun对rt.jar中的类编译时,去除了部分调试信息(保留了行号，未保留变量名)导致debug进去看不到变量的值。如果在debug的时候想查看局部变量，就必须自己编译相应的源码使之拥有调试信息。

### 自己编译JDK(带debug信息)
编译rt.jar这一个就够了
教程链接：http://stackoverflow.com/questions/18255474/debug-jdk-source-cant-watch-variable-what-it-is
已测试，可用

### javap
常用反编译命令

javap a.class
javap -c a.class
javap -c -v a.class （能够输出常量池、）
javap 

## decompilers

### 解码器种类
CFR (supports Java 8)
Jadx, fast and with Android support
JDCore (very fast)
Procyon
Fernflower
JAD (very fast, but outdated)

### eclipse插件


Eclipse Class Decompiler integrates JD, Jad, FernFlower, CFR, Procyon seamlessly with Eclipse and allows Java developers to debug class files without source code directly. It also integrates Javadoc and supports the syntax of JDK8 lambda expressions.

### online decompiler
http://www.javadecompilers.com/ 反编译很牛b啊

## jd-gui
https://github.com/java-decompiler/jd-gui

## java监控管理控制台
jconsole

## comments

### 怎么感觉java要完蛋啊

- Android 是一個開源平台，是開源社群合作的結晶。
在下一版的 Android 中，我們計劃將 Java 語言庫換為以 OpenJDK 為基礎，開發一個通用代碼庫，方便開發者開發應用程式和服務。
Google 與 OpenJDK 有長期的合作，未來也會為它做更多貢獻。
- [谷歌安卓侵权Oracle Java](http://tech.sina.com.cn/zl/post/detail/it/2016-05-18/pid_8507499.htm)
- [Java EE 8停步不前](http://www.infoq.com/cn/news/2016/07/Java-EE-8-Stagnating)Oracle根本没兴趣为竞争对手做嫁衣，也不想共享自己的创新成果。
- [JAVA EE守护者联盟](https://javaee-guardians.io/)
- Oracle将OpenOffice捐赠给Apache基金会(https://zh.wikipedia.org/wiki/Apache_OpenOffice) 
ubuntu系统中自带的office以前是open office现在是libre office。
- [Oracle可能放弃Java EE，但不会放弃Java](http://info.ec.hc360.com/2016/07/091111871332.shtml)




### 疑问

## 扩展阅读