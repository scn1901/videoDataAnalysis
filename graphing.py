
##########################
# function name: cumulativeGraph
# date: 03.10.2021
# update: 03.22.2021
# description: display cumulative graph in a grid


def cumulativeGraph(fwhm, fwhmX, fwhmY, centX, centY, flux, fileName):
	
	data = [fwhm, fwhmX, fwhmY, centX, centY, flux]
	res = []
	x = []
	i = 0
	for i in data:
		res.append(stats.cumfreq(fwhm, numbins=400))
		x.append(res[i].lowerlimit + np.linspace(0, res[i].binsize*res[i].cumcount.size, res[i].cumcount.size))

	i = 0
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




