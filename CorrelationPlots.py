#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 19:34:17 2018

@author: jose
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class CorrelationPlot():
    """docstring for ."""
    def __init__(self, filename=''):
        super(, self).__init__()
        self.filenam = filenam
        self.param = None
        self.data = None

    def loadData(self):
        self.data = pd.read_csv(self.filenam)

    def readParam(self, param=''):
        
