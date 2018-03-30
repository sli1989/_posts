---
title: java系列 - Map
keywords:
  - java
abbrlink: 8748fd7b
categories:
  - programing
  - lan
  - java
  - jdk
  - jdk
date: 2017-02-02 00:00:00
---
## dd

| 类            | 同步(线程安全) | order            | key可为null | implementation |  复杂度：增删改查，containsValue |  其他语言 |
| :--------     | --------:      | --------:        | --------:   |   --------:    |   --------:     | :--:      |
| HashMap       | No             |  无序            | Yes         | hash table （采用seperate chaining解决键冲突）    |  O(1), 顺序查找O(n)   | redis的字典
| LinkedHashmap | No             |  按插入顺序排序  | Yes  key和value都可以       | 同上     |
| Hashtable     | Yes            |  无序            | No  key和value都不可以        | 同上     |
| TreeMap       |                |  按key自定义排序 |             | Red-Black tree() |   O(log n),  |
| WeakHashMap   | | | |
| EnumMap   | | | |





HashTable使用Enumeration，HashMap使用Iterator。
HashTable中hash数组默认大小是11，增加的方式是 old*2+1。HashMap中hash数组的默认大小是16，而且一定是2的指数。

6.哈希值的使用不同，HashTable直接使用对象的hashCode，代码是这样的：
int hash = key.hashCode();
int index = (hash & 0x7FFFFFFF) % tab.length;
而HashMap重新计算hash值，而且用与代替求模：
int hash = hash(k);
int i = indexFor(hash, table.length);

static int hash(Object x) {
　　int h = x.hashCode();

　　h += ~(h << 9);
　　h ^= (h >>> 14);
　　h += (h << 4);
　　h ^= (h >>> 10);
　　return h;
}
static int indexFor(int h, int length) {
　　return h & (length-1);
}
以上只是一些比较突出的区别，当然他们的实现上还是有很多不同的，比如
HashMap对null的操作
