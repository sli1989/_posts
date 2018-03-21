#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:59:04 2017

@author: song
"""

# from http://stackoverflow.com/questions/37558899/efficiently-finding-closest-word-in-tensorflow-embedding
# The tensorboard has already done this job

import tensorflow as tf

# load embedding

embedding = tf.placeholder(tf.float32, [vocab_size, embedding_size])
batch_array = tf.placeholder(tf.float32, [batch_size, embedding_size])


normed_embedding = tf.nn.l2_normalize(embedding, dim=1)
normed_array = tf.nn.l2_normalize(batch_array, dim=1)

cosine_similarity = tf.matmul(normed_array, tf.transpose(normed_embedding, [1, 0]))

closest_words = tf.argmax(cosine_similarity, 1)  # shape [batch_size], type int64

# compute distance