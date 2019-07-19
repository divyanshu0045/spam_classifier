#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from Utility import *
from Logger import logger


__author__ = 'Divyanshu Chauhan <divyanshu0045@gmail.com>'
__date__ = '24 Dec 2018'

class Reader():

    log = logger.get_logger()

    def __init__(self, dataset_path="datasets/spam.csv"):
        self.set_dataset(dataset_path)

    def get_dataset(self):
        return self.dataset

    def set_dataset(self, dataset_path="datasets/spam.csv"):
        Reader.log.info("Reading " + dataset_path)
        self.dataset = pd.read_csv(dataset_path, encoding = "latin1")
        self.dataset = self.dataset.fillna('')
        self.dataset = self.dataset.rename(columns={'v1': 'cls','v2': 'text'})
        self.dataset = self.dataset.dropna(how='all', axis='columns')
        self.dataset = self.dataset.dropna(how='all', axis='index')
        self.dataset['length'] = self.dataset['text'].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii'))
        self.dataset['length'] = self.dataset['text'].apply(len)
        Reader.log.info("Reading Completed")
        Reader.log.debug('\n' + str(self.dataset))

