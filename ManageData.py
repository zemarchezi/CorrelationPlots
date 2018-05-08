#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 19:34:17 2018

@author: jose
"""

import pandas as pd
import numpy as np
import os


class ReadData():
    """docstring for ."""
    def __init__(self, filename='',directory='', param=[], colname=[]):
        self.filenam = filename
        self.directory = directory
        self.colName = colname
        self.param = param
        self.data = None

    def loadData(self):
        self.data = pd.read_csv(self.directory+self.filenam)
        self.index = np.linspace(50,100,6)

    def readParam(self):
        self.colum = []
        for i in self.param:
            self.colum.append(self.data[i])
        self.frame = pd.DataFrame(np.transpose(self.colum), columns= self.colName, index=self.index)

        return self.frame


class FittingData():
    """docstring for ."""
    def __init__(self, x, y, degree):
        self.x = x
        self.y = y
        self.degree = degree

    def polfit(self):
        # Polynomial Regression
        self.results = {}
        coeffs = np.polyfit(self.x, self.y, self.degree)

         # Polynomial Coefficients
        self.results['polynomial'] = coeffs.tolist()

        # r-squared
        p = np.poly1d(coeffs)
        # fit values, and mean
        yhat = p(self.x)                         # or [p(z) for z in x]
        ybar = np.sum(self.y)/len(self.y)          # or sum(y)/len(y)
        ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
        sstot = np.sum((self.y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
        self.results['determination'] = ssreg / sstot

        return (self.results)

def poly2latex(poly, variable="x", width=2):
    t = ["{0:0.{width}f}"]
    t.append(t[-1] + " {variable}")
    t.append(t[-1] + "^{1}")

    def f():
        for i, v in enumerate(reversed(poly)):
            idx = i if i < 2 else 2
            yield t[idx].format(v, i, variable=variable, width=width)

    return "${}$".format("+".join(f()))



#
#
#     def plots(self, layout, numbOfPlots):
#         pass


# for i, v in enumerate(reversed(pol['polynomial'])):
#     idx = i if i < 2 else 2
#     yield t[idx].format(v, i, variable=variable, width=2)
