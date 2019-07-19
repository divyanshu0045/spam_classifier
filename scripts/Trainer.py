#!/usr/bin/env python
# coding: utf-8
import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from Utility import *
from threading import Lock
from Timer import timer
from Logger import logger
from Reader import Reader
import sys 

__author__ = 'Divyanshu Chauhan <divyanshu0045@gmail.com>'
__date__ = '24 Dec 2018'

class Trainer():

    TrainDataPickle = r"train_data.pickle"
    mutex = Lock()
    ContinousLearnerPeriodicity = 360 #every 6 minutes
    Vectorizer = CountVectorizer
    Classifier = MultinomialNB
    Transformer = TfidfTransformer
    log = logger.get_logger()
    model = None

    def __init__(self, dataset_path):
        Trainer.log.info("Starting Trainer...")
        self.data_reader = Reader(dataset_path)
        self.dataset = self.data_reader.get_dataset() 

    def model_maker(self, loadFromPickle = True):
        try:
            if (loadFromPickle == False):
                raise Exception('Load from pickle is disabled')
            with open(Trainer.TrainDataPickle,"rb") as vt:
                pipeline = pickle.load(vt)
                self.set_model(pipeline)
        except Exception as e:
            Trainer.log.info("Couldn't load training data:" + str(e))
            pipeline = Pipeline([('bow',Trainer.Vectorizer(analyzer=process_text)), ('classifier',Trainer.Classifier())])
            pipeline.fit(self.dataset.text, self.dataset.cls)
            self.set_model(pipeline)
            with open(Trainer.TrainDataPickle,"wb") as vt:
                pickle.dump(pipeline, vt)
        Trainer.log.info("model created...")
            
    def get_model(self):
        Trainer.mutex.acquire()
        current_model =  Trainer.model
        Trainer.mutex.release()
        return current_model

    def set_model(self, model):
        Trainer.mutex.acquire()
        Trainer.model = model
        Trainer.mutex.release()

    def get_train_dataset(self):
        return self.dataset

    def continous_learner(self):
        Trainer.log.info("Starting Trainer...")
        self.data_reader.set_dataset()
        self.dataset = self.data_reader.get_dataset()
        self.model_maker(loadFromPickle = False)
        Trainer.log.info("Model Updated...")

    def periodic_continous_learner(self):
        t = timer(Trainer.ContinousLearnerPeriodicity, 'periodic', self.continous_learner)
        t.start()
