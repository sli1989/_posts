


## 基本介绍

|  tool |  year | download | feature | example code  | pretrained_model|  state of art | 备注|
| :-------- | -----:| ----:|--------:|--------:|:--: |
| caffe |||
| theano |||
| tensorflow |||
| torch |||
| DL4j | || 容易与Kafka、Hadoop和Spark集成|


## api比较

|           |   | tensorflow      | pytorch                                | theano | keras | MXNet |
|-----------|---|-----------------|----------------------------------------|--------|-------|-------|
| 输入数据x |   | tf.placeholder  | autograd.Variable()                    |        |       |       |
| 变量param |   | tf.variable     | autograd.Variable(.requires_grad=True) |        |       |       |
|           |   |                 |                                        |        |       |       |
|           |   | tf.scan         | 可用普通的imperative flow control      |        |       |       |
|           |   | tf.constant放哪 | torch.tensor放哪？                     |        |       |       |
|           |   | 这些都是符号    | 包含数据的变量                         |        |       |       |


**tensor to numpyArray**
- tensorflow
  - tf.eval 或 session.run。需要依赖
- pytorch
  - torch.from_numpy(a) 方便


类似的东东
tf - tf.variable是tf.tensor的封装
pytorch - autograd.Variable是tensor的封装


ONNX

性能Caffe> TensorFlow和Torch



上升趋势：MXNet(Amazon主推) > PyTorch(Facebook主推) > TF & Keras

速度：
pytorch想要写的快也需要了解自动求导等原理，没写好一定慢。tf没写好也会慢
PyTorch多清爽 (tf的session，graph很烦)
MXNet多快。
底层都是C++，为什么tf的python这么丑？


为什么keras不支持MXNet？不支持PyTorch？

## TF

**pros**
- 与Theano类似的计算图抽象化
- 编译时间快于Theano
- 用TensorBoard进行可视化 (pytorch和MXNet也有可视化了，这个不算优势了)
- 同时支持数据并行和模型并行
- 生态好，分布式，serving，

**cons**
- control dependency反人类（不理解）
- 写动态结构麻烦(不理解)
- 目前TensorFlow还不支持所谓的“内联（inline）”矩阵运算，必须要复制矩阵才能对其进行运算。复制非常大的矩阵会导致成本全面偏高。TF运行所需的时间是最新深度学习工具的四倍。谷歌表示正在解决这一问题。
- 速度慢（例如：CNTK 和 MxNet）.  为什么？？？
- TensorFlow不提供商业支持。而谷歌也不太可能会从事支持开源企业软件的业务。谷歌的角色是为研究者提供一种新工具。
- 和Theano一样，TensforFlow会生成计算图（如一系列矩阵运算，例如z = sigmoid(x)，其中x和z均为矩阵），自动求导。自动求导很重要，否则每尝试一种新的神经网络设计就要手动编写新的反向传播算法，没人愿意这样做。在谷歌的生态系统中，这些计算图会被谷歌大脑用于高强度计算，但谷歌还没有开放相关工具的源代码。TensorFlow可以算是谷歌内部深度学习解决方案的一半。
- 加载每个新的训练批次时都要跳至Python
- 动态类型在大型软件项目中容易出错
- 速度慢,有争议
- 比Torch笨重许多；更难理解
- tensorflow是符号式编程方式，继承了theano一大堆缺点，不仅写法麻烦，而且bug难调；
- 作为静态图框架，调试困难。有个tfdbg的工具可以调试。
- tensorflow_Fold的“动态”是指dynamic batching，并非pytorch的“动态”

**疑问**
- 按道理静态图适宜部署，运行应该比动态图快啊。比pytorch快吗？为什么比MXNet慢呢？

## caffe -- deprecated
适合前馈网络和图像处理

**pros**
+ 适合前馈网络和图像处理
+ 适合微调已有的网络
+ 无需编写任何代码即可训练模型
+ Python接口相当有用

**cons**
- 需要用C++ / CUDA编写新的GPU层
- 不适合循环网络，不适用于文本、声音或时间序列数据等其他类型的深度学习应用
- 用于大型网络（GoogLeNet、ResNet）时过于繁琐
- 不可扩展，有些不够精简
- 不提供商业支持
- 更新缓慢，以后不再更新



## caffe2 -- 没文档 by 贾扬清
Caffe2将接替原版Caffe，与Caffe和PyTorch一样，Caffe2提供一个在C++引擎上运行的Python API。

不提供商业支持


## pytorch
- 命令式编程的方式，随时能够运行结果，容易定位bug
- 支持动态图，非常灵活，能够随意取出其中的tensor进行操作和查看；
- 最新的cs231n都推出了PyTorch版本的作业

- 其实PyTorch也是仿照Chainer开发的，其后端也是调用的torch的运算，定位比keras低，但是又比tensorflow高。
- PyTorch定位于科研，在Facebook内部使用Caffe2作为产品的部署和应用
- pytorch更容易重构函数，但是如果需要部署的话就还是得像TF或者其他一些框架一样老老实实做dirty work。

## CNTK


## Chainer


## DyNet
DyNet亦称动态神经网络工具包，由卡纳基梅隆大学推出，过去曾被称为cnn。它最值得一提的功能就是动态计算图，能够处理可变长度的输入，很适合自然语言分析。PyTorch和Chainer也提供同样的功能。

+ 动态计算图
- 用户群较小
、


## keras
Keras 是一个基于Theano和TensorFlow的深度学习库，具有一个受Torch启发、较为直观的API。这可能是目前最好的Python API。Deeplearning4j可以导入Keras模型。Keras是由谷歌软件工程师Francois Chollet开发的。

