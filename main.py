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
from graphing import cellArrayGraph
from Data import ChipData
from initData import findVideoLocation
import glob, os, importlib

# since each directory for the data was labeled by the first part of the filename, I would use the second argument in commandline to determine directory to work with.
# I had my .py files in different directories, so it was easier for me to type the whole path below.
# if your directories are in the same path, you can use 
#   cwd = os.getcwd() and pullDirectory = cwd+'/'+sys.argv[1]
pullDirectory = '/Users/seri/Desktop/2 - project/dataFiles/128.171.123.254:22281/psvideo.20210121/'+sys.argv[1]
os.chdir(pullDirectory) #pass in a directory through the arguments in command line

dirNames = []
for name in glob.glob('*.fits'):
	dirNames.append(name)

ChipDataArray = [] #will hold all that have video
fileDirectory = name.split(".")

n = 0

for file in dirNames:
	# checking if the file has video file (as established by the collectFileNames function)
	
	hdul = fits.open(file)
	cellmode = hdul[0].header['CELLMODE']
	videoCellNum, hasVideo = findVideoLocation(cellmode)
	if (hasVideo == True):
		data = hdul[65].data
		ChipDataArray.append(ChipData(file, data))
		print(ChipDataArray[n].fileName)
		print(ChipDataArray[n].percentile16)
		print(ChipDataArray[n].percentile84)
		cumulativeGraph(ChipDataArray[n])
		dataGraph(ChipDataArray[n])
		cellArrayGraph(ChipDataArray[n])
		print('\n')
		n+=1
	hdul.close()

resultsFile = open(fileDirectory[0]+'.txt', 'a') 
resultsFile.write('#'+fileDirectory[0]+'\n')
for chip in ChipDataArray:
	chip.writeFile(resultsFile)

resultsFile.close()

#show()