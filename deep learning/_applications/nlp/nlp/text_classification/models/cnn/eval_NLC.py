#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 21:34:04 2017

@author: song
"""

#! /usr/bin/env python

import tensorflow as tf
import numpy as np
import os
import time
import datetime
import data_helpers
from text_cnn import TextCNN
from tensorflow.contrib import learn
import csv
import data_helpers
from data_helpers import datasets_bluescan




# Parameters
# ==================================================

# Data Parameters
tf.flags.DEFINE_string("train_data_file", "./data/bluescan-NLC/train_for_NLC.data", "Data source for the positive data.")
tf.flags.DEFINE_string("test_data_file", "./data/bluescan-NLC/test_for_NLC.data", "Data source for the positive data.")
#tf.flags.DEFINE_string("test_data_file", "./data/bluescan-NLC/dev_for_NLC.data", "Data source for the positive data.")
tf.flags.DEFINE_string("label_file", "label.txt", "id for labels")

# Eval Parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_string("checkpoint_dir", "./runs_bluescan/1495423833/", "")
tf.flags.DEFINE_boolean("eval_train", False, "Evaluate on all training data")

# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")


FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{}={}".format(attr.upper(), value))
print("")


class eval:
    def __init__(self):
        
        # Parameters
        # ==================================================
        
        # Data Parameters
        
        # Eval Parameters
        self.batch_size = 64
        self.checkpoint_dir = "./runs_bluescan/1495375961/"
        
        # Misc Parameters
        self.allow_soft_placement = True
        self.log_device_placement = False
        
        
        # load vocab
        vocab_path = os.path.join(FLAGS.checkpoint_dir, "vocab")
        self.vocab_processor = learn.preprocessing.VocabularyProcessor.restore(vocab_path)
        
        # load labels
        label_path = os.path.join(FLAGS.checkpoint_dir, FLAGS.label_file)
        dataControl = datasets_bluescan()
        self.idx2label = dataControl.load_idx2label(label_path)

    
    '''
    text is a list of string. such as:
        text = ["a masterpiece four years in the making", "everything is off."]
        eval = eval()
        print eval.eval(text)
        
        return [1, 0]
    '''
    def eval(self, text):
        x_raw = text
        # Map data into vocabulary
        x_test = np.array(list(self.vocab_processor.transform(x_raw)))
        
        print("\nEvaluating...\n")
        
        # Evaluation
        # ==================================================
        checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
        graph = tf.Graph()
        with graph.as_default():
            session_conf = tf.ConfigProto(
              allow_soft_placement=FLAGS.allow_soft_placement,
              log_device_placement=FLAGS.log_device_placement)
            sess = tf.Session(config=session_conf)
            with sess.as_default():
                # Load the saved meta graph and restore variables
                saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))
                saver.restore(sess, checkpoint_file)
        
                # Get the placeholders from the graph by name
                input_x = graph.get_operation_by_name("input_x").outputs[0]
                # input_y = graph.get_operation_by_name("input_y").outputs[0]
                dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]
        
                # Tensors we want to evaluate
                predictions = graph.get_operation_by_name("output/predictions").outputs[0]
        
                # Generate batches for one epoch
                batches = data_helpers.batch_iter(list(x_test), FLAGS.batch_size, 1, shuffle=False)
        
                # Collect the predictions here
                all_predictions = []
        
                for x_test_batch in batches:
                    batch_predictions = sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
                    all_predictions = np.concatenate([all_predictions, batch_predictions])
        
        print all_predictions
        all_predictions = [self.idx2label[int(idx)] for idx in all_predictions]
        #predictions_human_readable = np.column_stack((np.array(x_raw), all_predictions))
        
        
        return all_predictions
    
    '''
    
        
    '''
    #def eval(self, eval_path):
    #    pass



