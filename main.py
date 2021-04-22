import astropy
from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
from pylab import *
import sys
from graphing import cumulativeGraph
from graphing import dataGraph
from Data import ChipData
from initData import collectFileNames
import glob, os, importlib

#cwd = os.getcwd()
pullDirectory = '/Users/seri/Desktop/2 - project/dataFiles/128.171.123.254:22281/psvideo.20210121/'+sys.argv[1]
os.chdir(pullDirectory) #pass in a directory through the arguments in command line

dirNames = []
for name in glob.glob('*.fits'):
	dirNames.append(name)

ChipDataArray = [] #will hold all that have video
fileDirectory = name.split(".")

n = 0
#videoFileNames, videoNum = collectFileNames(sys.argv[1])

for file in dirNames:
	# checking if the file has video file (as established by the collectFileNames function)
	#print(file)
	hdul = fits.open(file)
	if (len(hdul) == 66):
		data = hdul[65].data
		ChipDataArray.append(ChipData(file, data))
		#print(ChipDataArray[n].fileName)
		#print(ChipDataArray[n].percentile16)
		#print(ChipDataArray[n].percentile84)
		cumulativeGraph(ChipDataArray[n])
		dataGraph(ChipDataArray[n])
		hdul.close()
		print('\n')
		n+=1

resultsFile = open(fileDirectory[0]+'.txt', 'a') 
resultsFile.write('#'+fileDirectory[0]+'\n')
for chip in ChipDataArray:
	chip.writeFile(resultsFile)

resultsFile.close()

#show()