import numpy as np
import csv
import re
import itertools
from collections import Counter
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split

class preprocessor:
    """
    better move to text.py
    reference: tensorflow.preprocessing.text.py
    """
    @staticmethod
    def clean_str(string):
        """
        Tokenization/string cleaning for all datasets except for SST.
        Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
        """
        string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
        string = re.sub(r"\'s", " \'s", string)
        string = re.sub(r"\'ve", " \'ve", string)
        string = re.sub(r"n\'t", " n\'t", string)
        string = re.sub(r"\'re", " \'re", string)
        string = re.sub(r"\'d", " \'d", string)
        string = re.sub(r"\'ll", " \'ll", string)
        string = re.sub(r",", " , ", string)
        string = re.sub(r"!", " ! ", string)
        string = re.sub(r"\(", " \( ", string)
        string = re.sub(r"\)", " \) ", string)
        string = re.sub(r"\?", " \? ", string)
        string = re.sub(r"\s{2,}", " ", string)
        return string.strip().lower()


class VocabularyProcessor:
    '''
    not need, has been implemented in tf.learn
    '''
    def fit():
        pass
    def transform():
        pass
    def fit_and_transform():
        pass
    
    
    
class datasets:
    @staticmethod
    def load_datasets_treebank():
        '''
        Reference: https://github.com/JonathanRaiman/pytreebank
        '''
        import pytreebank
        treebank_path = "/data/xs/datasets/SentimentTreebank/trainDevTestTrees_PTB/trees"
        dataset = pytreebank.load_sst(treebank_path)
        #train_data = pytreebank.import_tree_corpus("/path/to/sentiment/train.txt")
        example = dataset["train"][0]
        
        # extract spans from the tree.
        X_train = []
        X_test = []
        y_train = []
        y_test = []
        for example in dataset["train"]:
            y_train.append(example.to_labeled_lines()[0][0])
            X_train.append(example.to_labeled_lines()[0][1])
        
        for example in dataset["test"]:
            y_test.append(example.to_labeled_lines()[0][0])
            X_test.append(example.to_labeled_lines()[0][1])       
        
        return [X_train, X_test, y_train, y_test]
    @staticmethod
    def load_datasets_bluescan(data_file):
        """
        load all datasets (train and test)
        """
        f = open(data_file)
        reader = csv.reader(f, delimiter="\t")
        data = list(reader)
        data = np.array(data)
        y = data[:,0].tolist()
        x_text = data[:,1].tolist()
        x_text = [preprocessor.clean_str(sent) for sent in x_text]
        f.close()
        return x_text, y
    
    @staticmethod
    def load_datasets_20newsgroup(subset='train', categories=None, shuffle=True, random_state=42):
        """
        Retrieve data from 20 newsgroups
        :param subset: train, test or all
        :param categories: List of newsgroup name
        :param shuffle: shuffle the list or not
        :param random_state: seed integer to shuffle the dataset
        :return: data and labels of the newsgroup
        """
        datasets = fetch_20newsgroups(subset=subset, categories=categories, shuffle=shuffle, random_state=random_state)
        return datasets
    
    
    @staticmethod
    def load_datasets_mrpolarity_(positive_data_file, negative_data_file):
        """
        Loads MR polarity data from files, splits the data into words and generates labels.
        Returns split sentences and labels.
        
        Reference: http://www.cs.cornell.edu/people/pabo/movie-review-data/   
            sentence_polarity_dataset_v1.0: http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz
        """
        # Load data from files
        positive_examples = list(open(positive_data_file, "r").readlines())
        positive_examples = [s.strip() for s in positive_examples]
        negative_examples = list(open(negative_data_file, "r").readlines())
        negative_examples = [s.strip() for s in negative_examples]
        # Split by words
        x_text = positive_examples + negative_examples
        x_text = [preprocessor.clean_str(sent) for sent in x_text]
        # Generate labels
        positive_labels = [[0, 1] for _ in positive_examples]
        negative_labels = [[1, 0] for _ in negative_examples]
        y = np.concatenate([positive_labels, negative_labels], 0)
        return [x_text, y]

    @staticmethod
    def train_test_split(X, y, test_size=0.25):
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
        return [X_train, X_test, y_train, y_test]
    
    @staticmethod
    def save_data(X, y, path):
        text = ""
        for i in range(len(y)):
            text = text + y[i] + "\t" + X[i] + "\n"
            
        fo = open(path, "w")
        fo.write(text)
        fo.close()


