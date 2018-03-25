#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:25:17 2017

@author: song
"""


'''
reference: 
    1. watson NLC: https://www.ibm.com/watson/developercloud/natural-language-classifier/api/v1
    2. songfang NLC

'''

import web
from eval_NLC import eval
import json

''' TODO:
    restAPI: nlc/train nlc/status  nlc/predict
    
    form for send request
'''

class text_classification:
    def __init__(self):
        self.x_train=[]
        self.y_train=[]
        self.x_test=[]
        self.y_test=[]
        
        #self.eval = eval()
    
    def GET(self):
        getInput = web.input(text=None)
        
        # convert jsonArray to a list of string
        if not getInput.text:
            return "no training path"
        else:
            print getInput.text
            
            evalss = eval()
            labels = evalss.eval(json.loads(getInput.text))
            
            print labels
            return json.dumps(labels)
            '''
            self.x_test = json.loads(getInput.text)
            return self.classify(self.x_test)
            '''
        
    def classify(self, text):
        evalss = eval()
        return evalss.eval(text)
    
    
    def train(self):
        pass
        