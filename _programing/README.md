
## 各种语言








| 编程语言   |  推出时间 |  features |pros  | cons| 强弱类型(隐式类型转换)|
| :-------- |  :--------| :--------| :--------|--------:| :--: |
| Objective-C  | 1980年 |     | |
| C     |   1972年 | | | |(char,short)->int->long->double<-float|
| C++		| 1985年 |    | |
| Python	 |	1991年 | dynamically typed|easy to read, less effort to write| |
| Java	|	1995年 || |  | 原始类型：(byte,short,char)-->int-->long-->float-->double 引用类型一般不能隐式类型转换(toString是特例)|
| JavaScript | 1995年 | ||
| Php	|	1995年 | | |
| Ruby	|	1995年 | | |
| C#		| 2000年 | | |
| haskell| | | | |  int不能转double|
| Node.js	|	2009年 || | |


- python范式，python思想，http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#other-languages-have-variables


## 强类型 弱类型 静态类型 动态类型
 轮子哥 知乎
强类型：偏向于不容忍隐式类型转换。譬如说haskell的int就不能变成double
弱类型：偏向于容忍隐式类型转换。譬如说C语言的int可以变成double
静态类型：编译的时候就知道每一个变量的类型，因为类型错误而不能做的事情是语法错误。
动态类型：编译的时候不知道每一个变量的类型，因为类型错误而不能做的事情是运行时错误。譬如说你不能对一个数字a写a[10]当数组用。


编程模式通常分为命令式编程（imperative style programs）和符号式编程（symbolic style programs）。
命令式编程容易理解和调试，命令语句基本没有优化，按原有逻辑执行。符号式编程涉及较多的嵌入和优化，不容易理解和调试，但运行速度有同比提升。


C语言：可以说堪称简陋，除了指针还是指针，但其却可能是对于计算机底层的最佳抽象。
ObjC：谁能想到它会在iOS编程上焕发第二春呢？
C++：最大而全的编程语言，刚刚发布了C++14标准。
Python：可能是最好的入门语言，脚本语言。
Java：自诞生以来可以说是久经考验，本来是考虑为嵌入式设备语言，结果却在Web中大放异彩。J2ME被唾弃了之后，一个新的分支Android却蓬勃发展。本来是缺点的古板编程风格，却在服务器领域大受欢迎。再加上Java似乎与生俱来的就与开源为伴，Apache，Spring等优秀开源组织不断的为Java添砖加瓦。本来极慢的性能，随着JIT技术的发展，Java成了扩展性极佳的一个解决方案。
JavaScript：可能是使用人数最多的编程语言。
Php：一个被人唾弃的编程语言，但是却简单粗暴的有效。
Ruby：一个特性上考虑的很完备的语言，但是却感觉没有发展起来？也许是受end的影响？
C#：一个语言特性上好Java好几条街的语言，还有VS神器加持，最近似乎也开源了，但是其影响力却似乎还是比不过Java？
Node.js：又是一个非常牛的编程语言，也许能代替Php？（大雾）



## 反编译

- 高级语言与机器语言不是一一对应的, 所以将EXE文件反编译成C++语言, 或其它任何的高级语言, 原则上都是不可能的.反汇编成汇编语言是可能的, 不过现在的程序都这么复杂而庞大, 即使你懂汇编语言, 也不可能看懂全部的程序. 查看特定的代码是可以的.

- 有pdb基本等于开源。有map等于开源了一半。。

- C++、C语言一般不能反编译为源代码，只能反编译为asm（汇编）语言，因为C较为底层，编译之后不保留任何元信息，而计算机运行的二进制实际上就代表了汇编指令，所以反编译为汇编是较为简单的。

- C#、Java这类高级语言，尤其是需要运行环境的语言，如果没有混淆，非常容易反编译。原因很简单，这类语言只会编译为中间语言（C#为MSIL，Java为Bytecode），而中间语言与原语言本身较为相似，加上保留的元信息（记录类名、成员函数等信息）就可以反向生成源代码，注意是由反编译器生成，不会与源代码完全相同，但可以编译通过。这些特性本来是为反射技术准备的，却被反编译器利用，现在的C#反编译器ILSpy甚至可以反向工程

- Java最主流的源码编译器，javac，基本上不对代码做优化，只会做少量由Java语言规范要求或推荐的优化；也不做任何混淆，包括名字混淆或控制流混淆这些都不做。这使得javac生成的代码能很好的维持与原本的源码/AST之间的对应关系。换句话说就是javac生成的代码容易反编译。

- Java Class文件含有丰富的符号信息。而且javac默认的编译参数会让编译器生成行号表，这些都有助于了解对应关系。（本来是为反射技术准备的）

- 并不是不能被反编译，只是还没发明一个通用的反编译算法。


[app可以被反编译到什么程度？] (https://www.zhihu.com/question/30723538)
[C不容易反编译,C#、Java容易反编译](https://www.zhihu.com/question/21853681)

## 语言大战

- [What are the best programming languages to learn today?](https://www.quora.com/What-are-the-best-programming-languages-to-learn-today?redirected_qid=3115216)
- [Python & Java: A Side-by-Side Comparison](https://pythonconquerstheuniverse.wordpress.com/2009/10/03/python-java-a-side-by-side-comparison/)
- [JAVA真的这么落后没用吗](https://www.zhihu.com/question/27533938)
- [Java已经过时了吗？](http://robbin.iteye.com/blog/96925)
- [Python做Web开发已经过时了吗？](https://www.zhihu.com/question/40120818)

##

| Item      |    Value | Qty  |
| :-------- | --------:| :--: |
| Computer  | 1600 USD |  5   |
| Phone     |   12 USD |  12  |
| Pipe      |    1 USD | 234  |
