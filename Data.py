from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from math import log10
from scipy import stats

#####################
# class name: Data
# date: 03.23.2021
# update: 03.29.2021
# description: class initializing/handling data

class ChipData:

	#def __init__(self):
		# change to array of pointers. utilize less memory allocation
	def __init__(self, fileName, data):
		self.fileName = fileName
		self.setData(data)
		print('created ChipData class')

	########################
	# function name: setDataSingle
	# date: 03.28.2021
	# update: 04.07.2021
	# description: sets data by finding the file name, single filename usage

	def setDataSingle(self, direct, num):
		self.fileName = direct + '.ota' + num + '.fits'
		hdul = fits.open(fileName)
		
		hdul.close()

	######################
	# function name: findVideoLoc
	# date: 03.10.2021
	# update: 03.22.2021
	# description: find the array location for the video

	def findVideoLoc(self,hdul):
		res = 0
		for x in hdul:
			if (isinstance(hdul[x], fits.fitsrec.FITS_rec)):
				res = x
		return res;

	########################
	# funcion name: setData
	# date: 03.29.2021
	# update: 04.07.2021
	# decsription: hdul will be utilized outside of function and setData will only handle the data.

	def setData(self, data):
		self.fwhm = (data.field('fwhm'))
		self.fwhmX = (data.field('fwhm_x'))
		self.fwhmY = (data.field('fwhm_y'))
		self.centX = (data.field('centroid_x'))
		self.centY = (data.field('centroid_y'))
		self.dx = (data.field('centroid_x'))-(data.field('cnpix1'))
		self.dy = (data.field('centroid_y'))-(data.field('cnpix2'))
		self.flux = (data.field('flux'))
		self.time = (data.field('frame_start_time'))
		self.fileData = [self.fwhm, self.fwhmX, self.fwhmY, self.dx, self.dy, self.flux]
		self.dataMedian = [0.00]*6
		for i in range(0,len(self.fileData)):
			self.dataMedian[i] = (np.median(self.fileData[i])) ## double check with the cumulative histogram 0.5
		self.instrMag[i] = (self.instrumentMag())
		self.getPercentile()
		self.getGSigma()
		print('set data')

	#######################
	# function name: instrumentMag
	# date: 03.10.2021
	# update: 03.22.2021
	# description: create array of instrumental magnitude
	# I believe because I use the math.log10 function, im unable to do it this way, but I will try it for the next run											################

	def instrumentMag(self):
		instr_mag = [0.00]*len(self.flux)
		i = 0
		while(i < len(self.flux)):
			instr_mag[i] = (-2.5)*(np.log10(self.flux[i]))
			i += 1
		self.instrMag = instr_mag

	#################
	# function name: findPercentile
	# date: 03.29.2021
	# update: 03.29.2021
	# description: function finding the value at a certain percentile

	def findPercentile(self, res, percentile, dataSize):
		i = 0
		percent = 0.0
		before= 0.00
		after = 0.00
		while (percent < percentile):
			percent = res.cumcount[i]/dataSize
			i += 1
		if (percent > percentile and i == 1):
			before = 0
			after = res.binsize
		if (percent > percentile):
			before = res.binsize*(i-1)
			after = res.binsize*i
		if (percent == percentile):
			before = res.binsize*i
			after = res.binsize*i
		percentileValue = (before + after)/2
		return percentileValue;
		

	##################
	# function name: getPercentile
	# date: 03.29.2021
	# update: 03.29.2021
	# description: collecting the percentile data and saving it to the Class

	def getPercentile(self):
		self.percentile16 = []
		self.percentile84 = []
		for i in range(0,6):
			res = stats.cumfreq(self.fileData[i], numbins = 400)
			self.percentile16.append(self.findPercentile(res, 0.16, len(self.fileData[i])))
			self.percentile84.append(self.findPercentile(res, 0.84, len(self.fileData[i])))


	###################
	# function name: newArray
	# date: 03.01.2021
	# update: 03.29.2021
	# description: creates an array of the values between percentile 16 and 84 (originally named distribution in statistics.py)

	def newArray(self, dataField, per16, per84):
		newArr = []
		i = 0
		while (i < dataField.size):
			if(dataField[i] > per16 and dataField[i] < per84):
				newArr.append(dataField[i])
			i += 1
		return newArr;

	###################
	# function name: findGSigma
	# date: 03.29.2021
	# update: 03.29.2021
	# description: function finding the gaussian sigma of a data set

	def findGSigma(self, dataField, per16, per84): 
		gSigma = (per84-per16)/2.0
		return gSigma;


	####################
	# function name: getGSigma
	# date: 03.29.2021
	# update: 03.29.2021
	# description: collect and set gaussian sigma of all files

	def getGSigma(self):
		i = 0
		self.gSigma = [0.00]*6
		for i in range(0,6):
			self.gSigma[i] = self.findGSigma(self.fileData[i], self.percentile16[i], self.percentile84[i])
	
	#####################
	# function name: writeFile
	# date: 04.08.2021
	# update: 04.08.2021
	# description: take in a file to print out all values

	def writeFile(self, file): #add input opened file # file, one line per chip 
		file.write(self.fileName+",") # commented title
		for i in range(0,6):
			file.write('%.3f' % self.dataMedian[i])
			file.write(',')
			file.write('%.6f' % self.gSigma[i])
			if (i != 5):
				file.write(',')
		file.write('\n')
