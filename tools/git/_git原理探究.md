


- 核心思想: 观察.git目录的变化。



## git in git

如何方便的查看.git目录的变化？
一个简单的方式是利用git仓库本身，即git in git



### 流程

```bash
$ cd .git
$ git init
$

```

## 要探究的问题

index到底是什么东西？
多次index会自动合并为一个吗？还是会保留多次index的历史？

commit后到底是什么？


stash存到哪了？
