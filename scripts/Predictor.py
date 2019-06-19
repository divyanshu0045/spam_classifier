#!/usr/bin/env python
# coding: utf-8

from nltk.stem.porter import PorterStemmer
from Utility import *
from Logger import logger
import sys
import pandas as pd
from time import time

__author__ = 'Divyanshu Chauhan <divyanshu.chauhan@one97.net>'
__date__ = '24 Dec 2018'

class Predictor():

    log = logger.get_logger()

    def __init__(self, classifier_model):
        self.classifier_model = classifier_model

    def predict(self, data):
        if (type(data) == type(pd.Series(list()))):
            s = time()
            predict = self.classifier_model.predict(data)
            e = time()
        else:
            s = time()
            predict = self.classifier_model.predict([data])
            e = time()
        Predictor.log.info('Prediction:' + str(e-s) + ' secs:' + str(predict))
        return str(predict)

    def accuracy(self, data, verify_against):
        if (type(data) == type(pd.Series(list()))):
            score = self.classifier_model.score(data, verify_against)
            Predictor.log.info('Score:' + str(score))
        else:
            score = self.classifier_model.score([data], [verify_against])
            Predictor.log.info('Score:' + str(score) + ' where y=' + str(verify_against))
        return str(score)

    def probabilty(self, data):
        if (type(data) == type(pd.Series(list()))):
            prob = self.classifier_model.predict_proba(data)
        else:
            prob = self.classifier_model.predict_proba([data])
        Predictor.log.info('Probability:' + str(prob))     
        return str(prob)
