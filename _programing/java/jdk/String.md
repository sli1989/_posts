## fd

String s = “abc”,并没有在堆上生成对象
Object o = new Object() 对应字节码为:

    0: new           #2                  // class java/lang/Object
    3: dup           
    4: invokespecial #1                  // Method java/lang/Object."<init>":()V
    7: astore_1   
 
String s = "abc" 对应字节码为:

    0: ldc           #2                  // String abc
    2: astore_1  
 

String s = new String() 对应字节码为:

    0: new           #2                  // class java/lang/String
    3: dup           
    4: invokespecial #3                  // Method java/lang/String."<init>":()V
    7: astore_1  