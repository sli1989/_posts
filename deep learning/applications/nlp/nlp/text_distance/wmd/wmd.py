#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:44:45 2017

@author: song
@reference:  http://nbviewer.jupyter.org/github/vene/vene.github.io/blob/pelican/content/blog/word-movers-distance-in-python.ipynb
"""


import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer




from nlp.word_representation.model.word2vec import loader
W,vocab_list = loader.W,loader.vocab_list
vocab_dict = {w: k for k, w in enumerate(vocab_list)}








# add bigram
def wmd(text1, text2):
    from scipy.spatial.distance import cosine
    
    vect = CountVectorizer(stop_words="english").fit([text1, text2])
    print("Features:",  ", ".join(vect.get_feature_names()))
    
    v_1, v_2 = vect.transform([text1, text2])
    v_1 = v_1.toarray().ravel()
    v_2 = v_2.toarray().ravel()
    print(v_1, v_2)
    print("cosine_BOW(text_1, text_2) = {:.2f}".format(1-cosine(v_1, v_2)))
    
    from sklearn.metrics import euclidean_distances
    W_ = W[[vocab_dict[w] for w in vect.get_feature_names()]]
    D_ = euclidean_distances(W_)

    from pyemd import emd
    # pyemd needs double precision input
    v_1 = v_1.astype(np.double)
    v_2 = v_2.astype(np.double)
    v_1 /= v_1.sum()
    v_2 /= v_2.sum()
    D_ = D_.astype(np.double)
    D_ /= D_.max()  # just for comparison purposes
    return emd(v_1, v_2, D_)



###################### general interface ###################### 

# return the wmd of two text
def inference(text1, text2):
    return wmd(text1, text2)


###################### test1 ###################### 

if __name__ == "__main__":
    d1 = "(a)	Hertz may benchmark the Charges for the Services in the aggregate by domain of Services (i. e., AMS Services and/or CCS Services) once during the Term, beginning upon thestart of Contract Year 3."
    d2 = "(a) Beginning six (6) months after the end of Transition under the applicable Work Order, Freddie Mac may benchmark the Charges for one or more of the Service Tower each in the aggregate, provided that benchmarking of particular Charges cannot be undertaken more than one (1) time in any rolling two (2) year period during the Initial Term of the applicable Work Order."
    d3 = "(v) Unless otherwise agreed by the parties, IBM shall not be required as the result of a benchmarking to reduce the Charges for the benchmarked Services in total by more than five percent (5%) from the Charges that were originally in effect for the applicable Contract Year as of the Effective Date."
    print 1-inference(d1, d2)
    print inference(d1, d3)
    #print("d(doc_1, doc_2) = {:.2f}".format(distance))
    