+ 受Torch启发的直观API
+ 可使用Theano、TensorFlow和Deeplearning4j后端（即将推出CNTK后端）
+ 该框架正快速成长
+ 有可能成为用于开发神经网络的标准Python API
- 不用keras的原因主要是不能像TensorFlow一样自己定义输入输出，只能add layer，不太好构造结构独特的网络。
## MxNet
- 结合了神经网络几何的象征性声明与张量操作的命令性编程
- 允许混合符号和命令式编程风格。
- MXNet平台是建立在一个动态依赖调度器上的，它可以自动并行化符号和命令式操作
- 在许多方面MXNet类似于TensorFlow，但增加了嵌入命令张量操作的能力。
- MXnet速度快，省显存，并行效率高，分布式简单
- 动态图接口Gluon。MXNet正是看到了以PyTorch为首的命令式编程框架的潜力，对于新用户特别友好，易于上手，所以他们决定模仿PyTorch开发一个动态图接口Gluon
- Gluon也可以看作一个接口，调用底层的MXNet，但是前端使用符号式编程的方式。
- Gluon不仅定位于科研，同时也可用于产品
- PyTorch只有动态图的模式，有的时候我们的网络结构其实是一个静态图，但是通过PyTorch每次都会重新构建动态图，而Gluon提供了一个静态图和动态图之间切换的方式
- 使用者可以先用imperatvie的方式写网络，debug，最后跑通网络之后，如果网络是一个静态图结构，就可以用net.hybridize()的方式将其转换成静态图，众所周知静态图的运算会比动态图快，

## Paddle


## 如何评价余凯在朋友圈发表呼吁大家用caffe, mxnet等框架，避免tf

1. 假设有一天Google为了卖它的TPU，决定渐渐放弃GPU支持，你说nVidia会不会慌？
2. 假设Google说要把放弃x86和Xeon Phi支持，你说Intel慌不慌？
3. Google拒绝针对以太网（AWS和Windows Azure都是万兆以太网）做任何优化，而且不愿意merge任何与此相关的PR，你说Amazon和Microsoft慌不慌？
4. 假设有一家做TPU(比如寒武纪)，或者做无人车的公司，对Google造成了严重威胁，那么他们发的PR，能不能保证得到Google的公正对待？

NVidia笑了。这几个框架跑分全靠cuDNN，就算不用cuDNN，也是要用CUDA的。深度学习就是NVidia的私家花园。TensorFlow能垄断啥？

NVIDIA 搞生态(？？？)，是指支持很多框架吗？


## 发展史  段子

---
我曾经做过一段时间的图像算法工程师，主要工作就是看论文、实践论文中的各种算法以及优化算法以适应自己的工程问题。当时的主要工程问题就是做人脸检测、图像识别和图像搜索等等，其中比较考验水平和依赖经验的部分是选择Feature和优化Feature以适应具体的工程问题。对于当时的一些通用的Feature，比如SURF/SIFT（这两个基本是划时代的）、LBP或者MSER等等，不仅是需要了解其使用场景及各种局限，而且最好能够很清楚其理论基础和推导过程，这样才能便于优化和适应。
大概在2013年左右，了解到Deep Learning崛起的趋势，然后阅读了相关教程。当时的第一个反应就是WTF，难怪有人将DL列为“知其然而不知其所以然”的科学技术之前几名。第二个反应就是，选择和优化Feature这一步岂不是被完全替代了。紧接着Caffe、TensorFlow以及各种DL的Library接踵而出，搞DL的门槛被拉得越来越低。这不得不让人想起来在OpenCV中实现人脸检测就只需要一两行代码，使用的人完全不用考虑Adaboost以及Haar等数学问题。



-----
我大概13年的时候听说有深度学习这回事，然后跟着UFLDL学习了如何推导矩阵导数，练习了一些常见层的推导和代码编写。后来出了caffe，因为当时在外地出差，搬砖之余就看了不少caffe的代码，慢慢地就开始在caffe上写layer，前向cpu、后向cpu、前向gpu、后向gpu，一共4份代码。为了写一个layer，需要学会推导矩阵求导的公式（我研究生时期才学到相关知识），要会写c++，会使用BLAS（一个矩阵运算的库，参数非常繁复，每次都要看半天文档才能写出一个函数），还要会写GPU上运行的CUDA代码。如果是一名编程基础不是很好的研究生，可能到了研二结束都写不出一个layer。还好，当时我是个编程基础还不错的研究生，上手还不算很困难。然而当我刚刚能够熟练写layer的时候，深度学习的各种library如雨后春笋般一个个冒出来了，各个都有自动求导、cpu gpu代码自动转换的功能！这意味着不需要推导公式，不需要会BLAS，不需要会CUDA，只需要写1份前向代码，而其他所有工作都由library自动完成！一开始我并没有在意，后来实现neural style（就是之前很火的Prisma用的方法：免费摄影APP“Prisma”将照片变成名画）的时候我花了2天时间写了个gram layer并完成测试后，赫然看到别人用torch几行就写出来了，顿时目瞪口呆：function gram(input)    local k = input:size(2)    local flat = input:view(k, -1)    local gram = torch.mm(flat, flat:t())    return gramend它简洁而优雅，简洁到根本不需要测试就知道它是对的，优雅得像“神说要有光，于是便有了光”。而这是我的代码：caffe-windows/gram_layer.cpp at master · happynear/caffe-windows · GitHubcaffe-windows/gram_layer.cu at master · happynear/caffe-windows · GitHub两个文件，一个cpu版一个gpu版。理所当然的，我的代码除了我自己根本没人使用。如果不保持学习，就算你在从事尖端的人工智能研究，一样说淘汰就淘汰。
作者：王峰
链接：https://www.zhihu.com/question/50144455/answer/119655526
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
