



##

pytorch教程特别基础，适合入门。




## tensor vs variable

autograd.Variable
torch.Tensor


> When we added two tensors together, we got an output tensor. All this output tensor knows is its data and shape. It has no idea that it was the sum of two other tensors.
The Variable class keeps track of how it was created

Tensor是数据，无指向。
Variable才能构建graph。


### 问题
tf.placeholder 等价于
pytorch通过不区分input和param

## 自定义梯度？？

define our own autograd operator by de×ning a subclass of
torch.autograd.Function
