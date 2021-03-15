import astropy
from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from pylab import *
from scipy import stats
import pandas as pd

##################
# functino name: calculatedGSigmaHdul
# date: 03.01.2021
# update: 03.01.2021
# description: using equation sigma^2 = sum(x-mean)^2/numOfValues

def calculatedGSigmaHdul(hdul):
	data = hdul[65].data

	arr = ['fwhm', 'fwhm_x', 'fwhm_y', 'centroid_x', 'centroid_y', 'flux']
	gSigmaArr = [0.00]*6
	i = 0
	while (i < 6):
		dataField = data.field(arr[i])
		#print(np.median(dataField)) #this is fine
		gSigmaArr[i] = np.sum(np.power((dataField-np.median(dataField)), 2)/dataField.size)#typically use average
		i += 1
	return gSigmaArr;

##################
# functino name: calculatedGSigmaHList
# date: 03.01.2021
# update: 03.01.2021
# description: using equation sigma^2 = sum(x-mean)^2/numOfValues

def calculatedGSigmaList(correctedList):
	gSigma = 0.00
	#print(np.median(correctedList))
	gSigma = np.sum(np.power((correctedList-np.median(correctedList)), 2)/len(correctedList))#typically use average

	return gSigma;


###################
# function name: distribution
# date: 03.01.2021
# update: 03.01.2021
# description: creates an array of the values between percentile 16 and 84

def distribution(dataField, per16, per84): #numbers at each percentile
	newArr = []
	i = 0
	while (i < dataField.size):
		if(dataField[i] > per16 and dataField[i] < per84):
			newArr.append(dataField[i])
		i += 1
	print('distribution function')
	print(newArr)
	print('next')
	return newArr;



##################
# function name: getGSigma
# date: 03.08.2021
# update: 03.08.2021
# description: save gaussian sigma of all data sets

def getGSigma(hdul, index):
	data = hdul[65].data

	file = pd.read_csv("percentile_array.txt", sep=',')
	# g0223, g0401, g0423 (16, 84), g0056
	fwhmLim = np.asarray(file.fwhm)
	fwhmXLim = np.asarray(file.fwhm_x)
	fwhmYLim = np.asarray(file.fwhm_y)
	centXLim = np.asarray(file.centroid_x)
	centYLim = np.asarray(file.centroid_y)
	fluxLim = np.asarray(file.flux)

	gSigmaArr = [0.00]*6
	gSigmaArr = calculatedGSigmaHdul(hdul)

	fwhm = data.field('fwhm')
	fwhmX = data.field('fwhm_x')
	fwhmY = data.field('fwhm_y')
	centX = data.field('centroid_x')
	centY = data.field('centroid_y')
	flux = data.field('flux')

	i = index*2

	dataCorrected = []
	print(fwhm)
	print(fwhm.size)
	dataCorrected.append(distribution(fwhm, fwhmLim[i], fwhmLim[i+1]))
	dataCorrected.append(distribution(fwhmX, fwhmXLim[i], fwhmXLim[i+1]))
	dataCorrected.append(distribution(fwhmY, fwhmYLim[i], fwhmYLim[i+1]))
	dataCorrected.append(distribution(centX, centXLim[i], centXLim[i+1]))
	dataCorrected.append(distribution(centY, centYLim[i], centYLim[i+1]))
	dataCorrected.append(distribution(flux, fluxLim[i], fluxLim[i+1]))

	correctedGSigmaArr = [0.00]*6

	i = 0
	while(i < 6):
		correctedGSigmaArr[i] = calculatedGSigmaList(dataCorrected[i])
		i += 1

	return gSigmaArr, correctedGSigmaArr;


gSigma0223 = [0.00]*6
correctedGSigma0223 = [0.00]*6
hdul = fits.open('o8646g0223o.ota51.fits')
gSigma0223, correctedGSigma0223 = getGSigma(hdul, 0)
hdul.close()


gSigma0401 = [0.00]*6
correctedGSigma0401 = [0.00]*6
hdul = fits.open('o8645g0401o.ota25.fits')
gSigma0401, correctedGSigma0401 = getGSigma(hdul, 1)
hdul.close()


gSigma0423 = [0.00]*6
correctedGSigma0423 = [0.00]*6
hdul = fits.open('o8646g0423o.ota25.fits')
gSigma0423, correctedGSigma0423 = getGSigma(hdul, 2)
hdul.close()


gSigma0056 = [0.00]*6
correctedGSigma0056 = [0.00]*6
hdul = fits.open('o9095g0056o.ota35.fits')
gSigma0056, correctedGSigma0056 = getGSigma(hdul, 3)
hdul.close()

print(gSigma0223)
print(correctedGSigma0223)
print(gSigma0401)
print(correctedGSigma0401)
print(gSigma0423)
print(correctedGSigma0423)
print(gSigma0056)
print(correctedGSigma0056)