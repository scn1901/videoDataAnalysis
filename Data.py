from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math

#####################
# class name: Data
# date: 03.23.2021
# update: 03.29.2021
# description: class initializing/handling data

class ChipData:

	def __init__(self):
		self.fileName = None
		self.fwhm = None
		self.fwhmX = None
		self.fwhmY = None
		self.centX = None
		self.centY = None
		self.flux = None
		self.instrMag = None
		self.time = None
		self.percentile16 = None
		self.percentile84 = None
		self.dataMedian = [0.00]*6
		self.gSigma = [0.00]*6
		self.gSigmaCorr = [0.00]*6
		# change to array of pointers. utilize less memory allocation
		self.fileData = [self.fwhm, self.fwhmX, self.fwhmY, self.centX, self.centY, self.flux]

	def __init__(self, fileName, hdul):
		self.fwhm = None
		self.fwhmX = None
		self.fwhmY = None
		self.centX = None
		self.centY = None
		self.flux = None
		self.instrMag = None
		self.time = None
		self.fileData = [self.fwhm, self.fwhmX, self.fwhmY, self.centX, self.centY, self.flux]
		self.percentile16 = [0.00]*6
		self.percentile84 = [0.00]*6
		self.dataMedian = [0.00]*6
		self.gSigma = [0.00]*6
		self.gSigmaCorr = [0.00]*6
		self.setData(hdul)
		self.fileName = fileName

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
	# decsription: sets data, called by loadDataFile

	def setData(self, hdul):
		vidLoc = self.findVideoLoc(hdul)
		data = hdul[65].data
		self.fwhm = (data.field('fwhm'))
		self.fwhmX = (data.field('fwhm_x'))
		self.fwhmY = (data.field('fwhm_y'))
		self.centX = (data.field('centroid_x'))
		self.centY = (data.field('centroid_y'))
		self.flux = (data.field('flux'))
		self.time = (data.field('frame_start_time'))
		for i in range(0,len(self.fileData)):
			self.dataMedian[i] = (np.median(self.fileData))
		self.instrMag[i] = (self.instrumentMag())
		self.getPercentile()
		self.getGSigma()

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
			instr_mag[i] = (-2.5)*(math.log10(self.flux[i]))
			i += 1
		self.instrMag = instr_mag

	#################
	# function name: findPercentile
	# date: 03.29.2021
	# update: 03.29.2021
	# description: function finding the value at a certain percentile

	def findPercentile(self, res, percentile):
		i = 0
		percent = 0.0
		before, after = 0.00
		while (percent < percentile):
			percent = res.cumcount[i]/dataSize
			i += 1
		if (percent > percentile and i == 0):
			before = 0
			after = res.binsize
		if (percent > percentile):
			before = res.binsize*(i-1)
			after = res.binsize*i
		if (percent == percentile):
			before = res.binsize
			after = res.binsize
		percentileValue = (before + after)/2
		return percentileValue;
		

	##################
	# function name: getPercentile
	# date: 03.29.2021
	# update: 03.29.2021
	# description: collecting the percentile data and saving it to the Class

	def getPercentile(self):
		for i in self.fileData:
			res = stats.cumfreq(self.fileData[i], numbins = 400)
			self.percentile16.append(self.findPercentile(res, 0.16))
			self.percentile84.append(self.findPercentile(res, 0.84))


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
		correctedDataArray = self.newArray(dataField, per16, per84)
		gSigmaUncorrected = np.sum(np.power(dataField-np.median(dataField), 2)/dataField.size)
		gSigmaCorrected = np.sum(np.power((correctedDataArray-np.median(correctedDataArray)), 2)/len(correctedDataArray))
		return gSigmaUncorrected, gSigmaCorrected;


	####################
	# function name: getGSigma
	# date: 03.29.2021
	# update: 03.29.2021
	# description: collect and set gaussian sigma of all files

	def getGSigma(self):
		i = 0
		for i in fileData:
			self.gSigma[i], self.gSigmaCorr[i] = self.findGSigma(fileData[i], percentile16[i], percentile84[i])
	
