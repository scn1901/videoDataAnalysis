import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
import sys

##########################
# function name: cumulativeGraph
# date: 03.10.2021
# update: 03.22.2021
# description: display cumulative graph in a grid

np.seterr(divide='ignore', invalid='ignore')

def cumulativeGraph(DataClass):
	
	res = []
	x = []
	i = 0
	for i in range(0,6):
		res.append(stats.cumfreq(DataClass.fileData[i], numbins=400))
		x.append(res[i].lowerlimit + np.linspace(0, res[i].binsize*res[i].cumcount.size, res[i].cumcount.size))

	i = 0
	n = 0
	m = 0
	fig, axs = plt.subplots(3, 2, sharex=False, constrained_layout=True)
	fig.suptitle(DataClass.fileName + ' cumulative histogram')
	title = ['fwhm', 'fwhm_x', 'fwhm_y', 'dx', 'dy', 'flux']
	
	for i in range(0,6):
		#print(i)
		#print(m)
		axs[n, m].set_title(title[i])
		axs[n, m].bar(x[i], res[i].cumcount/len(DataClass.fileData[i]), width = res[i].binsize)
		axs[n, m].axhline(0.16, 0, max(DataClass.fileData[i]), color='red')
		axs[n, m].axhline(0.84, 0, max(DataClass.fileData[i]), color='red')
		axs[n, m].axhline(0.50, 0, max(DataClass.fileData[i]), color='red')
		axs[n, m].set_yticks([0.16, 0.50, 0.84])
		axs[n, m].set_xlabel('value')
		axs[n, m].set_ylabel('quant/total')
		n += 1
		if (n == 3):
			n = 0
			m = 1
	figTitle = DataClass.fileName+' cumulative histogram.png'
	print(figTitle)
	plt.savefig('/Users/seri/Desktop/2 - project/dataFiles/128.171.123.254:22281/resultFiles/'+sys.argv[1]+'/'+figTitle)


############################
# function name: dataGraph
# date: 03.4.2021
# update: 03.23.2021
# description: display the data graphs

def dataGraph(DataClass):
	dataName = ['fwhm', 'fwhm_x', 'fwhm_y', 'dx', 'dy', 'flux']
	fig, axs = plt.subplots(3,2, constrained_layout=True)
	fig.suptitle(DataClass.fileName + ' data plots')
	n = 0
	m = 0
	for x in range(0, 6):
		axs[n, m].plot(DataClass.time, DataClass.fileData[x])
		axs[n, m].set_title(dataName[x]+' vs time')
		axs[n, m].set_ylabel(dataName[x])
		axs[n, m].set_xlabel('time')
		n += 1
		if (n == 3):
			n = 0
			m = 1
	figTitle = DataClass.fileName+' data plot.png'
	print(figTitle)
	plt.savefig('/Users/seri/Desktop/2 - project/dataFiles/128.171.123.254:22281/resultFiles/'+sys.argv[1]+'/'+figTitle)




