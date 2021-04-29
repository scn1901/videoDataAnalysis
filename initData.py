import sys
import glob

######################
# function name: findVideoLocation
# date: 03.10.2021
# update: 04.08.2021
# description: find the array location for an individual video file using the cellmode

def findVideoLocation(cellmode):
	videoNum = 0
	hasVideo = False
	for i in range(0, len(cellmode)):
		if(cellmode[i] == 'V'):
			hasVideo = True
			videoNum = i
	return videoNum, hasVideo;


######################
# function name: findVideoLoc
# date: 03.10.2021
# update: 04.08.2021
# description: find the array location for the video using the cellmode

def findVideoLoc(dataFileNames, videoLocation):
	videoNum = []
	videoName = []
	hasVideo = False
	n = 0
	for dataString in videoLocation:
		for i in range(0, len(dataString)):
			if (dataString[i]=='V'):
				videoNum.append(int(i)+1)
				hasVideo = True
		if (hasVideo == True):
			temp = dataFileNames[n].split('/')
			videoName.append(temp[1])
		n += 1
		hasVideo = False
	return videoName, videoNum;

#######################
# function name: collectFileNames
# date: 04.06.2021
# update: 04.08.2021
# description: splice the file names and 

def collectFileNames(directoryName):
	for name in glob.glob('*.cells.txt'):
		dirName = name
		#there should be only one cells.txt
	dataFileNames = []
	videoLocation = []

	with open(dirName) as file:
		for line in file:
			temp = line.split("  ")
			dataFileNames.append(temp[0])
			videoLocation.append(temp[1])

	#print(dataFileNames)
	#print(videoLocation)

	videoFileNames, videoNum = findVideoLoc(dataFileNames, videoLocation)

	return videoFileNames, videoNum;



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
