#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:18:53 2017

@author: song
"""



"""
Config for web_service only

"""

task = "similarity"
model = "wmd"
param = ""


"""
all models should implement "learning" and "inference" interface
"""
url = ["learning","inference"] # leanring/training  inference