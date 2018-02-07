## introduction

目的：完整分析class文件。

## java源码

	package MyTest;

	public class SimpleClass {
		void dfd() {
			int i;
			for (i = 0; i < 100; i++) {
			; // Loop body is empty
			}
		}
	}



## class文件 16进制

编译得到MyTest.class



	cafe babe  | 0000   0033      000c                   
	magic num  | minor0  major51  常量池计数器11+1=12  

	//////////// 常量池 /////////////

	#1  07     0002
		class  #2 

	#2	01     0012         4d79 5465 7374 2f53 696d 706c 6543 6c61 7373  
		utf8   length=18    MyTest/SimpleClass                            |  |

	#3	07     0004  
		class  #4           // java/lang/Object   
	 
	#4	01     0010         6a61 7661 2f6c 616e 672f 4f62 6a65 6374 |
		utf8   lengh16      java/lang/Object                        |

	#5	01     0006         3c 696e 6974 3e     
		utf8   length=6     <init>

	#6	01     0003         2829 56
		utf8   length=3     ()V

	#7	01     0004         436f 6465 
		utf8   length=3     Code

	#8	0a     000300       09
		md_ref #3.          #9  //  java/lang/Object."<init>":()V

	#9	0c     0005         0006 
		nam&ty #5           #6   //  "<init>":()V

	#10	01     0003         64 6664 
		utf8   length=3     dfd

	#11	01     000d         53 7461 636b 4d61 7054 6162 6c65 
		utf8   length=13    StackMapTable

	//////////// 常量池 /////////////

	0021               0001         0003
	可能是public       #1 类索引    #3 父类索引

	// 0x0021=0x0001|0x0020 也即ACC_PUBLIC 和 ACC_SUPER为真，其中ACC_PUBLIC大家好理解，ACC_SUPER是jdk1.2之后编译的类都会带有的标志。

	0000            
	接口计数器      接口表

	0000       
	fields_count 

	0002 
	methods_count

	//////////////// 第一个method void <init>  ///////////

	0001     0005       0006
	public   #5<init>   #6()V      其值为()V，表示<init>方法没有参数和返回值, 其实这是编译器自动生成 的实例构造器方法

	0001            
	attrib_count    

	0007        00000011     0001       0001        00000005     2ab70008b1  0000                    0000
	#7Code属性  attrib_len   max_stack  max_locals  code_length  code[]      exception_table_length  attribute_count
	// 代码是存储在Class文件中的method的code属性的code[]数组中

	                    

	//////////////// 第二个method dfd()  ///////////

	0000              000a     0006
	没写access_flag   #10,dfd  ()V

	0001 
	attrib_count

	0007        00000028       0002       0002        0000000f          033ca700068401011b1064a1fffab1  
	#7Code属性  属性表的长度   max_stack  max_locals  code_length=15    code[]，解析见《jvm spec》41页

	0000
	exception_table_length

	0001 
	attribute_count

	000b                  00000007   0002              fc00 0501 0200 00
	#11:StackMapTable     length     num_of_entries    7个length的stack_map_frame





## 疑问

.和：是怎么区分的？


## 其他阅读

http://coolshell.cn/articles/9229.html






