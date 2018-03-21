#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:25:31 2017

@author: song
"""

import web
from nlp.text_distance.wmd import wmd

d1 = "Obama speaks to the media in Illinois"
d2 = "The President addresses the press in Chicago"
print wmd.inference(d1,d2)

class text_distance:
    
    def POST(self):
        getInput = web.input()
        print getInput
        
        # convert jsonArray to a list of string
        if not getInput.text1:
            return "no training path"
        else:
            print getInput.text1
            
            
            distance = wmd.inference(getInput.text1, getInput.text2)
            print distance
            
            return distance