#####################
# class name: Data
# date: 03.23.2021
# update: 03.29.2021
# description: class initializing/handling data

class Data:

	def __init__(self, fileName, fwhm_data, fwhmX_data, fwhmY_data, centX_data, centY_data, flux_data, instrMag_data):
		self.fileName = fileName
		self.fwhm = fwhm_data
		self.fwhmX = fwhmX_data
		self.fwhmY = fwhmY_data
		self.centX = centX_data
		self.centY = centY_data
		self.flux = flux_data
		self.instrMag = None
		self.percentile16 = []
		self.percentile84 = []
		self.dataMedian = []
		self.gSigma = [0.00]*6
		self.gSigmaCorr = [0.00]*6
		# change to array of pointers. utilize less memory allocation
		self.fileData = [self.fwhm, self.fwhmX, self.fwhmY, self.centX, self.centY, self.flux]

	def __init__(self, direct, num):
		self.fwhm, self.fwhmX, self.fwhmY, self.centX, self.centY, self.flux, self.instrMag, self.time, self.fileName = loadData(direct, num)


	def __init__(self, fileName):
		self.fwhm = None
		self.fwhmX = None
		self.fwhmY = None
		self.centX = None
		self.centY = None
		self.flux = None
		self.instrMag = None
		self.time = None
		self.fileData = [self.fwhm, self.fwhmX, self.fwhmY, self.centX, self.centY, self.flux]

		self.percentile16 = []
		self.percentile84 = []
		self.dataMedian = []
		self.gSigma = []
		self.gSigmaCorr

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

	########################
	# funcion name: setData
	# date: 03.29.2021
	# update: 04.07.2021
	# decsription: sets data, called by loadDataFile

	def setData(self, hdul):
		self.vidLoc = findVideoLoc(hdul)
		self.data = hdul[vidLoc].data
		self.fwhm = data.field('fwhm')
		self.fwhmX = data.field('fwhm_x')
		self.fwhmY = data.field('fwhm_y')
		self.centX = data.field('centroid_x')
		self.centY = data.field('centroid_y')
		self.flux = data.field('flux')
		self.time = data.field('frame_start_time')
		for i in fileData:
			self.dataMedian.append(np.median(fileData[i]))
		self.instrMag = instrumentMag(fluxData)

	########################
	# function name: setDataFolder
	# date: 03.28.2021
	# update: 03.29.2021
	# description: sets data with the full fileName, used when full filename is known (files in a directory)
# unnecessary for current class usage
#	def setDataFolder(self, fileName):
#		hdul = fits.open(fileName)
#		vidLoc = findVideoLoc(hdul)
#		data = hdul[vidLoc].data
#		fwhm = data.field('fwhm')
#		fwhmX = data.field('fwhm_x')
#		fwhmY = data.field('fwhm_y')
#		centX = data.field('centroid_x')
#		centY = data.field('centroid_y')
#		flux = data.field('flux')
#		time = data.field('frame_start_time')
#		instrumentMag(fluxData)
#		hdul.close()

	#######################
	# function name: instrumentMag
	# date: 03.10.2021
	# update: 03.22.2021
	# description: create array of instrumental magnitude
	# np array flux? 	I believe because I use the math.log10 function, im unable to do it this way, but I will try it for the next run											################

	def instrumentMag(flux):
		instr_mag = []
		instr_mag = (-2.5)*(math.log10(flux))
		return instr_mag;


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

	def getPercentile(self,fileData):
		for i in fileData:
			res = stats.cumfreq(fileData[i], numbins = 400)
			self.percentile16.append(findPercentile(res, 0.16))
			self.percentile84.append(findPercentile(res, 0.84))


	###################
	# function name: newArray
	# date: 03.01.2021
	# update: 03.29.2021
	# description: creates an array of the values between percentile 16 and 84 (originally named distribution in statistics.py)

	def newArray(self, dataField, per16, per84):
		newArr = []
		i = 0:
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
		correctedDataArray = newArray(dataField, per16, per84)
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
		for i in self.fileData:
			self.gSigma[i], self.gSigmaCorr[i] = findGSigma(fileData[i], percentile16[i], percentile84[i])
	
