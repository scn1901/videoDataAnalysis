import astropy
from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from pylab import *

def countValues(arrName):
    arrCount = [0]
    arrVal = [0.00]
    arrCount[0] = arrCount[0] + 1
    arrVal[0] = arrName[0]
    i = 0
    #print(len(arrName))
    #print(len(arrVal))
    #print(len(arrCount))
    while (i < len(arrName)):
    	i += 1
    	n = 0
    	numerated = 0
    	while (n < len(arrVal)):
    		if (numerated == 1):
    			break

    		elif(arrName[i] == arrVal[n]):
    			arrCount[n] += 1
    			numerated = 1
    			break
    		n += 1

    	if (numerated == 0):
    		
    while (i < len(arrName)):
    	i = i + 1
    	n = 0
    	numerated = 0
    	#print(i)
    	#print(len(arrVal))
    	#print(len(arrCount))
    	while (n < len(arrVal)):
    		if (numerated == 1):
    			break
            elif (arrName[i] == arrVal[n]):
                arrCount[n] = arrCount[n] + 1
                numerated = 1
                break
            n = n + 1

		if(numerated == 0):
			arrCount.append(1)
            arrVal.append(arrName[i])
            #print(arrVal[n])
        
    return arrVal, arrCount

hdul = fits.open('o9095g0056o.ota35.fits')

data = hdul[65].data
fwhm = data.field('fwhm')
fwhm_x = data.field('fwhm_x')
fwhm_y = data.field('fwhm_y')
cent_x = data.field('centroid_x')
cent_y = data.field('centroid_y')
flux = data.field('flux')
#snr = data.field('snr')
fwhmHistVal, fwhmHistCount = countValues(fwhm)
fwhmXHistVal, fwhmXHistCount = countValues(fwhm_x)
fwhmYHistVal, fwhmYHistCount = countValues(fwhm_y)
centXHistVal, centXHistCount = countValues(cent_x)
centYHistVal, centYHistCount = countValues(cent_y)
fluxHistVal, fluxHistCount = countValues(flux)

instr_mag = [0.000, 0.000]
instr_mag[0] = (-2.5)*(math.log10(flux[0]))
instr_mag[1] = (-2.5)*(math.log10(flux[1]))
i = 2
while (i < len(flux)):
    instr_mag.append((-2.5)*(math.log10(flux[i])))
    i = i + 1

instrMagHistVal, instrMagHistCount = countValues(instr_mag)

time = data.field('frame_start_time')
dt = time-time[0]

#fwhm vs time
plt.figure()
plt.bar(fwhmHistVal, fwhmHistCount)
plt.xlabel('fwhm')
plt.ylabel('count')
plt.title('o9095g0056o.ota35 fwhm histogram')
plt.savefig('o9095g0056o.ota35_fwhm_histogram.png')

#fwhm x vs time
plt.figure()
plt.bar(fwhmXHistVal, fwhmXHistCount)
plt.xlabel('fwhm x')
plt.ylabel('count')
plt.title('o9095g0056o.ota35 fwhm_x histogram')
plt.savefig('o9095g0056o.ota35_fwhm_x_histogram.png')

#fwhm y vs time
plt.figure()
plt.bar(fwhmYHistVal, fwhmYHistCount)
plt.xlabel('fwhm y')
plt.ylabel('count')
plt.title('o9095g0056o.ota35 fwhm_y histogram')
plt.savefig('o9095g0056o.ota35_fwhm_y_histogram.png')

#centroid x vs time
plt.figure()
plt.bar(centXHistVal, centXHistCount)
plt.xlabel('centroid x')
plt.ylabel('count')
plt.title('o9095g0056o.ota35 cent_x histogram')
plt.savefig('o9095g0056o.ota35_centroid_x_histogram.png')

#centroid y vs time
plt.figure()
plt.bar(centYHistVal, centYHistCount)
plt.xlabel('centroid y')
plt.ylabel('count')
plt.title('o9095g0056o.ota35 cent_y histogram')
plt.savefig('o9095g0056o.ota35_centroid_y_histogram.png')

#flux vs time
plt.figure()
plt.bar(fluxHistVal, fluxHistCount)
plt.xlabel('flux')
plt.ylabel('count')
plt.title('o9095g0056o.ota35 flux histogram')
plt.savefig('o9095g0056o.ota35_flux_histogram.png')

#snr vs time
#plt.plot(dt, snr)
#plt.xlabel('time')
#plt.ylabel('snr')
#plt.title('o8645g0401o.ota25 snr vs time'
#plt.savefig(ota25_snr_time)

#instrumental magnitude
#print(len(dt))
#print(len(instr_mag))
plt.figure()
plt.bar(instrMagHistVal, instrMagHistCount)
plt.xlabel('instrumental magnitude')
plt.ylabel('count')
plt.title('o9095g0056o.ota35 instrumental magnitude histogram')
plt.savefig('o9095g0056o.ota35_instrmag_histogram.png')

#flux xy
#plt.figure()
#plt.scatter(cent_x,cent_y,c=flux)
#plt.xlabel('centroid_x')
#plt.ylabel('centroid_y')
#plt.title('o8646g0223o.ota51 flux axis')
#plt.colorbar()
#plt.grid(True)
#plt.savefig('o8646g0223o.ota51_centroid_flux_color.png')


#xlim([0.5,2.0])
#ylim([26.0,12.0])


show()
