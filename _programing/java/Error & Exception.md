## definition

- catch an error at compile time:  before you even try to run the program  (think in java)
-
## java framework


```java

Throwable─┬─Exception─┬─RuntimeException─┬─IndexOutOfBoundsException
          │           │                  ├─NullPointerException
          │           │                  │
          │           │                  │
          │           │                  │
          │           │                  │
          │           │                  │
          │           │                  │
          │           │                  └─
          │           │                  
          │           ├─ ReflectiveOperationException─┬─NoSuchMethodException
          │           │                               ├─ClassNotFoundException
          │           │                               └─IllegalAccessException
          │           │
          │           │
          │           │
          │           ├─IOException─┬─FileNotFoundException
          │           │             ├─EOFException
          │
          └─Error─┬─

```

|            | RuntimeException | non-RuntimeException               |
|------------|------------------|------------------------------------|
| checked    | ×                | √                                  |
| occur in   | runtime          | **runtime**                            |
| must catch | ×                | √                                  |
| caused by  | programmer,such as NullPointerException, IndexOutOfBoundsException        |  external, such as FileNotFoundException |
| thrown     | during the normal operation of JVM |  |


 Compile-Time Checking of Exceptions

## 设计思想

**RuntimeException**
一般情况下，不要捕获或声明RuntimeException。因为问题在于你的程序逻辑本身有问题，
如果你用异常流程处理了，反而让正常流程问题一直存在。
程序应该从逻辑角度尽可能避免这类异常的发生；

**non-RuntimeException**
RuntimeException之外的异常我们统称为非运行时异常。
从程序语法角度讲是必须进行处理的异常，如果不处理，程序就不能编译通过。

非运行时异常，编译期要做语法检查，即检查是否处理了catch。程序报Exception还是要运行期才能知道的。

An Exception is checked, and a RuntimeException is unchecked.

- A checked exception must be handled explicitly by the code (catch or throw)
- An un-checked exception does not need to be explicitly handled.


## ambiguous, common errors, common misconceptions

Is non-RuntimeException CompiletimeException in java framework?
No, non-RuntimeException would be checked in compile time. But the Exception occurs in run time.


## where did RuntimeException comes from

since JDK1.0


## new/reasonable framework

In my view, the RuntimeException should be renamed as CheckedException

- RuntimeException
  - CheckedException
  - UncheckedException
- CompiletimeException
 - ..




## reference
- 《The Java™ Language Specification》11.2  Compile-Time Checking of Exceptions











## other framework

1. <Java language specification 8>
> Some programming languages and their implementations react to such errors
by peremptorily terminating the program; other programming languages allow an
implementation to react in an arbitrary or unpredictable way. Neither of these
approaches is compatible with the design goals of the Java SE platform: to provide
portability and robustness.

> Instead, the Java programming language specifies that an exception will be thrown
when semantic constraints are violated and will cause a non-local transfer of control
from the point where the exception occurred to a point that can be specified by the
programmer.

2.



### python framework

reference: http://www.cnblogs.com/rubylouvre/archive/2011/06/22/2086644.html

### c++ framework
