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
from graphing import errorBarsInverseSD
from graphing import scaledWithLogFlux
from Data import ChipData
from initData import findVideoLocation
from initData import loadDirectories
import glob, os, importlib

# since each directory for the data was labeled by the first part of the filename, I would use the second argument in commandline to determine directory to work with.
# I had my .py files in different directories, so it was easier for me to type the whole path below.
# if your directories are in the same path, you can use 
#   cwd = os.getcwd() and pullDirectory = cwd+'/'+dirNameArr[x]

dirNameArr = loadDirectories('directories.txt')

CONST_DIR = '/Users/seri/Desktop/2 - project/dataFiles/128.171.123.254:22281/psvideo.20210121/'

# will hold all of the ChipDataArray
DirectoryDataArray = []

for dirName in dirNameArr:
	pullDirectory = CONST_DIR+dirName
	os.chdir(pullDirectory) #pass in a directory through the arguments in command line

	dataFileNames = []
	for name in glob.glob('*.fits'):
		dataFileNames.append(name)


	ChipDataArray = [] #will hold all that have video

	n = 0

	for file in dataFileNames:

		# opens file and collects the header for CELLMODE	
		hdul = fits.open(file)
		cellmode = hdul[0].header['CELLMODE']

		# function to check CELLMODE for video data chips
		videoCellNum, hasVideo = findVideoLocation(cellmode)

		if (hasVideo == True):
			data = hdul[65].data
			ChipDataArray.append(ChipData(file, data))

			# debugging
			print(ChipDataArray[n].fileName)

			# function for creating cumulative graphs
			#cumulativeGraph(ChipDataArray[n])
			# function for creating plots for the data values against time
			dataGraph(ChipDataArray[n], dirName)
			# function for creating singular plot of the locations of the measured bright spots
			#cellArrayGraph(ChipDataArray[n])

			# debugging
			print('\n')

			n+=1
		hdul.close()

	# function for creating plot with average location of the files with error lines
	errorBarsInverseSD(ChipDataArray, dirName)

	#scaledWithLogFlux(ChipDataArray)

	# file that printed average and error
	#resultsFile = open(fileDirectory[0]+'.txt', 'a') 
	#resultsFile.write('#'+fileDirectory[0]+'\n')
	#for chip in ChipDataArray:
	#	chip.writeFile(resultsFile)

	#resultsFile.close()

	DirectoryDataArray.append(ChipDataArray)


#show()