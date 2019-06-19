#!/usr/bin/env python
# coding: utf-8
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
import os
import sys 
from Logger import logger

__author__ = 'Divyanshu Chauhan <divyanshu.chauhan@one97.net>'
__date__ = '24 Dec 2018'

log = logger.get_logger()

def process_text(text):
   
    #1
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    #2
    clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    
    #3
    stemmer = PorterStemmer()
    clean_words = [stemmer.stem(word) for word in clean_words]

    return clean_words

def write_results_to_file(line):
    exists = os.path.isfile('test_score.csv')
    if exists:
        with open('test_score.csv', 'a') as file:
            for row in csv_arr:
                csvfile.write(line)
                csvfile.write('\n')
    else:
        with open('test_score.csv', 'w') as file:
            csvfile.write('`'.join(['#', 'text', 'answer', 'predict', 'result']))
            csvfile.write('\n')


