

## tensorflow 疑问
### 什么是client？
cpu端的都叫client？



### 为什么要有sesstion？
Client通过Session为桥梁，连接TensorFlow后端的「运行时」，并启动计算图的执行过程。

### 为什么要有graph？
如果都在cpu中 




## 设计思想

- 无非就是数据，操作(函数)。

### 需要解决的问题？

- 如何与C中的cuda交互？
- 如何体现graph？
- 

## 我来设计


### 第一版


tensor1 = tf.Tensor(value, type="constant", shape, dtype=float32)
tensor2 = tf.Tensor(value, type="variable", shape, dtype=float32)

tensor3 = tf.add(tf.tensor1, tensor2)
tensor4 = tf.multiply(tf.tensor1, tensor2)


class Tensor:
    def __init__():
        pass



class Operation:
    def __init__():


    def add():
        pass

    def multiply():
        pass

    def conv():
        pass

**存在的问题**

* 

###





运行时才能确定的是：


编译时确定的是：


