---
title: java系列 - Collection Framework
keywords:
  - java
abbrlink: aca7a464
date: 2017-02-02 00:00:00
---
## Hierarchy

	Collection
	├List
	│├ArrayList
	│├LinkedList
	│└Vector
	│　└Stack
	├PriorityQueue
	├Set
	│├EnumSet 	 
	│├HashSet
	│├LinkedHashSet
	│├TreeSet
	└ArrayDeque

	！其中的Vector和Stack类现在已经极少使用。



## compare





| 类            | 同步(线程安全) | 随机访问    | 快速增删 | 存储空间 |  复杂度：增删改查，containsValue |  其他语言 |
| :--------     | --------:      | --------:        | --------:   |   --------:    |   --------:     | :--:      |
| Array       | ..          | Yes | O() | 最小 |
| ArrayList       | ..          | Yes | O() | 小 |  . |
| LinkedList | ..             |  No | O() | 大 | . | redis中的list采用双向链表实现
| Vector     | ..            |
| Stack      |
| Queue      |





class Stack<E> extends Vector<E>
interface Queue<E> extends Collection<E>


## 实例场景

排队：秒杀。FIFO，
消息队列：
频繁插入：采用linkedList
