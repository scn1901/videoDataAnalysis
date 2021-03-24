

###################
# function name: loadData
# date: 03.10.2021
# update: 03.22.2021
# description: load data and save to necessary arrays


def loadData(dir, num): #must be strings
	
	fileName = dir + '.ota' + num + '.fits'
	hdul = fits.open(fileName)
	for x in hdul:
		