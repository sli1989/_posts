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
from data_helpers import datasets
from data_helpers import label_processor_bluescan

# Parameters
# ==================================================

# Data Parameters
tf.flags.DEFINE_string("test_data_file", "./runs_bluescan/1496221930/dev.file", "")
#tf.flags.DEFINE_string("test_data_file", "./data/bluescan-NLC/test_for_NLC.data", "Data source for the positive data.")
#tf.flags.DEFINE_string("test_data_file", "./data/bluescan-NLC/dev_for_NLC.data", "Data source for the positive data.")
tf.flags.DEFINE_string("label_file", "label.txt", "id for labels")

# Eval Parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_string("checkpoint_dir", "./runs_bluescan/1496221930/", "")
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

# CHANGE THIS: Load data. Load your own data here

dataset_name = "bluescan"

# init
    
if dataset_name == "bluescan":
    x_text, y_text = datasets.load_datasets_bluescan(FLAGS.test_data_file)
    
    
    # load labels
    label_path = os.path.join(FLAGS.checkpoint_dir, FLAGS.label_file)
    label_processor = label_processor_bluescan()
    label_processor.load_idx2label(label_path)
    y_test = label_processor.transform(y_text)


#if FLAGS.eval_train:
#    x_raw, y_test = data_helpers.load_data_and_labels(FLAGS.positive_data_file, FLAGS.negative_data_file)
#    y_test = np.argmax(y_test, axis=1)
#else:
#    x_raw = ["a masterpiece four years in the making", "everything is off."]
#    y_test = [1, 0]



# Map data into vocabulary
vocab_path = os.path.join(FLAGS.checkpoint_dir,"vocab")
vocab_processor = learn.preprocessing.VocabularyProcessor.restore(vocab_path)
x_test = np.array(list(vocab_processor.transform(x_text)))

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

# Print accuracy if y_test is defined
if y_test is not None:
    correct_predictions = float(sum(all_predictions == y_test))
    print("Total number of test examples: {}".format(len(y_test)))
    print("Accuracy: {:g}".format(correct_predictions/float(len(y_test))))

# Save the evaluation to a csv
all_predictions = [label_processor.idx2label[int(idx)] for idx in all_predictions]
all_labels = [label_processor.idx2label[int(idx)] for idx in y_test]
predictions_human_readable = np.column_stack((np.array(x_text), all_labels, all_predictions))
title = ["txt","label_human","label_predict"]
predictions_human_readable = np.row_stack((np.array(title), predictions_human_readable))

out_path = os.path.join(FLAGS.checkpoint_dir, "prediction.csv")
print("Saving evaluation to {0}".format(out_path))
with open(out_path, 'w') as f:
    csv.writer(f).writerows(predictions_human_readable)