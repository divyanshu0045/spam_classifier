#!/usr/bin/env python
# coding: utf-8
import sys 
from threading import Thread
from Logger import logger
from Queue import Queue

__author__ = 'Divyanshu Chauhan <divyanshu0045@gmail.com>'
__date__ = '24 Dec 2018'

class ThreadPool():

    log = logger.get_logger()
    PoolSize = 1

    def __init__(self):
        self.tlist = list()
        self.q = Queue(maxsize=0)
        for i in range(ThreadPool.PoolSize):
            t = Thread(target=self.worker)
            t.daemon = True
            ThreadPool.log.info("Created thread object for " + str(self.worker) + ". Worker no. " + str(i+1))
            t.start()
            ThreadPool.log.info("Started thread " + str(self.worker) + ". Worker no. " + str(i+1))
            self.tlist.append(t)

    def push(self, task):
        self.q.put(task, block=True)
        ThreadPool.log.info("Task pushed in queue:" + str(task[0]))

    def worker(self):
        while True:
            task = self.q.get(block=True)
            ThreadPool.log.info("Task recieved by worker:" + str(task[0]))
            try:
                func = task[0]
                args = task[1:]
                func(*args)
            except Exception as e:
                ThreadPool.log.info("Cant parse task:" + str(e))
            self.q.task_done()
                
                



