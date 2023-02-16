import numpy as np
#!pip install astropy
#!pip install fitsio
from scipy import stats
from scipy.stats import norm
import fitsio
import glob
import os
import sys
import matplotlib.pyplot as plt
import statistics
import argparse
import astropy
from astropy.table import Table,join
from astropy.time import Time
from astropy.io import fits

import LSS.common_tools as common


parser = argparse.ArgumentParser()

basedir='/global/cfs/cdirs/desi/survey/catalogs'
parser.add_argument("--tracer", help="tracer type to be selected",default='all')
parser.add_argument("--basedir", help="base directory for input/output",default=basedir)
parser.add_argument("--survey", help="e.g., main (for all), DA02, any future DA",default='Y1')
parser.add_argument("--verspec",help="version for redshifts",default='iron')
parser.add_argument("--catver",help="version for redshifts",default='test')
parser.add_argument("--mkfiles",help="whether or not to make the files",default='y')
#parser.add_argument("--tracer",help="tracer type (e.g., LRG)",default='LRG')

args = parser.parse_args()
basedir = args.basedir
survey  = args.survey
specver = args.verspec
#tp = args.tracer



#ff = fitsio.read(filepathLF)
#hdul = fits.open(filepathLF)
#ff2 = fitsio.read(filepathBGS)
#hdul = fits.open(filepathBGS)

if args.tracer == 'all':
    tracers = ['QSO','LRG','ELG_LOPnotqso','BGS_ANY']
else:
    tracers = [args.tracer]

if args.mkfiles == 'y':
    for tp in tracers:
     
        zf = basedir+'/'+survey+'/LSS/'+specver+'/LSScats/'+args.catver+'/'+tp+'_full_noveto.dat.fits'
        dz = Table(fitsio.read(zf))
        z_tot = dz['ZWARN'] != 999999
        z_tot &= dz['ZWARN']*0 == 0
        z_tot &= dz['GOODHARDLOC'] == 1
        if tp[:3] != 'BGS':
            z_tot &= dz['TSNR2_ELG'] > 80
        z_suc = common.goodz_infull(tp,dz,zcol='Z')

        #print(len(ff[z_suc]),len(ff[z_tot]))
        print("zsuccess rate for "+tp,len(dz[z_suc&z_tot])/len(dz[z_tot]))
        fibl,n_tot = np.unique(dz[z_tot]['FIBER'],return_counts=True)
        fiblg,n_g = np.unique(dz[z_suc&z_tot]['FIBER'],return_counts=True)
        fib_test = np.isin(fibl,fiblg)
        z_tot &= np.isin(dz['FIBER'],fibl[fib_test])
        fibl,n_tot = np.unique(dz[z_tot]['FIBER'],return_counts=True)

        if np.array_equal(fibl,fiblg):
            gfrac = n_g/n_tot
        else:
            sys.exit('need to put something in for mismatch fiber lists')
        modl = []
        for fib in fibl:
            sel = dz['FIBER'] == fib
            nmod = np.sum(dz[sel&z_tot]['mod_success_rate'])
            modl.append(nmod)
            print(fib)
        fn = basedir+'/'+survey+'/LSS/'+specver+"/"+tp+'_zsuccess_fromfull.txt'
        fo = open(fn,'w')
        for ii in range(len(fibl)):
            fo.write(str(fibl[ii])+' '+str(n_g[ii]/n_tot[ii])+' '+str(n_g[ii])+' '+str(n_tot[ii])+' '+str(modl[ii])+'\n')
        fo.close()
 
