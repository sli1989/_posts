#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:11:38 2017

@author: song
"""

from text_distance import text_distance

urls = (
    ## word service
    '/','index',
    '/nlp/word/distance','word_distance',
    
    ## text service
    '/nlp/text/classification', 'text_classification',
    '/nlp/text/distance', 'text_distance'
)


import web
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()



class index:
    def GET(self):
        with open('index.html', 'r') as content_file:
            return content_file.read()