#!/usr/bin/env python2
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
"""
Created onmain. May  8, 2018

@author: jose
"""
from ManageData import ReadData
from PlotData import PlotData
import os

filename = 'Dados_Alternaria_Alternata.csv'
# filename = 'Dados_Aspergillus_flavus.csv'
# filename = 'Dados_Penicillium_crustosum.csv'
path = os.getcwd()
direct = path+'/data/'

# colName = ['O. odorifera', 'O. diospyrifolia', 'O. puberula', 'C. dinisii',]
# Par = ['Media_odo', 'Media_dio', 'Media_pub', 'Media_din']
colName = ['O. odorifera', 'O. diospyrifolia','C. dinisii',]
Par = ['Media_odo', 'Media_dio', 'Media_din']
#
fungo = 'A. alternata'
# fungo = 'A. flavus'
# fungo = 'P. crustosum'

###################

rd = ReadData(filename=filename, directory=direct, param=Par, colname=colName)

rd.loadData()

a = rd.readParam()


pl = PlotData(a, colName, figname=fungo+'_quad3p.png', directory=path+'/figs/', fungo=fungo, savePlot=True)


pl.plote(fitDegree=2)
