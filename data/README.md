the original errorbars were very large
## use these files:

**KeplerSampleWErrSparse.npy**	sparse array with corrected errorbars

**KeplerSampleWErr.npy** dense array with corrected errorbars

these are numpy arrays: download and load the local file as numpy.load("file name"). The resulting object is a 2500,3,100 numpy.ndarray for the KeplerSampleWErr.npy and 2500,3,50 for the KeplerSampleWErrSparse.npy. Notice that the Sparse array is not only subsampled (50% of the point) but the times are randomely picked, so the sampling is irregular in time.

These are median devided Kepler lcvs 

**kepSparselcvs.csv**	and **kepDenselcvs.csv**	are the corresponding csv files with 4 columns: time, flux, error, index, where index is a dummy index for the star target. 

**gaialcvs.csv**	is a dataset of gaia targets, which contains ~3000 objects, sparsely and irregularly sampled and with lightcurves of different lengths. The data-file structure is the same


# missing: HR_Weirdness.npy

# missing : Kepler_Spike_Removal_Full_LCs.npy