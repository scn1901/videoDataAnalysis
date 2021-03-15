import astropy
from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from pylab import *

hdul = fits.open('o9095g0056o.ota35.fits')

data = hdul[65].data
fwhm = data.field('fwhm')
fwhm_x = data.field('fwhm_x')
fwhm_y = data.field('fwhm_y')
cent_x = data.field('centroid_x')
cent_y = data.field('centroid_y')
flux = data.field('flux')

instr_mag = [0.000, 0.000]
instr_mag[0] = (-2.5)*(math.log10(flux[0]))
instr_mag[1] = (-2.5)*(math.log10(flux[1]))
i = 2
while (i < len(flux)):
    instr_mag.append((-2.5)*(math.log10(flux[i])))
    i += 1

time = data.field('frame_start_time')
dt = time-time[0]

print('fwhm median ')
print(np.median(fwhm))
print('fwhm_x median ')
print(np.median(fwhm_x))
print('fwhm_y median ')
print(np.median(fwhm_y))
print('cent_x median ')
print(np.median(cent_x))
print('cent_y median ')
print(np.median(cent_y))
print('flux median ')
print(np.median(flux))
print('instrumental magnitude median ')
print(np.median(instr_mag))