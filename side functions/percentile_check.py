import astropy
from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from pylab import *
from scipy import stats

##################
# function name: cumulative_hist_val_at_percent
# date: 02.25.2021
# update date: 02.28.2021
# description: finds the 16th pecentile and 84 percentile of data
#				using these two values to find the gaussian sigma

def cumulative_hist_val_at_percent(hdul, dataField):
#fits.HDUList, string 
	data = hdul[65].data
	dataVal = data.field(dataField)

	percent_value = 0.00
	binNum = 50
	repeat = 0
	while(repeat == 0):
		res = stats.cumfreq(dataVal, numbins=binNum)
		percentage = 0.00
		i = 0
		while(round(percentage, 2) < 0.16):
			percentage = res.cumcount[i]/dataVal.size
			if (round(percentage, 2) == 0.16):
				percent_value = res.binsize*i
				percentile16 = [percent_value, res.binsize, i, binNum]   
				#print(percent_value)
#				print(dataVal.size)
#				print(i)
#				i += 1
				repeat = 1
			i += 1
		
		if (binNum == 10000):
			i = 0
			percentage = 0.00
			while (percentage < 0.16):
				percentage = res.cumcount[i]/dataVal.size
				i += 1
			percent_value = res.binsize*i
			percentile16 = [percent_value, res.binsize, i, binNum]
			repeat = 1

		#print(binNum)
		binNum += 1
		
	percent_value = 0.00
	binNum = 50
	while(repeat == 1):
		res = stats.cumfreq(dataVal, numbins=binNum)
		percentage = 0.00
		i = 0
		while(round(percentage, 2) < 0.84):
			percentage = res.cumcount[i]/dataVal.size
			if (round(percentage, 2) == 0.84):
				percent_value = res.binsize*i
				percentile84 = [percent_value, res.binsize, i, binNum]
				repeat = 0
				#print(percent_value)
			i += 1

		if (binNum == 10000):
			i = 0
			percentage = 0.00
			while (percentage < 0.84):
				percentage = res.cumcount[i]/dataVal.size
				i += 1
			percent_value = res.binsize*i
			percentile84 = [percent_value, res.binsize, i, binNum]
			repeat = 0

		binNum += 1
	return percentile16, percentile84;


################
# function name: writeArray
# date: 02.25.2021
# update: 02.28.2021
# description: write array to file 

def writeArray(fileName, arr, numSize, arrSize): #arrSize = number of columns, numSize is 1 unless 2D array or more
	file = open(fileName, 'a') #'a': append to the end of file 'w': rewrites whole file
	n = 0
	while(n < arrSize):
		i = 0
		while(i < numSize):
			print(arr[n][i])
			file.write(str(arr[n][i]))
			file.write(', ')
			i += 1
		file.write('\n')
		n += 1
	file.write('\n')
	file.close()

# o8646g0223o.ota51 percentile data
#
#
hdul = fits.open('o8646g0223o.ota51.fits')

arr = ['fwhm', 'fwhm_x', 'fwhm_y', 'centroid_x', 'centroid_y', 'flux']
o8646g0223o_per16 = [0.00]*6
o8646g0223o_per84 = [0.00]*6
#arrays store the value, bin number, total bin numbers
#o8646g0223o_16, o8646g0223o_84 = cumulative_hist_val_at_percent(hdul, arr[1])
i = 0 #no 2 or 4
while (i < 6):
	o8646g0223o_per16[i], o8646g0223o_per84[i] = cumulative_hist_val_at_percent(hdul, arr[i])
	i += 1

hdul.close()


file = 'newBinFile.txt'
writeArray(file, o8646g0223o_per16, 4, 6)
writeArray(file, o8646g0223o_per84, 4, 6)

print(o8646g0223o_per16)
print(o8646g0223o_per84)



# o8645g0401o.ota25 percentile data
#
#
hdul = fits.open('o8645g0401o.ota25.fits')

o8645g0401o_per16 = [0.00]*6
o8645g0401o_per84 = [0.00]*6
#arrays store the value, bin number, total bin numbers
i = 0 #second part of 4
while (i < 6):
	o8645g0401o_per16[i], o8645g0401o_per84[i] = cumulative_hist_val_at_percent(hdul, arr[i])
	i += 1

hdul.close()

writeArray(file, o8645g0401o_per16, 4, 6)
writeArray(file, o8645g0401o_per84, 4, 6)

print(o8645g0401o_per16)
print(o8645g0401o_per84)



# o8646g0423o.ota25 percentile data
#
#
hdul = fits.open('o8646g0423o.ota25.fits')

o8646g0423o_per16 = [0.00]*6
o8646g0423o_per84 = [0.00]*6
#arrays store the value, bin number, total bin numbers
i = 0
while (i < 6):
	o8646g0423o_per16[i], o8646g0423o_per84[i] = cumulative_hist_val_at_percent(hdul, arr[i])
	i += 1

hdul.close()

writeArray(file, o8646g0423o_per16, 4, 6)
writeArray(file, o8646g0423o_per84, 4, 6)

print(o8646g0423o_per16)
print(o8646g0423o_per84)




# o8646g0423o.ota25 percentile data
#
#
hdul = fits.open('o9095g0056o.ota35.fits')

o9095g0056o_per16 = [0.00]*6
o9095g0056o_per84 = [0.00]*6
#arrays store the value, bin number, total bin numbers
i = 0
while (i < 6):
	o9095g0056o_per16[i], o9095g0056o_per84[i] = cumulative_hist_val_at_percent(hdul, arr[i])
	i += 1

hdul.close()

writeArray(file, o9095g0056o_per16, 4, 6)
writeArray(file, o9095g0056o_per84, 4, 6)

print(o9095g0056o_per16)
print(o9095g0056o_per84)


show()

