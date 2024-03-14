# Double background subtracing
# The contains of the back corrector:
from astropy.io import fits
import argparse as arg
def parsing args():
parser = arg.ArgumentParser()
parser.add argument(’-c’, ’–coeff’, help=”coefficient”, dest=”coeff”, required = True)
parser.add argument(’-r’, ’–reno’, help=”spaces renormalization”, dest=”renorm”)
parser.add argument(’-s’, ’–clus’, help=”cluster file”, dest=”clus file”)
parser.add argument(’-b’,’–back’, help=”background file”, dest=”back file”)
parser.add argument(’-o’,’–output’,help=”output file”, dest=”out file”)
args = parser.parse args()
return args
15
args = parsing args()
K = float(args.coeff)
R = float(args.renorm)
#open the source (AGN+cluster), surroundings (cluster) and remote background FITS files
hdub = fits.open(back file)
hduc = fits.open(clus file)
bkg data = hdub[1].data
clus data = hduc[1].data
#set the last (wrong) count to 0
bkg data[’COUNTS’][-1] = 0
clus data[’COUNTS’][-1] = 0
#set coefficients
Kmax = len(clus data[’COUNTS’])
#rescaling the data and subtracting the surroundings spectrum from the source spectrum
for i in range(0,Kmax,1):
bkg data[’COUNTS’][i] = clus data[’COUNTS’][i]*K*R + bkg data[’COUNTS’][i]*(1-K)
#write the new FITS files with the rescaled source and remote background counts
hdub.writeto(out file)
