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

resultsFile = open(fileDirectory[0]+'.txt', 'a') 

n = 0
videoFileNames, videoNum = collectFileNames(sys.argv[1])
for file in dirNames:

	# checking if the file has video file (as established by the collectFileNames function)
	if(file == videoFileNames[n]):
		hdul = fits.open(file)

		data = hdul[videoNum[n]].data
		ChipDataArray.append(ChipData(file, data))
		ChipDataArray[x].writeFile(resultsFile)
		cumulativeGraph(ChipDataArray[n])
		dataGraph(ChipDataArray[n])
		n+=1

#show()