class label_processor:
    '''
    y = [1, 2, 6, 4, 2]
        x_text, y = merge(x_text, y)
    x_text, y = removeLowCount(x_text, y)
    
    .fit(y)
    .classes_
    .transform([1, 6])
    array([[1, 0, 0, 0],
           [0, 0, 0, 1]])
    '''
    
    def __init__(self):
        
        self.idx2label = None
        self.label2count = None
        self.label2idx = None
        self.isMerge = True
        self.isRemoveLowCount = True
        merger_SST = {0:0,1:0,3:1,4:1} # with neutral reviews removed and binary labels.
        merger_bluescan = {"#laws":"#laws", "#dispute resolution":"#laws", "#verification":"#verification", 
        "#objective":"#contract","#risk of loss":"#verification","#responsibilities":"#responsibilities",
        #"#other terms":"#other terms",
        "#validity of contract":"#contract","#contract":"#contract","#validity":"#contract",
        "#liability":"#liability","#limitation of liability":"#liability","#prevail":"#contract",
        "#objective &charges":"#contract", "#growth relationship offering":"#contract","#compliance with laws":"#laws",
        "#definition":"#contract","#product":"#program","#termination":"#contract","#programs":"#program","#program":"#program","#law":"#laws",
        "#service":"#program","#charges-payment":"#charges-payment","#contract period":"#contract",
        "#charges - payment":"#charges - payment","#charges":"#charges - payment","#products":"#program",
        "#statute of limitations for bringing a claim":"#liability","#warranties":"#warranties",
        "#intellectual property":"#intellectual property","#taxes - payment":"#charges-payment",
        "#delivery":"#program","#payment":"#charges-payment","#guarantee":"#guarantees","#guarantees":"#guarantees",
        "#charges - paygment":"#charges-payment","#not to exceed":"#pricing","#warranty":"#warranties",
        "#liability and indemnity":"#liability","#compliance":"#compliance"}  # with root labels
        self.merger = merger_bluescan

    def preprocess(self, x_text, y_text):
        x_text, y_text = self.merge(x_text, y_text)
        x_text, y_text = self.removeLowCount(x_text, y_text)
        
        return x_text,y_text
     
    def merge(self, x_text, y_text):
        '''
        1. label to index
        2. merge hierachical label
        3. remove data not in label set
        
        '''
        
        all_idx = [i for i in range(len(y_text)) if self.merger.has_key(y_text[i])]
        y_text = [self.merger[y_text[i]] for i in all_idx]
        x_text = [x_text[i] for i in all_idx]
        print "Merging labels..."
        
        return x_text, y_text
    


    
    
    def removeLowCount(self, x_text, y):
        '''
        '''
        print "Removing low_count_label... : "
        low_bound = 2
        self.label2count = {}
        for label in set(y):
            count = y.count(label) 
            self.label2count[label] = count
            if count < low_bound:
                print label
            
            
        remove_indices = [i for i in range(len(y)) if y.count(y[i]) < low_bound]
        x_text = [i for j, i in enumerate(x_text) if j not in remove_indices]
        y = [i for j, i in enumerate(y) if j not in remove_indices]
        return x_text, y
        
    def fit_transform(self, y_text):
        self.fit(y_text)
        return self.transform(y_text)
        
    
    def fit(self, y):
        '''
        '''
        # Generate labels
        self.idx2label = list(set(y))
        
        # label2idx
        self.label2idx = {}
        for i in range(len(self.idx2label)):
            self.label2idx[self.idx2label[i]] = i
        
        
    
    def transform(self, y_text):
        ''' transform to index
        y = ["pair", "beijing", "nanjing"]
        
        '''
        if self.isMerge:
            return [self.label2idx[self.merger[y_text[i]]] for i in range(len(y_text))]
        else:
            return [self.label2idx[y_text[i]] for i in range(len(y_text))]
        
    
    def transform_binary(self, y_text, length):
        ''' transform to one-hot encoding
        
        '''
        y_index = self.transform(y_text)
        return self.index_to_onehot(y_index, length)
    
    
    
    @staticmethod
    def index_to_onehot(index, length):
        oneHot = np.zeros((len(index), length))
        for i in range(len(index)):
            oneHot[i, index[i]] = 1
        return oneHot
    
    @staticmethod
    def onehot_to_index(one_hot):
        idxLabel = ([np.where(one_hot[i,:]>=1)[0][0] for i in range(one_hot.shape[0])] )
        return idxLabel
    
    def idx2label(self, i):
        return self.idx2label[i]
    
    def save_idx2label(self, path):
        labels = "\n".join(self.idx2label)
        fo = open(path, "w")
        fo.write(labels)
        fo.close()
        
    def load_idx2label(self, path):
        fo = open(path, "r")
        self.idx2label = fo.readlines()
        self.idx2label = [label.strip() for label in self.idx2label]
        fo.close()
        
        # label2idx
        self.label2idx = {}
        for i in range(len(self.idx2label)):
            self.label2idx[self.idx2label[i]] = i
                          
        return self.idx2label
        



