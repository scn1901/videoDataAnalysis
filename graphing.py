import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats

##########################
# function name: cumulativeGraph
# date: 03.10.2021
# update: 03.22.2021
# description: display cumulative graph in a grid

np.seterr(divide='ignore', invalid='ignore')

def cumulativeGraph(DataClass):
	
	data = [DataClass.fwhm, DataClass.fwhmX, DataClass.fwhmY, DataClass.centX, DataClass.centY, DataClass.flux]
	res = []
	x = []
	i = 0
	for i in range(0,len(data)):
		res.append(stats.cumfreq(DataClass.fwhm, numbins=400))
		x.append(res[i].lowerlimit + np.linspace(0, res[i].binsize*res[i].cumcount.size, res[i].cumcount.size))

	n = 0
	i = 0
	m = 0
	fig, axs = plt.subplots(3, 2)
	fig.suptitle(DataClass.fileName + ' cumulative history')
	title = ['fwhm', 'fwhm_x', 'fwhm_y', 'centroid_x', 'centroid_y', 'flux']
	data = [DataClass.fwhm, DataClass.fwhmX, DataClass.fwhmY, DataClass.centX, DataClass.centY, DataClass.flux]
	
	for n in range(0,6):
		#print(i)
		#print(m)
		axs[i, m].set_title(title[n])
		axs[i, m].bar(x[n], res[n].cumcount/len(data[n]), width = res[n].binsize)
		plt.hlines(0.16, min(x[n]), max(x[n]))
		plt.hlines(0.84, min(x[n]), max(x[n]))
		plt.grid()
		i += 1
		if (i == 3):
			i = 0
			m = 1
	figTitle = DataClass.fileName+'.png'
	print(figTitle)
	plt.savefig(figTitle)


############################
# function name: dataGraph
# date: 03.4.2021
# update: 03.23.2021
# description: display the data graphs

def dataGraph(DataClass):
	dataName = ['fwhm', 'fwhm_x', 'fwhm_y', 'centroid_x', 'centroid_y', 'flux']
	fig, axs = plt.subplots(3,2)
	fig.suptitle(DataClass.fileName + ' data plots')
	n = 0
	m = 0
	for x in range(0, 6):
		axs[n, m].plot(DataClass.time, DataClass.fileData[x])
		axs[n, m].set_xlabel(dataName[x])
		axs[n, m].set_ylabel('time')
		plt.grid()
		n += 1
		if (n == 3):
			n = 0
			m = 1
	figTitle = DataClass.fileName+'.png'
	plt.savefig(figTitle)




