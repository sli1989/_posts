

## 参考


[Why cant I see .grad of an intermediate variable?](https://discuss.pytorch.org/t/why-cant-i-see-grad-of-an-intermediate-variable/94/2)



[RuntimeError: Trying to backward through the graph a second time, but the buffers have already been freed. Specify retain_graph=True when calling backward the first time](https://discuss.pytorch.org/t/runtimeerror-trying-to-backward-through-the-graph-a-second-time-but-the-buffers-have-already-been-freed-specify-retain-graph-true-when-calling-backward-the-first-time/6795)


credit assignment problem with BP/BPTT,

## 开头


```python

    def backward(self, gradient=None, retain_graph=None, create_graph=False):
        """Computes the gradient of current variable w.r.t. graph leaves.
        The graph is differentiated using the chain rule. If the variable is
        non-scalar (i.e. its data has more than one element) and requires
        gradient, the function additionally requires specifying ``gradient``.
        It should be a tensor of matching type and location, that contains
        the gradient of the differentiated function w.r.t. ``self``.
        This function accumulates gradients in the leaves - you might need to
        zero them before calling it.
        Arguments:
            gradient (Tensor, Variable or None): Gradient w.r.t. the
                variable. If it is a tensor, it will be automatically converted
                to a Variable that does not require grad unless ``create_graph`` is True.
                None values can be specified for scalar Variables or ones that
                don't require grad. If a None value would be acceptable then
                this argument is optional.

```

这里的 current variable 指的是out.backward()中的out，不是input variable/ param

accumulates gradients in the leaves 这句话的意思是？见 http://blog.csdn.net/qq_24401379/article/details/77970049
跟bp的链式法则什么关系，梯度叠加是这个意思吗？

https://sherlockliao.github.io/2017/07/10/backward/

## 为什么要累积梯度？ 为什么要zero-gradient？
This allows us to cumulate gradients over several samples or several batches before using the gradients to update the weights.
Once you have updated the weights you don’t want to keep those gradients around because if you reuse them, then you will push the weights too far.
即 several batches共同更新一次梯度的时候，需要累积梯度。update weights后要马上zero-gradient，不然会影响下次update

## gradient有什么作用？
是给out加的一个权重。

## 给out 加一个gradient权重的意义是什么呢？
严格意义上，gradient是个矩阵，即jacob矩阵。
1. gradient可以起到selector的作用，选择矩阵中的哪个点，就置为1，其他位置为0。导出整个jacob矩阵，要分别backward n次(n为output的data数目，比如[2,3]的output，n=6)



## tensor output做backward的用途？
多数情况下都采用标量作为loss，比如(分类问题中的MSE，回归问题中的..)。
什么情况下会用到tensor output的梯度？
- 纯数学问题，比如你要得到jacob矩阵
- ML问题，



## 多维的output和多维的input，在求梯度的时候，实质上都是等价于flatten成一维向量。最终都是求和。


```python
import torch
from torch.autograd import Variable

x = Variable(torch.ones(2, 3), requires_grad=True)
a = Variable(torch.ones(3, 4))
out = torch.mm(x,a)    # shape: (2,4)

gradient = torch.FloatTensor([[1,2,3,4],[5,6,7,8]]) # shape=(2,4)
#gradient = torch.ones(4, 4)
out.backward(gradient)
print(x.grad)

```

`x`

| x_11 | x_12 | x_13  |
|------|------|------|
| x_21 | x_22 | x_23 |

`out`

| x_11+x_12+x_13 | x_11+x_12+x_13 | x_11+x_12+x_13 | x_11+x_12+x_13 |
|----------------|----------------|----------------|----------------|
| x_21+x_22+x_23 | x_21+x_22+x_23 | x_21+x_22+x_23 | x_21+x_22+x_23 |

`d(out)/dx`

|         | d(out_11) | d(out_12) | d(out_13 | d(out_14 | d(out_21) | d(out_22) | d(out_23) | d(out_24) |
|---------|-----------|-----------|----------|----------|-----------|-----------|-----------|-----------|
| d(x_11) | 1         | 1         | 1        | 1        |           |           |           |           |
| d(x_12) | 1         | 1         | 1        | 1        |           |           |           |           |
| d(x_13) | 1         | 1         | 1        | 1        |           |           |           |           |
| d(x_14) |           |           |          |          | 1         | 1         | 1         | 1         |
| d(x_21) |           |           |          |          | 1         | 1         | 1         | 1         |
| ...     |           |           |          |          |           |           |           |           |


`gradient*out`  

| x_11+x_12+x_13 | 2x_11+2x_12+2x_13 | 3x_11+3x_12+3x_13 | 4x_11+4x_12+4x_13 |
|----------------|----------------|----------------|----------------|
| 5x_21+5x_22+5x_23 | 6x_21+6x_22+6x_23 | 7x_21+7x_22+7x_23 | 8x_21+8x_22+8x_23 |


`x.grad`  

```
Variable containing:
 10  10  10
 26  26  26
```

10 = 1+2+3+4
26=5+6+7+8



- `x.grad`  should has the same shape with `x.data`, for update weight
- `gradient` should has the same shape with `out` (current variable)

The effect of `gradient` a
