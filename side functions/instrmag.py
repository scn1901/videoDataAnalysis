import astropy
from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from pylab import *

hdul = fits.open('o9095g0056o.ota35.fits')

data = hdul[65].data
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

plt.figure()
plt.figure()
plt.plot(dt, instr_mag)
plt.xlabel('time')
plt.ylabel('instrumental magnitude')
plt.ylim([-4.0,-11.5])
plt.title('o9095g0056o.ota35 instrumental magnitude vs time')
plt.savefig('o9095g0056o.ota35_instrmag_time.png')