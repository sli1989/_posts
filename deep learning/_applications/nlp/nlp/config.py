#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:44:19 2017

@author: song

所有config都写在这，会导致项目过多耦合。可以先写在这儿，减少重复代码。后面解耦的时候再分开
"""



import os


cwd = os.getcwd() # the current working directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))   # the directory of the script being run

print "cwd = ", cwd
print "ROOT_DIR =",ROOT_DIR
print "SCRIPT_DIR = ",SCRIPT_DIR


