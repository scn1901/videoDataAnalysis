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

print(dirNames)
print(pullDirectory)

ChipDataArray = [] #will hold all that have video

fileDirectory = name.split(".")

print(fileDirectory)

n = 0
videoFileNames, videoNum = collectFileNames(sys.argv[1])

#pullDirectory = '/Users/seri/Desktop/2 - project/dataFiles/128.171.123.254:22281/resultFiles/'+sys.argv[1]
#os.chdir(pullDirectory)
for file in dirNames:
	# checking if the file has video file (as established by the collectFileNames function)
	#print(file)
	if file in videoFileNames:
		print(file)
		print(videoNum[n])
		hdul = fits.open(file)

		data = hdul[65].data
		ChipDataArray.append(ChipData(file, data))
		ChipDataArray[n].writeFile(resultsFile)
		cumulativeGraph(ChipDataArray[n])
		dataGraph(ChipDataArray[n])
		hdul.close()
		n+=1

resultsFile = open(fileDirectory[0]+'.txt', 'a') 
resultsFile.write('#'+fileDirectory[0]+'\n')
for chip in ChipDataArray:
	chip.writeFile(checkResFile)

resultsFile.close()

#show()