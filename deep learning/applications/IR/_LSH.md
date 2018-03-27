---

---


# semantic hash

加速环节：




## 检索
v1 bit[] [1 0 0 0 1 0 1],.
v2 bit[] [1 0 0 0 1 1 1]

|v1-V2|



## 分类
v1 double[]    softmax(v1)=
v2 double[]

|v1-v2|
cosine()


## 局部敏感哈希(Locality Sensitive Hashing，LSH)
- 传统 Hash 希望即使两个数据有一点点不一样，也要尽可能差异大。
- 而LSH则是希望相似的 value 对应的 Hash 值越相似越好。

常见的使用场景:
- 判重 Near-duplicate detection
- 摘要 Sketching
- 聚类 Clustering
- 相似搜索 Near-neighbor search

如果两个文本在原有的数据空间是相似的，那么分别经过哈希函数转换以后的它们也具有很高的相似度；相反，如果它们本身是不相似的，那么经过转换后它们应仍不具有相似性。

## 参考

局部敏感哈希(Locality Sensitive Hashing，LSH) http://www.cnblogs.com/maybe2030/p/4953039.html