# https://github.com/cahya-wirawan/cnn-text-classification-tf/blob/master/data_helpers.py
def load_data_labels(datasets):
    """
    Load data and labels
    :param datasets:
    :return:
    """
    # Split by words
    x_text = datasets['data']
    x_text = [preprocessor.clean_str(sent) for sent in x_text]
    # Generate labels
    labels = []
    for i in range(len(x_text)):
        label = [0 for j in datasets['target_names']]
        label[datasets['target'][i]] = 1
        labels.append(label)
    y = np.array(labels)
    return [x_text, y]



def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]




class word2vec: 
    '''
    input:
        wordList(id2word): traverse 
        or 
        wordDict(word2id):
    
    output:
        embedding_dict:
        or
        vocab_vec:
    
    '''
    @staticmethod    
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
    
    @staticmethod
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
    @staticmethod
    def load_embedding_vectors_glove(vocabulary, filename, vector_size):
        """
        load embedding_vectors from the glove
        initial matrix with random uniform
        
        pros: 1. fast
        cons: 1. can not get oov
        """
        #embedding_vectors = np.random.uniform(-0.25, 0.25, (len(vocabulary), vector_size))
        embedding_vectors = np.zeros((len(vocabulary), vector_size))
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
    
    
    @staticmethod
    def load_embedding_vectors_glove_xs(filename, wordmap):
        """
        load embedding_vectors from the glove
        initial matrix with random uniform
        
        pros: 1. can get oov
        cons: 1. slow
        """
        w2v = word2vec.load_txt_vec(filename, wordmap)
        for word in w2v:
            vector_size = len(w2v[word])
            break
        
        #embedding_vectors = np.random.uniform(-0.25, 0.25, (len(vocabulary), vector_size))
        embedding_vectors = np.zeros((len(wordmap), vector_size))
        
        oov = []
        for i in range(len(wordmap)):
            word = wordmap[i]
            if (w2v.has_key(word)):
                embedding_vectors[i] = np.asarray(w2v[word], dtype="float32")
            else:
                oov.append(word)

        print "OOV" 
        print oov
        return embedding_vectors

