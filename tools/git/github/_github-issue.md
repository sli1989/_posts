
每一次 commit 都可以选择性的与某个 issue 关联。比如在 message 中添加 #n，就可以与第 n 个 issue 进行关联。
commit message title, #1


官方doc  https://guides.github.com/features/issues/



By prefacing your commits with
- “Fixes”,
- “Fixed”,
- “Fix”,
- “Closes”,
- “Closed”,
- “Close”
- resolve
- resolves
- resolved

when the commit is merged into master, it will also automatically close the issue.


## 常用标签

Labels，标签。包括 enhancement、bug、invalid 等，表示 issue 的类型，解决的方式。除了自带的以外，也可以去自定义。

Milestone，里程碑。几经修改后，它现在已经与git tag和Github release区分开来，仅仅作为issue的一个集合。通常用来表示项目的一个阶段，比如demo、release等，保护达成这些阶段需要解决的问题。有时候，也会与版本计划重合，比如v1.0、v2.0等。issue不能设置截止时间，但是milestone可以。

Assignee，责任人。指定这个 issue 由谁负责来解决。
