import tensorflow as tf
import numpy as np
from sklearn import preprocessing

model_name = "single-channel"

class TextCNN(object):
    def init_embedding(self, vocab_size, embedding_size, embedding_init_method="rand", embedding_static=False, embedding_init_value=None):
        # Embedding layer
        with tf.device('/cpu:0'), tf.name_scope("embedding"):
            # static: tf.constant
            if embedding_static:
                if embedding_init_method=="rand":
                    self.W = tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0, name="W") # return mutable tensor, not constant
                if embedding_init_method=="pretrain":
                    self.W = tf.constant(embedding_init_value, dtype=tf.float32, name="W")
                    
            # nonstatic: tf.variable    
            else:
                if embedding_init_method=="rand":
                    self.W = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0), name="W")
                if embedding_init_method=="pretrain":
                    self.W = tf.Variable(embedding_init_value, dtype=tf.float32, name="W")
                    
                    
            
            self.embedded_chars = tf.nn.embedding_lookup(self.W, self.input_x)
            self.embedded_chars_expanded = tf.expand_dims(self.embedded_chars, -1)
            
            # pretrain embedding usually very large, should not place all in GPU
            if(model_name == "multi-channel" ):
                self.W_pretrain = tf.placeholder(tf.float32, [None, embedding_size], name="W_pretrain")
                self.embedded_chars_pretrain = tf.nn.embedding_lookup(self.W_pretrain, self.input_x)
                self.embedded_chars_expanded_pretrain = tf.expand_dims(self.embedded_chars_pretrain, -1)
                self.embedded_chars_expanded = tf.concat([self.embedded_chars_expanded, self.embedded_chars_expanded_pretrain], 3)

        
    """
    A CNN for text classification.
    Uses an embedding layer, followed by a convolutional, max-pooling and softmax layer.
    """
    def __init__(
      self, sequence_length, num_classes, vocab_size,
      embedding_size, embedding_init_method, embedding_static, embedding_init_value, filter_sizes, num_filters, l2_reg_lambda=0.0):

        # Placeholders for input, output and dropout
        self.input_x = tf.placeholder(tf.int32, [None, sequence_length], name="input_x")
        self.input_y = tf.placeholder(tf.float32, [None, num_classes], name="input_y")
        self.dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")

        # Keeping track of l2 regularization loss (optional)
        l2_loss = tf.constant(0.0)
        self.init_embedding(vocab_size, embedding_size, embedding_init_method, embedding_static, embedding_init_value)
        

        # Create a convolution + maxpool layer for each filter size
        pooled_outputs = []
        for i, filter_size in enumerate(filter_sizes):
            with tf.name_scope("conv-maxpool-%s" % filter_size):
                # Convolution Layer
                filter_shape = [filter_size, embedding_size, 1, num_filters]
                W = tf.Variable(tf.truncated_normal(filter_shape, stddev=0.1), name="W")
                b = tf.Variable(tf.constant(0.1, shape=[num_filters]), name="b")
                conv = tf.nn.conv2d(
                    self.embedded_chars_expanded,
                    W,
                    strides=[1, 1, 1, 1],
                    padding="VALID",
                    name="conv")
                # Apply nonlinearity
                h = tf.nn.relu(tf.nn.bias_add(conv, b), name="relu")
                # Maxpooling over the outputs
                pooled = tf.nn.max_pool(
                    h,
                    ksize=[1, (sequence_length - filter_size + 1)/2, 1, 1],
                    strides=[1, (sequence_length - filter_size + 1)/4, 1, 1],
                    padding='VALID',
                    name="pool")
                pooled_outputs.append(pooled)

        # Combine all the pooled features
        num_filters_total = num_filters * len(filter_sizes)
        
        #tmp1 = tf.reshape(pooled_outputs[0],[-1])
        #tmp2 = tf.reshape(pooled_outputs[1],[-1])
        #tmp3 = tf.reshape(pooled_outputs[2],[-1])
        #self.h_pool_flat = tf.concat([tmp1,tmp2,tmp3],1)

        self.h_pool = tf.concat(pooled_outputs, 1)
        self.h_pool_flat = tf.reshape(self.h_pool, [-1, num_filters_total*3])

        # Add dropout
        with tf.name_scope("dropout"):
            self.h_drop = tf.nn.dropout(self.h_pool_flat, self.dropout_keep_prob)

        # Final (unnormalized) scores and predictions
        with tf.name_scope("output"):
            W = tf.get_variable(
                "W",
                shape=[num_filters_total*3, num_classes],
                initializer=tf.contrib.layers.xavier_initializer())
            b = tf.Variable(tf.constant(0.1, shape=[num_classes]), name="b")
            l2_loss += tf.nn.l2_loss(W)
            l2_loss += tf.nn.l2_loss(b)
            self.scores = tf.nn.xw_plus_b(self.h_drop, W, b, name="scores")
            self.predictions = tf.argmax(self.scores, 1, name="predictions")

        # CalculateMean cross-entropy loss
        with tf.name_scope("loss"):
            losses = tf.nn.softmax_cross_entropy_with_logits(logits=self.scores, labels=self.input_y)
            self.loss = tf.reduce_mean(losses) + l2_reg_lambda * l2_loss

        # Accuracy
        with tf.name_scope("accuracy"):
            correct_predictions = tf.equal(self.predictions, tf.argmax(self.input_y, 1))
            self.accuracy = tf.reduce_mean(tf.cast(correct_predictions, "float"), name="accuracy")
