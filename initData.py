

######################
# function name: findVideoLoc
# date: 03.10.2021
# update: 04.08.2021
# description: find the array location for the video using the cellmode

def findVideoLoc(fileName):
	

#######################
# function name: collectFileNames
# date: 04.06.2021
# update: 04.08.2021
# description: splice the file names and 

def collectFileNames(directoryName):
	dirNames = []
	for name in glob.glob('*.cells.txt'):
		dirNames.append(name)
	vidLoc = []
	########Once I am able to access the files, this part should be used to find the string CELLMODE
	file = open(dirNames[0]) #for now, since I'm not sure if there is only one txt file, I shall keep it at 0
	cellmodeString = file.readline()
	while (i < len(cellmodeString)):
		if(cellmodeString[i] == 'V'):
			vidLoc.append(i)
	######## might need to loop for the multiple files, else, loop the function
	return vidLoc;



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


def loadData(direct, num): #must be strings

	fileName = direct + '.ota' + num + '.fits'
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
