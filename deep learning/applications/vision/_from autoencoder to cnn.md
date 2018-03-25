## title

- from autoencoder to cnn
- from fully-connect
- from small image to large image


可以用autoencoder学习到的filter作为cnn的pre_train filter吧？unsupervised_pretrain是不是更好些

##

UFLDL介绍顺序很好，
图像分类
方法一： 全部串起来，全连接softmax
方法二： 小图片，利用sparse autoencoder全连接学映射，然后再softmax
方法三： 大图片，学习位置无关映射(即filter，类似于crop后的全连接)
其中二和三隐约觉的有什么联系。

大图片如何学习位置无关映射？
方法一：random_crop + autoencoder (unsupervised)
方法二：cnn  (supervised)

疑问又来了，方法一学到的映射可否用于分类？与方法二中学到的映射有什么区别？
详见--UFLDL: Learning color features with Sparse
Autoencoders

两者的区别无非是监督与非监督而已(暂不考虑pooling)
