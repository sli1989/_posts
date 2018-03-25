#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:38:25 2017

@author: song
"""


#! /usr/bin/env python

import tensorflow as tf
import numpy as np
import os
import time
import datetime

import data_helpers
from data_helpers import datasets
from data_helpers import label_processor
from data_helpers import word2vec
from text_cnn import TextCNN
from tensorflow.contrib import learn
from tensorflow.contrib.tensorboard.plugins import projector
from sklearn.model_selection import train_test_split

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

# Parameters
# ==================================================

# model- cnn-rand cnn-static cnn-multichannel

# Data loading params
tf.flags.DEFINE_float("dev_sample_percentage", .1, "Percentage of the training data to use for validation")
## bluescan dataset
tf.flags.DEFINE_string("bluescan_data_file", "../../data/bluescan-NLC/all_for_NLC.data", "Data source for the train data.")
tf.flags.DEFINE_string("bluescan_train_data_file", "../../data/bluescan-NLC/train_for_NLC.data", "Data source for the train data.")
tf.flags.DEFINE_string("test_data_file", "../../data/bluescan-NLC/test_for_NLC.data", "Data source for the test data.")
tf.flags.DEFINE_string("save_test_file", "test_for_NLC.data", "if train_test_split automatically")


## sentiment dataset
tf.flags.DEFINE_string("positive_data_file", "../../data/rt-polaritydata/rt-polarity.pos", "Data source for the positive data.")
tf.flags.DEFINE_string("negative_data_file", "../../data/rt-polaritydata/rt-polarity.neg", "Data source for the negative data.")
tf.flags.DEFINE_string("label_file", "label.txt", "id for labels")

# Model Hyperparameters
tf.flags.DEFINE_integer("embedding_dim", 128, "Dimensionality of character embedding (default: 128)")
tf.flags.DEFINE_string("filter_sizes", "3,4,5", "Comma-separated filter sizes (default: '3,4,5')")
tf.flags.DEFINE_integer("num_filters", 128, "Number of filters per filter size (default: 128)")
tf.flags.DEFINE_float("dropout_keep_prob", 0.5, "Dropout keep probability (default: 0.5)")
tf.flags.DEFINE_float("l2_reg_lambda", 0.0, "L2 regularization lambda (default: 0.0)")

# Training parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_integer("num_epochs", 200, "Number of training epochs (default: 200)")
tf.flags.DEFINE_integer("evaluate_every", 100, "Evaluate model on dev set after this many steps (default: 100)")
tf.flags.DEFINE_integer("checkpoint_every", 100, "Save model after this many steps (default: 100)")
tf.flags.DEFINE_integer("num_checkpoints", 5, "Number of checkpoints to store (default: 5)")
# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")
tf.flags.DEFINE_string("embedding_init_method", "rand", "rand pretrain (default: rand)")
tf.flags.DEFINE_boolean("embedding_static", False, "rand glove (default: false)")


FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{}={}".format(attr.upper(), value))
print("")


# Data Preparation
# ==================================================

# Load data
print("Loading data...")

dataset_name = "SST"

if dataset_name == "sentiment":
    # Load data
    print("Loading data...")
    x_text, y = datasets.load_datasets_mrpolarity_(FLAGS.positive_data_file, FLAGS.negative_data_file)
    
    # Build vocabulary
    max_document_length = max([len(x.split(" ")) for x in x_text])
    vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
    x = np.array(list(vocab_processor.fit_transform(x_text)))
    
    
    # Randomly shuffle data
    np.random.seed(10)
    shuffle_indices = np.random.permutation(np.arange(len(y)))
    x_shuffled = x[shuffle_indices]
    y_shuffled = y[shuffle_indices]
    
    # Split train/test set
    # TODO: This is very crude, should use cross-validation
    dev_sample_index = -1 * int(FLAGS.dev_sample_percentage * float(len(y)))
    x_train, x_dev = x_shuffled[:dev_sample_index], x_shuffled[dev_sample_index:]
    y_train, y_dev = y_shuffled[:dev_sample_index], y_shuffled[dev_sample_index:]


if dataset_name == "SST":
    x_text_train, x_text_dev, y_train, y_dev = datasets.load_datasets_treebank()
    
    y_train = np.array(label_processor.index_to_onehot(y_train, 5))
    y_dev = np.array(label_processor.index_to_onehot(y_dev, 5))
    # Build vocabulary for text
    x_text = x_text_train + x_text_dev
    max_document_length = max([len(x.split(" ")) for x in x_text])
    vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
    vocab_processor.fit(x_text)
    x_train = np.array(list(vocab_processor.transform(x_text_train)))
    x_dev = np.array(list(vocab_processor.transform(x_text_dev)))
    
if dataset_name == "bluescan":
    # Load data
    x_text, y_text = datasets.load_datasets_bluescan(FLAGS.bluescan_data_file)
    
    # label preprocess
    label_processor = label_processor()
    x_text, y_text = label_processor.preprocess(x_text, y_text)
    x_text_train, x_text_dev, y_text_train, y_text_dev = datasets.train_test_split(x_text, y_text)
    
    # Build vocabulary for label
    label_processor.fit(y_text)
    y_train = label_processor.transform_binary(y_text_train, len(label_processor.idx2label))
    y_dev = label_processor.transform_binary(y_text_dev, len(label_processor.idx2label))
    
    # Build vocabulary for text
    max_document_length = max([len(x.split(" ")) for x in x_text])
    vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
    vocab_processor.fit(x_text)
    x_train = np.array(list(vocab_processor.transform(x_text_train)))
    x_dev = np.array(list(vocab_processor.transform(x_text_dev)))
    

if dataset_name == "20newsgroup":
    datasets = datasets.get_datasets_20newsgroup(subset="train")
    x_text, y = datasets.load_data_labels(datasets)
    
    # Build vocabulary
    max_document_length = max([len(x.split(" ")) for x in x_text])
    vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
    x = np.array(list(vocab_processor.fit_transform(x_text)))
    
    # Randomly shuffle data
    np.random.seed(10)
    shuffle_indices = np.random.permutation(np.arange(len(y)))
    x_shuffled = x[shuffle_indices]
    y_shuffled = y[shuffle_indices]
    
    # Split train/test set
    # TODO: This is very crude, should use cross-validation
    dev_sample_index = -1 * int(FLAGS.dev_sample_percentage * float(len(y)))
    x_train, x_dev = x_shuffled[:dev_sample_index], x_shuffled[dev_sample_index:]
    y_train, y_dev = y_shuffled[:dev_sample_index], y_shuffled[dev_sample_index:]
    

print("max_document_length: {:d}".format(max_document_length))
print("Vocabulary Size: {:d}".format(len(vocab_processor.vocabulary_)))
print("Train/Dev split: {:d}/{:d}".format(len(y_train), len(y_dev)))
    


w2v_pretrain = None
if FLAGS.embedding_init_method == "pretrain":
    w2v_pretrain = word2vec.load_embedding_vectors_glove_xs("/data/xs/word2vec-pretrained/glove.6B.100d.txt", vocab_processor.vocabulary_._reverse_mapping)
    print "loading glove"
    
    #sess.run(cnn.W.assign(w2v))




# Training
# ==================================================

with tf.Graph().as_default():
    session_conf = tf.ConfigProto(
      allow_soft_placement=FLAGS.allow_soft_placement,
      log_device_placement=FLAGS.log_device_placement)
    sess = tf.Session(config=session_conf)
    with sess.as_default():
        cnn = TextCNN(
            sequence_length=x_train.shape[1],
            num_classes=y_train.shape[1],
            vocab_size=len(vocab_processor.vocabulary_),
            embedding_size=FLAGS.embedding_dim,
            embedding_init_method=FLAGS.embedding_init_method,
            embedding_init_value=w2v_pretrain,
            embedding_static=FLAGS.embedding_static,
            filter_sizes=list(map(int, FLAGS.filter_sizes.split(","))),
            num_filters=FLAGS.num_filters,
            l2_reg_lambda=FLAGS.l2_reg_lambda)

        # Define Training procedure
        global_step = tf.Variable(0, name="global_step", trainable=False)
        optimizer = tf.train.AdamOptimizer(1e-3)
        grads_and_vars = optimizer.compute_gradients(cnn.loss)
        train_op = optimizer.apply_gradients(grads_and_vars, global_step=global_step)

        # Keep track of gradient values and sparsity (optional)
        grad_summaries = []
        for g, v in grads_and_vars:
            if g is not None:
                grad_hist_summary = tf.summary.histogram("{}/grad/hist".format(v.name), g)
                sparsity_summary = tf.summary.scalar("{}/grad/sparsity".format(v.name), tf.nn.zero_fraction(g))
                grad_summaries.append(grad_hist_summary)
                grad_summaries.append(sparsity_summary)
        grad_summaries_merged = tf.summary.merge(grad_summaries)

        # Output directory for models and summaries
        timestamp = str(int(time.time()))
        out_dir = os.path.join(os.path.curdir, "runs", timestamp)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        
        print("Writing to {}\n".format(out_dir))
        
        if dataset_name=="bluescan":
            label_processor.save_idx2label(os.path.join(out_dir, FLAGS.label_file))
            # save dev data for evaluation
            datasets.save_data(x_text_dev, y_text_dev, os.path.join(out_dir, FLAGS.save_test_file))

        # Summaries for loss and accuracy
        loss_summary = tf.summary.scalar("loss", cnn.loss)
        acc_summary = tf.summary.scalar("accuracy", cnn.accuracy)
        embedding_hist_summary = tf.summary.histogram("W embedding", cnn.W)
        #embeddingsum_summary = tf.summary.scalar("accuracy", cnn.accuracy)
        

        # Train Summaries
        train_summary_op = tf.summary.merge([loss_summary, acc_summary, grad_summaries_merged, embedding_hist_summary])
        train_summary_dir = os.path.join(out_dir, "summaries", "train")
        #train_summary_dir = os.path.join(out_dir, "train")
        train_summary_writer = tf.summary.FileWriter(train_summary_dir, sess.graph)

        # Dev summaries
        dev_summary_op = tf.summary.merge([loss_summary, acc_summary])
        dev_summary_dir = os.path.join(out_dir, "summaries", "dev")
        #dev_summary_dir = os.path.join(out_dir, "dev")
        dev_summary_writer = tf.summary.FileWriter(dev_summary_dir, sess.graph)

        # Checkpoint directory. Tensorflow assumes this directory already exists so we need to create it
        checkpoint_dir = os.path.abspath(os.path.join(out_dir, "checkpoints"))
        #checkpoint_dir = out_dir
        
        checkpoint_prefix = os.path.join(checkpoint_dir, "model")
        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir)
        saver = tf.train.Saver(tf.global_variables(), max_to_keep=FLAGS.num_checkpoints)

        # Initialize all variables
        sess.run(tf.global_variables_initializer())
        init_embedding = cnn.W.eval()

        
        def train_step(x_batch, y_batch):
            """
            A single training step
            """
            feed_dict = {
              cnn.input_x: x_batch,
              cnn.input_y: y_batch,
              cnn.dropout_keep_prob: FLAGS.dropout_keep_prob
            }
            _, step, summaries, loss, accuracy, predictions = sess.run(
                [train_op, global_step, train_summary_op, cnn.loss, cnn.accuracy, cnn.predictions],
                feed_dict)
            time_str = datetime.datetime.now().isoformat()
            print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
            train_summary_writer.add_summary(summaries, step)

        def dev_step(x_batch, y_batch, writer=None):
            """
            Evaluates model on a dev set
            """
            feed_dict = {
              cnn.input_x: x_batch,
              cnn.input_y: y_batch,
              cnn.dropout_keep_prob: 1.0
            }
            step, summaries, loss, accuracy, predictions = sess.run(
                [global_step, dev_summary_op, cnn.loss, cnn.accuracy, cnn.predictions],
                feed_dict)
            
            #print x_batch
            time_str = datetime.datetime.now().isoformat()
            print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
            if writer:
                writer.add_summary(summaries, step)

        # Generate batches
        batches = data_helpers.batch_iter(
            list(zip(x_train, y_train)), FLAGS.batch_size, FLAGS.num_epochs)
        # Training loop. For each batch...
        for batch in batches:
            x_batch, y_batch = zip(*batch)
            train_step(x_batch, y_batch)
            current_step = tf.train.global_step(sess, global_step)
            if current_step % FLAGS.evaluate_every == 0:
                print("\nEvaluation:")
                dev_step(x_dev, y_dev, writer=dev_summary_writer)
                print("")
            if current_step % FLAGS.checkpoint_every == 0:
                path = saver.save(sess, checkpoint_prefix, global_step=current_step)
                print("Saved model checkpoint to {}\n".format(path))


        # Write vocabulary as pickle for reloading next time
        vocab_processor.save(os.path.join(out_dir, "vocab"))
        
        
        # Write vocabulary as metadata.tsv for embedding visualization
        def save_vocab(save_path, vocabulary):
            with open(os.path.join(save_path, "metadata.tsv"), "w") as f:
                for i in xrange(vocabulary.__len__()):
                    #print vocabulary.reverse(i)
                    #vocab_word = tf.compat.as_text(vocabulary.reverse(i)).encode("utf-8")
                    vocab_word = vocabulary.reverse(i)
                    f.write("%s %d\n" % (vocab_word,vocabulary._freq[vocab_word]))



        def save_embedding_for_visualization():
            '''
            tensorboard --logdir $checkpoint_dir
            '''
            final_checkpoint_dir = out_dir
            print "tensorboard --logdir " + checkpoint_dir
            save_vocab(checkpoint_dir, vocab_processor.vocabulary_)
            # save final model for embedding visualization
            #saver.save(sess, os.path.join(final_checkpoint_dir, "model"), current_step)
            
            # Format: tensorflow/contrib/tensorboard/plugins/projector/projector_config.proto
            config = projector.ProjectorConfig()
            
            # You can add multiple embeddings. Here we add only one.
            embedding = config.embeddings.add()
            embedding.tensor_name = cnn.W.name
            # Link this tensor to its metadata file (e.g. labels).
            embedding.metadata_path = os.path.join(checkpoint_dir, 'metadata.tsv')
            
            # Use the same LOG_DIR where you stored your checkpoint.
            summary_writer = tf.summary.FileWriter(checkpoint_dir)
            
            # The next line writes a projector_config.pbtxt in the LOG_DIR. TensorBoard will
            # read this file during startup.
            projector.visualize_embeddings(summary_writer, config)
        
        save_embedding_for_visualization()
        
        def check_embedding(init_embedding, final_embedding, w2v_pretrain=None):
            if FLAGS.embedding_static:
                print "should be 0: %f" % sum(sum(init_embedding-final_embedding))
            else:
                print "shouldn't be 0: %f" % sum(sum(init_embedding-final_embedding))
                
            if FLAGS.embedding_init_method == "pretrain":
                print "should be 0: %f" % sum(sum(init_embedding-w2v_pretrain))

        check_embedding(init_embedding, cnn.W.eval(), w2v_pretrain)

        
