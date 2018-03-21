#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:36:31 2017

@author: song
"""


'''

    >>> from gensim.models.keyedvectors import KeyedVectors
    >>> word_vectors = KeyedVectors.load_word2vec_format('/tmp/vectors.txt', binary=False)  # C text format
    >>> word_vectors = KeyedVectors.load_word2vec_format('/tmp/vectors.bin', binary=True)  # C binary format


'''


import numpy as np
import re
import os

import config


print config.wordvec_google_dat
os.path.exists(config.wordvec_google_dat)




def default_loader():
    return load_cache()


def load_cache():
    """
    reference: http://nbviewer.jupyter.org/github/vene/vene.github.io/blob/pelican/content/blog/word-movers-distance-in-python.ipynb
    可以考虑使用单例
    
    """
    if not os.path.exists(config.wordvec_google_dat):
        print("Caching word embeddings in memmapped format...")
        from gensim.models.keyedvectors import KeyedVectors
        
        wv = KeyedVectors.load_word2vec_format(config.wordvec_google_bin,
            binary=True)
        fp = np.memmap(config.wordvec_google_dat, dtype=np.double, mode='w+', shape=wv.syn0.shape)
        fp[:] = wv.syn0[:]
        with open(config.wordvec_google_vocab, "w") as f:
            for _, w in sorted((voc.index, word) for word, voc in wv.vocab.items()):
                f.write(w.encode('utf8') + "\n")
        del fp, wv
    W = np.memmap(config.wordvec_google_dat, dtype=np.double, mode="r", shape=(3000000, 300))
    with open(config.wordvec_google_vocab) as f:
        vocab_list = map(str.strip, f.readlines())
    print "cache finished"
    return W,vocab_list

W,vocab_list = default_loader();
    
def load_txt_vec(fname, wordmap):
    """
    Loads 300x1 word vecs from Google (Mikolov) word2vec
    """
    num=0
    word_vecs = {}
    wordvecfile=open(fname,'r')
    for line in wordvecfile:
        num+=1
        if num%1000000==0:
            print ("load words",num)
        line=line.strip()
        elements=re.split('\s+',line)
        word=elements[0]
       # print word
        if word in wordmap:
            vector=[]
            for i in range(1,len(elements)):
                vector.append(float(elements[i]))
            word_vecs[word]=vector
            
    return word_vecs


def load_bin_vec(fname, wordmap):
    """
    Loads 300x1 word vecs from Google (Mikolov) word2vec
    """
    word_vecs = {}
    num=0
    with open(fname, "rb") as f:
        header = f.readline()
        vocab_size, layer1_size = map(int, header.split())
        print "word num "+str(vocab_size)
        binary_len = np.dtype('float32').itemsize * layer1_size
        for line in xrange(vocab_size):
            word = []
            while True:
                ch = f.read(1)
                if ch == ' ':
                    word = ''.join(word)
                    break
                if ch != '\n':
                    word.append(ch)
           # word=word.decode('utf8')
            if word in wordmap:
               #print word
               word_vecs[word] = np.fromstring(f.read(binary_len), dtype='float32')
            else:
                f.read(binary_len)
            num+=1
            if num%1000000==0:
                print ("load words",num)
            
    return word_vecs

# from https://github.com/cahya-wirawan/cnn-text-classification-tf/blob/master/data_helpers.py
def load_embedding_vectors_glove(vocabulary, filename, vector_size):
    """
    load embedding_vectors from the glove
    initial matrix with random uniform
    """
    embedding_vectors = np.random.uniform(-0.25, 0.25, (len(vocabulary), vector_size))
    f = open(filename)
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], dtype="float32")
        idx = vocabulary.get(word)
        if idx != 0:
            embedding_vectors[idx] = vector
    f.close()
    return embedding_vectors