#!/usr/bin/env python
# coding: utf-8
import sys 
from threading import Timer
from Logger import logger

__author__ = 'Divyanshu Chauhan <divyanshu.chauhan@one97.net>'
__date__ = '24 Dec 2018'

class timer():

    log = logger.get_logger()

    def __init__(self, duration, periodicity, callback):
        self.duration = duration
        self.periodicity = periodicity
        self.callback = callback
        self.isRunning = False

    def create_timer(self):
        self.t = Timer(self.duration, self.expiry_handler)
        self.t.daemon = True

    def start(self):
        self.create_timer()
        timer.log.info ("Starting " + str(self.t) + " with duration " + str(self.duration) + " seconds")
        self.t.start()
        self.isRunning = True

    def stop(self):
        timer.log.info ("Stopping " + str(self.t) + " with duration " + str(self.duration) + " seconds")
        self.t.cancel()
        self.isRunning = False

    def expiry_handler(self):
        if (self.periodicity == 'oneshot'):
            self.callback()
        elif (self.periodicity == 'periodic'):
            self.callback()
            self.start()
        else:
            self.callback()
            timer.log.info ("Invalid value:" + str(self.periodicity))
            self.isRunning = False
