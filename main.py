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

#fwhm, fwhmX, fwhmY, centX, centY, flux, instrMag, time, fileName = initData.loadData(argv[0], argv[1])
#data = [fwhm, fwhmX, fwhmY, centX, centY, flux]
#graphing.cumulativeGraph(fwhm,fwhmX,fwhmY,centX,centY,flux,fileName)
#graphing.dataGraph(fwhm, fwhmX, fwhmY, centX, centY, flux, instrMag, time, fileName)

cwd = os.getcwd()
os.chdir(cwd+'/dataFiles')

#importlib.import_module()

dirNames = []
for name in glob.glob('*.fits'):
	dirNames.append(name)

print(dirNames)
ChipDataArray = []
x = 0

for file in dirNames:
	print('in File loop')
	fileDirectory = file.split("/")
	hdul = fits.open(fileDirectory[-1])

	# for now, vidLoc is 65
	vidLoc = 65

	data = hdul[vidLoc].data
	ChipDataArray.append(ChipData(file,data))
	cumulativeGraph(ChipDataArray[x])
	dataGraph(ChipDataArray[x])
	x+=1

#show()