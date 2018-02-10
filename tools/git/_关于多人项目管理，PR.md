


利用branch管理自己的project和需要PR的project
> 主要目的也是为了不和自己的修改绞在一起产生混乱。比如我从next仓库fork到我自己的仓库，然后我做了一些只用于我自己的个性化修改，这时候我的master分支和远程master分支之间的变动越来越大了。
然后我碰到一个适用于所有人的变动，这时候想提交个pr，最好的方式显然是切换到远程master分支，然后做修改，之后提交到一个新的分支，再然后就可以去github上提交pr了，不会把自己master上的一些修改混到里面
不过如果自己master和远程master始终保持完全一致的话倒是可以直接提交到自己master上，然后直接用自己master分支提交pr   -- by tsanie




## 为什么要用branch，什么时候用？

比如next项目，我没权限，只能fork下来用。
如果不用branch，我在自己的master上修改，时间久了，与remote差异越来越大。我想更新功能，可以在remote上pull下来。但是我想提交change到remote呢，这就出问题了。因为提交commit首先要checkout到remote的master。

最好的方式是有一个branch跟remote同步，用这个branch与remote交互。

如果没有提交PR到remote的需求，可以不用branch。


### 说一下特殊情况。
我用两个git账号(俩仓库俩master)，一个做pull用，一个给remote提PR用。
那我是不是就没必要设置branch了。

## 如何pull remote到local？
Merging an upstream repository into your fork

https://help.github.com/articles/merging-an-upstream-repository-into-your-fork/


## 有冲突怎么办？
老简单了
https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/




##
