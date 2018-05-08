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

colName = ['O. odorifera', 'O. diospyrifolia', 'O. puberula', 'C. dinisii',]
Par = ['Media_odo', 'Media_dio', 'Media_pub', 'Media_din']
#
fungo = 'A. alternata'
# fungo = 'A. flavus'
# fungo = 'P. crustosum'

###################

rd = ReadData(filename=filename, directory=direct, param=Par, colname=colName)

rd.loadData()

a = rd.readParam()


pl = PlotData(a, colName, figname=fungo+'_lin.png', directory=path+'/figs/', fungo=fungo, savePlot=True)


pl.plote(fitDegree=1)

######

#
##

#####
## Plot
###



# index=np.linspace(50,100,6)

# Alternaria = pd.DataFrame(np.transpose([data['Media_odo'], data['Media_dio'], data['Media_pub'], data['Media_din']]), columns= colName, index=index)
#
#
# x = index
# y = Alternaria[colName[1]]
#
# aa = polfit(x,y,2)
#
# # fit = np.polyfit(x,y, 2)
# fit_fn = np.poly1d(aa['polynomial'])
#
# print (aa['determination'])
#
# print (poly2latex(aa['polynomial']))
#
# ss = np.linspace(50,100,100)
#
# plt.plot(x,y, '.', ss, fit_fn(ss),'-')
# plt.text(80,6, poly2latex(aa['polynomial']))
# plt.show()
# exit()
#
#
# Alternaria.plot(subplots=True, layout=(2, 2), figsize=(6, 6), sharex=False)
# plt.show()

# plt.plot(a.index, a['Media C. dinisii'])
# plt.show()
