######################
# function name: findVideoLoc
# date: 03.10.2021
# update: 03.22.2021
# description: find the array location for the video

def findVideoLoc(hdul):
	res = 0
	for x in hdul:
		if (isinstance(hdul[x], TableHDU)):
			res = x
	return res;


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

	return instr_mag;



###################
# function name: loadData
# date: 03.10.2021
# update: 03.22.2021
# description: load data and save to necessary arrays


def loadData(dir, num): #must be strings

	fileName = dir + '.ota' + num + '.fits'
	hdul = fits.open(fileName)
	vidLoc = findVideoLoc(hdul)
	data = hdul[vidLoc].data
	fwhmData = data.field('fwhm')
	fwhmXData = data.field('fwhm_x')
	fwhmYData = data.field('fwhm_y')
	centXData = data.field('centroid_x')
	centYData = data.field('centroid_y')
	fluxData = data.field('flux')
	timeData = data.field('frame_start_time')
	instrMagData = instrumentMag(fluxData)
	hdul.close()

	return fwhmData, fwhmXData, fwhmYData, centXData, centYData, fluxData, instrMagData, timeData, fileName;
