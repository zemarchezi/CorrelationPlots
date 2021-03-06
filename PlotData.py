#!/usr/bin/env python2
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
"""
Created on Tue May  8 2018

@author: jose
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ManageData import FittingData, poly2latex
import os

class PlotData():
    """docstring for PlotData."""
    def __init__(self, data, param, figname='', directory='', fungo='', savePlot=True):
        self.arg = data
        self.param = param
        self.figname = figname
        self.savePlot = savePlot
        self.dir = directory
        self.fungo = fungo

    def plote(self, fitDegree=1):
        self.degree = fitDegree
        self.fitCurve = []
        self.pollatex = []
        self.rSquare = []
        ss = np.linspace(50,100,100)
        for i in self.param:
            ft = FittingData(self.arg.index, self.arg[i], self.degree)
            pol = ft.polfit()
            fit_fn = np.poly1d(pol['polynomial'])

            self.fitCurve.append(fit_fn(ss))
            self.rSquare.append(pol['determination'])
            self.pollatex.append(poly2latex(pol['polynomial'], variable="x", width=self.degree))

        self.fitcurve = pd.DataFrame(np.transpose(self.fitCurve), columns=self.param, index=ss)

        # fig, axarr = plt.subplots(2, 2, figsize=(6,6),sharey=False, sharex=True)
        # fig.suptitle('$\t{%s}$' % (self.fungo),fontsize=15)
        # fig.text(0.04, 0.5, u'Diâmetro do Halo (mm)', va='center', rotation='vertical')
        # fig.text(0.5, 0.04, u'Concentração de óleo essencial (%)', ha='center')
        # plt1 = axarr[0,0].plot(self.arg.index, self.arg[self.param[0]], '.', ms=8)
        # plt1 = axarr[0,0].plot(ss, self.fitCurve[0],'-')
        # # max and min y
        # axarr[0,0].set_ylim(np.min(self.arg[self.param[0]])-1,np.max(self.arg[self.param[0]])+1)
        # # axarr[0,0].grid(color='gray',linestyle='--')
        # axarr[0,0].set_title('$\t{%s}$' %(self.param[0]))
        # axarr[0,0].text(55,np.max(self.arg[self.param[0]])-1, 'y = ' + self.pollatex[0]+'\n $R^2$ = %0.3f' %  (self.rSquare[0]), fontsize=8)
        #
        #
        # plt2 = axarr[0,1].plot(self.arg.index, self.arg[self.param[1]], '.', ms=8)
        # plt2 = axarr[0,1].plot(ss, self.fitCurve[1],'-')
        # # max and min y
        # axarr[0,1].set_ylim(np.min(self.arg[self.param[1]])-1,np.max(self.arg[self.param[1]])+1)
        # # axarr[0,1].grid(color='gray',linestyle='--')
        # axarr[0,1].set_title('$\t{%s}$' %(self.param[1]))
        # axarr[0,1].text(55,np.max(self.arg[self.param[1]])-1.5, 'y = ' + self.pollatex[1]+'\n $R^2$ = %0.3f' %  (self.rSquare[1]), fontsize=8)
        #
        # plt3 = axarr[1,0].plot(self.arg.index, self.arg[self.param[2]], '.', ms=8)
        # plt3 = axarr[1,0].plot(ss, self.fitCurve[2],'-')
        # # max and min y
        # axarr[1,0].set_ylim(np.min(self.arg[self.param[2]])-1,np.max(self.arg[self.param[2]])+1)
        # # axarr[1,0].grid(color='gray',linestyle='--')
        # axarr[1,0].set_title('$\t{%s}$' %(self.param[2]))
        # axarr[1,0].text(55,np.max(self.arg[self.param[2]])-1, 'y = ' + self.pollatex[2]+'\n $R^2$ = %0.3f' %  (self.rSquare[2]), fontsize=8)
        #
        # plt4 = axarr[1,1].plot(self.arg.index, self.arg[self.param[3]], '.', ms=8)
        # plt4 = axarr[1,1].plot(ss, self.fitCurve[3],'-')
        # # max and min y
        # axarr[1,1].set_ylim(np.min(self.arg[self.param[3]])-1,np.max(self.arg[self.param[3]])+1)
        # # axarr[1,1].grid(color='gray',linestyle='--')
        # axarr[1,1].set_title('$\t{%s}$' %(self.param[3]))
        # axarr[1,1].text(55,np.max(self.arg[self.param[3]])-1.7, 'y = ' + self.pollatex[3]+'\n $R^2$ = %0.3f' %  (self.rSquare[3]), fontsize=8)
        # if self.savePlot:
        #     plt.savefig(self.dir + self.figname, format='png')

        # fig, axarr = plt.subplots(1, 3, figsize=(7,3),sharey=False, sharex=True)
        # plt.subplots_adjust(left=0.09, bottom=0.2, top=0.8, right=0.98, wspace=0.3)
        # fig.suptitle('$\t{%s}$' % (self.fungo),fontsize=15)
        # fig.text(0.02, 0.5, u'Diâmetro do Halo (mm)', va='center', rotation='vertical')
        # fig.text(0.5, 0.04, u'Concentração de óleo essencial (%)', ha='center')
        # plt1 = axarr[0].plot(self.arg.index, self.arg[self.param[0]], '.', ms=8)
        # plt1 = axarr[0].plot(ss, self.fitCurve[0],'-')
        # # max and min y
        # axarr[0].set_ylim(np.min(self.arg[self.param[0]])-1,np.max(self.arg[self.param[0]])+1)
        # # axarr[0,0].grid(color='gray',linestyle='--')
        # axarr[0].set_title('$\t{%s}$' %(self.param[0]))
        # axarr[0].text(52,np.max(self.arg[self.param[0]])-1, 'y = ' + self.pollatex[0]+'\n $R^2$ = %0.3f' %  (self.rSquare[0]), fontsize=7)
        #
        #
        # plt2 = axarr[1].plot(self.arg.index, self.arg[self.param[1]], '.', ms=8)
        # plt2 = axarr[1].plot(ss, self.fitCurve[1],'-')
        # # max and min y
        # axarr[1].set_ylim(np.min(self.arg[self.param[1]])-1,np.max(self.arg[self.param[1]])+1)
        # # axarr[0,1].grid(color='gray',linestyle='--')
        # axarr[1].set_title('$\t{%s}$' %(self.param[1]))
        # axarr[1].text(52,np.max(self.arg[self.param[1]])-1.5, 'y = ' + self.pollatex[1]+'\n $R^2$ = %0.3f' %  (self.rSquare[1]), fontsize=7)
        #
        # plt3 = axarr[2].plot(self.arg.index, self.arg[self.param[2]], '.', ms=8)
        # plt3 = axarr[2].plot(ss, self.fitCurve[2],'-')
        # # max and min y
        # axarr[2].set_ylim(np.min(self.arg[self.param[2]])-1,np.max(self.arg[self.param[2]])+1)
        # # axarr[1,0].grid(color='gray',linestyle='--')
        # axarr[2].set_title('$\t{%s}$' %(self.param[2]))
        # axarr[2].text(50,np.max(self.arg[self.param[2]])-1.9, 'y = ' + self.pollatex[2]+'\n $R^2$ = %0.3f' %  (self.rSquare[2]), fontsize=7)
        #
        # if self.savePlot:
        #     plt.savefig(self.dir + self.figname, format='png')

        fig, axarr = plt.subplots(1, 1, figsize=(7,7),sharey=False, sharex=True)
        plt.subplots_adjust(left=0.09, bottom=0.2, top=0.8, right=0.98, wspace=0.3)
        # fig.suptitle('$\t{%s}$' % (self.fungo),fontsize=15)
        # fig.text(0.02, 0.5, u'Diâmetro do Halo (mm)', va='center', rotation='vertical')
        # fig.text(0.5, 0.04, u'Concentração de óleo essencial (%)', ha='center')
        # plt1 = self.arg.plot()
        plt1 = self.fitcurve.plot(style=['r','g','b'])
        plt.title('$\t{%s}$' % (self.fungo))
        plt.xlabel(u'Concentração de óleo essencial (%)')
        plt.ylabel(u'Diâmetro do Halo (mm)')
        plt.text(60,13, 'y = ' + self.pollatex[0]+'\n $R^2$ = %0.3f' %  (self.rSquare[0]), fontsize=9, color='red')
        plt.text(75,6, 'y = ' + self.pollatex[1]+'\n $R^2$ = %0.3f' %  (self.rSquare[1]), fontsize=9, color='g')
        plt.text(52,9, 'y = ' + self.pollatex[2]+'\n $R^2$ = %0.3f' %  (self.rSquare[2]), fontsize=9, color='b')
        # # max and min y
        # axarr[0].set_ylim(np.min(self.arg[self.param[0]])-1,np.max(self.arg[self.param[0]])+1)
        # # axarr[0,0].grid(color='gray',linestyle='--')
        # axarr[0].set_title('$\t{%s}$' %(self.param[0]))
        # axarr[0].text(52,np.max(self.arg[self.param[0]])-1, 'y = ' + self.pollatex[0]+'\n $R^2$ = %0.3f' %  (self.rSquare[0]), fontsize=7)
        #
        #
        # plt2 = axarr[1].plot(self.arg.index, self.arg[self.param[1]], '.', ms=8)
        # plt2 = axarr[1].plot(ss, self.fitCurve[1],'-')
        # # max and min y
        # axarr[1].set_ylim(np.min(self.arg[self.param[1]])-1,np.max(self.arg[self.param[1]])+1)
        # # axarr[0,1].grid(color='gray',linestyle='--')
        # axarr[1].set_title('$\t{%s}$' %(self.param[1]))
        # axarr[1].text(52,np.max(self.arg[self.param[1]])-1.5, 'y = ' + self.pollatex[1]+'\n $R^2$ = %0.3f' %  (self.rSquare[1]), fontsize=7)
        #
        # plt3 = axarr[2].plot(self.arg.index, self.arg[self.param[2]], '.', ms=8)
        # plt3 = axarr[2].plot(ss, self.fitCurve[2],'-')
        # # max and min y
        # axarr[2].set_ylim(np.min(self.arg[self.param[2]])-1,np.max(self.arg[self.param[2]])+1)
        # # axarr[1,0].grid(color='gray',linestyle='--')
        # axarr[2].set_title('$\t{%s}$' %(self.param[2]))
        # axarr[2].text(50,np.max(self.arg[self.param[2]])-1.9, 'y = ' + self.pollatex[2]+'\n $R^2$ = %0.3f' %  (self.rSquare[2]), fontsize=7)

        if self.savePlot:
            plt.savefig(self.dir + self.figname, format='png')
