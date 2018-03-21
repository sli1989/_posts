#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:07:34 2017

@author: song
"""
import os

## path

cwd = os.getcwd() # the current working directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))   # the directory of the script being run

                            
print "cwd = ", cwd
print "ROOT_DIR =",ROOT_DIR
print "SCRIPT_DIR = ",SCRIPT_DIR

# pretrained wordvec path
wordvec_google_bin = ROOT_DIR + "/pretrained-model/GoogleNews-vectors-negative300.bin"
wordvec_google_dat = ROOT_DIR + "/pretrained-model/GoogleNews-vectors-negative300.dat"
wordvec_google_vocab = ROOT_DIR + "/pretrained-model/GoogleNews-vectors-negative300.vocab"


