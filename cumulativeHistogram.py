import astropy
from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from pylab import *
from scipy import stats

####################
# function name: retrieveData
# date: n/a
# update: 02.28.2021
# description: initialize data for diagrams

def retrieveData(fileName):
	hdul = fits.open(fileName)

	data = hdul[65].data
	fwhm = data.field('fwhm')
	fwhmX = data.field('fwhm_x')
	fwhmY = data.field('fwhm_y')
	centX = data.field('centroid_x')
	centY = data.field('centroid_y')
	flux = data.field('flux')

	instrMag = [0.000, 0.000]
	instrMag[0] = (-2.5)*(math.log10(flux[0]))
	instrMag[1] = (-2.5)*(math.log10(flux[1]))
	i = 2
	while (i < len(flux)):
	    instrMag.append((-2.5)*(math.log10(flux[i])))
	    i += 1

	time = data.field('frame_start_time')
	dt = time-time[0]

	hdul.close()

	return fwhm, fwhmX, fwhmY, centX, centY, flux, instrMag;


######################
# function name: cumulativeGraph
# date: n/a
# update: 02.28.2021
# description: display cumulative graph

def cumulativeGraph(fileName, dataName, data, xSearchValue, percent, binNum):
	title = fileName + ' ' + dataName + ' cumulative histogram'
	res = stats.cumfreq(data, numbins=binNum)
	x = res.lowerlimit + np.linspace(0, res.binsize*res.cumcount.size, res.cumcount.size)

	fig, ax = plt.subplots()
	ax.set_title(title)
	ax.bar(x, res.cumcount/len(data), width = res.binsize)
	#plt.xlim(xSearchValue - 0.5, xSearchValue + 0.5)
	#plt.ylim(percent-0.05, percent + 0.05)
	plt.grid()
	show()


# o8646g0223o.ota51 cumulative histogram plots
#
#

file = 'o8646g0223o.ota51'
fileName = file + '.fits'
fwhm, fwhmX, fwhmY, centX, centY, flux, instrMag = retrieveData(fileName)
cumulativeGraph(file, 'fwhm', fwhm, 0.979, 0.16, 150)


show()

