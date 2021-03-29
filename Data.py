#####################
# class name: Data
# date: 03.23.2021
# update: 03.29.2021
# description: class initializing/handling data

class Data:

	def __init__(self, fwhm_data, fwhmX_data, fwhmY_data, centX_data, centY_data, flux_data, instrMag_data):
		self.fwhm = fwhm_data
		self.fwhmX = fwhmX_data
		self.fwhmY = fwhmY_data
		self.centX = centX_data
		self.centY = centY_data
		self.flux = flux_data
		self.instrMag = instrMag_data
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

		self.percentile16 = None
		self.percentile84 = None

		self.fileName = fileName

	########################
	# function name: setDataSingle
	# date: 03.28.2021
	# update: 03.29.2021
	# description: sets data by finding the file name, single filename usage

	def setDataSingle(direct, num):
		fileName = direct + '.ota' + num + '.fits'
		hdul = fits.open(fileName)
		vidLoc = findVideoLoc(hdul)
		data = hdul[vidLoc].data
		self.fwhm = data.field('fwhm')
		self.fwhmX = data.field('fwhm_x')
		self.fwhmY = data.field('fwhm_y')
		self.centX = data.field('centroid_x')
		self.centY = data.field('centroid_y')
		self.flux = data.field('flux')
		self.time = data.field('frame_start_time')
		instrumentMag(fluxData)
		hdul.close()

	########################
	# function name: setDataFolder
	# date: 03.28.2021
	# update: 03.29.2021
	# description: sets data with the full fileName, used when full filename is known (files in a directory)

	def setDataFolder(fileName):
		hdul = fits.open(fileName)
		vidLoc = findVideoLoc(hdul)
		data = hdul[vidLoc].data
		self.fwhm = data.field('fwhm')
		self.fwhmX = data.field('fwhm_x')
		self.fwhmY = data.field('fwhm_y')
		self.centX = data.field('centroid_x')
		self.centY = data.field('centroid_y')
		self.flux = data.field('flux')
		self.time = data.field('frame_start_time')
		instrumentMag(fluxData)
		hdul.close()

	#######################
	# function name: instrumentMag
	# date: 03.10.2021
	# update: 03.22.2021
	# description: create array of instrumental magnitude

	def instrumentMag(flux):
		instr_mag = [0.0000]*len(flux)
		i = 0
		while(i < len(flux)):
			instr_mag[i] = (-2.5)*(math.log10(flux[0]))
			i += 1
		self.instrMag = instr_mag


	#################
	# function name: findPercentile
	# date: 03.29.2021
	# update: 03.29.2021
	# description: function finding the value at a certain percentile

	def findPercentile(res, percentile):
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

	def getPercentile(self, fileData):
		for i in fileData:
			res = stats.cumfreq(fileData[i], numbins = 400)
			self.percentile16 = findPercentile(res, 0.16)
			self.percentile84 = findPercentile(res, 0.84)




