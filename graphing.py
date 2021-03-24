
##########################
# function name: cumulativeGraph
# date: 03.10.2021
# update: 03.22.2021
# description: display cumulative graph in a grid


def cumulativeGraph(fwhm, fwhmX, fwhmY, centX, centY, flux, fileName):
	
	res[0] = stats.cumfreq(fwhm, numbins=400)
	res[1] = stats.cumfreq(fwhmX, numbins=400)
	res[2] = stats.cumfreq(fwhmY, numbins=400)
	res[3] = stats.cumfreq(centX, numbins=400)
	res[4] = stats.cumfreq(centY, numbins=400)
	res[5] = stats.cumfreq(flux, numbins=400)
	x[0] = res[0].lowerlimit + np.linspace(0, res[0].binsize*res[0].cumcount.size, res[0].cumcount.size)
	x[1] = res[1].lowerlimit + np.linspace(0, res[1].binsize*res[1].cumcount.size, res[1].cumcount.size)
	x[2] = res[2].lowerlimit + np.linspace(0, res[2].binsize*res[2].cumcount.size, res[2].cumcount.size)
	x[3] = res[3].lowerlimit + np.linspace(0, res[3].binsize*res[3].cumcount.size, res[3].cumcount.size)
	x[4] = res[4].lowerlimit + np.linspace(0, res[4].binsize*res[4].cumcount.size, res[4].cumcount.size)
	x[5] = res[5].lowerlimit + np.linspace(0, res[5].binsize*res[5].cumcount.size, res[5].cumcount.size)

	fig, axs = plt.subplots(2, 3, i+1)
	fig.suptitle(fileName + ' cumulative history')
	title = ['fwhm', 'fwhm_x', 'fwhm_y', 'centroid_x', 'centroid_y', 'flux']
	data = [fwhm, fwhmX, fwhmY, centX, centY, flux]
	for i in axs:
		axs[i].set_title(title[i])
		axs[i].bar(x[i], res[i].cumcount/len(data[i]), width = res[i].binsize)
		plt.yline(0.16)
		plt.yline(0.84)
		plt.grid()

	show()


############################
# function name: dataGraph
# date: 03.4.2021
# update: 03.23.2021
# description: display the data graphs

def dataGraph(fwhm, fwhmX, fwhmY, centX, centY, flux, instrMag, time, fileName):
	data = [fwhm, fwhmX, fwhmY, centX, centY, flux, instrMag]
	dataName = ['fwhm', 'fwhm_x', 'fwhm_y', 'centroid_x', 'centroid_y', 'flux', 'instrument magnitude']
	fig, axs = plt.subplots(2,4)
	fig.suptitle(fileName + ' data plots')
	for x in data:
		axs[x].plot(time, data[x])
		axs[x].set_xlabel(dataName[x])
		axs[x].set_ylabel('time')




