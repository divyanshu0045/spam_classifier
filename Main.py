#!/usr/bin/env python
# coding: utf-8
import sys
from scripts import *
from time import time
from sklearn.model_selection import train_test_split
from time import sleep
__author__ = 'Divyanshu Chauhan <divyanshu0045@gmail.com>'
__date__ = '24 Dec 2018'

log = logger.get_logger()
tpool = ThreadPool()

def non_interactive(p):
    global log
    global tpool
    msg = Reader(dataset_path='datasets/spam_test.csv').get_dataset()
    result = p.predict(msg.text)
    result = p.accuracy(msg.text, msg.cls)

def interactive(p):
    global log
    global tpool
    msg = raw_input('Enter Text to Predict:')
    log.info('Text to predict:' + msg)
    result = p.predict(msg)
    result = p.probabilty(msg)
    result = p.accuracy(msg, 'ham')

def main():
    global log
    global tpool
    #change 'interactive_mode' to True if you want to give predictor input yourself
    #change 'interactive_mode' to False if you want to run predictor on test dataset
    interactive_mode = True
    t = Trainer(dataset_path='datasets/spam_train.csv')
    model = t.model_maker()
    p = Predictor(t.get_model())
    t.periodic_continous_learner()
    while True:
        if interactive:
            tpool.push((interactive, p))
        else:
            tpool.push((non_interactive, p))
        sleep(30)

if __name__ == '__main__':
    main()
