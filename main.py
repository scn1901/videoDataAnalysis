import astropy
from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from pylab import *
from scipy import stats
import sys
import initData
import graphing

fwhm, fwhmX, fwhmY, centX, centY, flux, instrMag, time, fileName = initData.loadData(argv[0], argv[1])
data = [fwhm, fwhmX, fwhmY, centX, centY, flux]
graphing.cumulativeGraph(fwhm,fwhmX,fwhmY,centX,centY,flux,fileName)
graphing.dataGraph(fwhm, fwhmX, fwhmY, centX, centY, flux, instrMag, time, fileName)