import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
import sys


#change this constant to your directory that will have the result files
CONST_DIR = '/Users/seri/Desktop/2 - project/dataFiles/128.171.123.254:22281/resultFiles'

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

	# for each savefig function, i created a new directory ex. 'histogram' in this function.
	# if you do not want to use separate directories, please delete the 'histogram/' part of each savefig
	# note: must create ALL directories before hand
	plt.savefig(CONST_DIR+'/'+dirName+'/'+'histogram/'+figTitle)


############################
# function name: dataGraph
# date: 03.4.2021
# update: 03.23.2021
# description: display the data graphs

def dataGraph(DataClass, dirName):
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
	plt.savefig(CONST_DIR+'/'+dirName+'/'+'data plot/'+figTitle)


############################
# function name: cellArrayGraph
# date: 04.22.2021
# update: 04.28.2021
# description: with the x and y axes being dx and dy and the plotted points being error bars

def cellArrayGraph(DataClass,dirName):
	fig, ax = plt.subplots()
	fig.suptitle('dx dy location plots')
	ax.scatter(DataClass.dx, DataClass.dy, marker=".", alpha=0.1)
	ax.set_xlabel('dx')
	ax.set_ylabel('dy')
	temp = DataClass.fileName.split(".")
	name = temp[1]
	plt.savefig(CONST_DIR+'/'+dirName + '/'+'dx dy/'+ name + '_dxdy_location_plots.png')


############################
# function name: errorBarsInverseSD
# date: 04.29.2021
# update: 05.01.2021
# decsription: plotting the average of each video cell bright star and error bars are plotted as the inverse standard deviation 
#	this is a graph of the location and the error

def errorBarsInverseSD(DataClassArr, dirName):
	medianXArr = []
	medianYArr = []
	errorXArr = []
	errorYArr = []
	label = []

	for DataClass in DataClassArr:
		medianXArr.append(DataClass.dataMedian[3])
		medianYArr.append(DataClass.dataMedian[4])
		errorXArr.append(1/(DataClass.gSigma[3]))
		errorYArr.append(1/(DataClass.gSigma[4]))
		temp = DataClass.fileName.split(".")
		label.append(temp[1])

	fig, ax = plt.subplots()
	fig.suptitle('average location on the cells')
	# error bars are too small to see with 100 by 100
	#ax.set_xlim(0,100)
	#ax.set_ylim(0,100)
	ax.set_xlabel('dx')
	ax.set_ylabel('dy')
	ax.errorbar(medianXArr, medianYArr, xerr=errorXArr, yerr=errorYArr, marker=".", linestyle="None", ecolor="red")

	# the following for loop labels each point
	#i = 0
	#for name in label:
	#	plt.annotate(name, (medianXArr[i], medianYArr[i]), textcoords="offset points", xytext=(0,10), ha='center')
	#	i += 1

	plt.savefig(CONST_DIR +'/'+ dirName + '/'+'average/' + dirName + '_average_xy_Error_cellLabel.png')


#############################
# function name: scaledWithLogFlux
# date: 04.29.2021
# update: 05.02.2021
# description: plotting the locations with size respect to 

def scaledWithLogFlux(DataClassArr,dirName):
	medianXArr = []
	medianYArr = []
	fluxArr = []
	label = []

	for DataClass in DataClassArr:
		medianXArr.append(DataClass.dataMedian[3])
		medianYArr.append(DataClass.dataMedian[4])
		fluxArr.append((np.log10(DataClass.dataMedian[5]))*10)
		temp = DataClass.fileName.split(".")
		label.append(temp[1])

	print(fluxArr)
	fig, ax = plt.subplots()
	fig.suptitle('location on cells with flux')
	ax.set_xlabel('dx')
	ax.set_ylabel('dy')
	ax.scatter(medianXArr, medianYArr, s=fluxArr)

	plt.savefig(CONST_DIR+'/'+dirName+ '/'+'average/' + dirName + '_average_xy_logflux.png')


