import numpy as np
import pylab as pl

def sporadicSampling(N, indata, square=False):
    '''Created a sporadically sampled subset of the original Mx3 data cube
    Input: 
    N: (int) minimum number of points per lightcurve
    square: (bool) if True each object in the dataset will have exactly N observations. if False N is an upper limit to the number of observations

    '''
    # set for reproducibility
    np.random.seed(123)

    #index of arrays created as uniform sampling of the indeces of each object
    subSampled = (np.random.rand(indata.shape[0], N) * ind[0][0][0]).astype(int)
    subSampled.sort(axis=1)
    
    #identify duplicate indeces
    duplicates = np.diff(subSampled, axis=1) == 0
    #replace duplicate indeces if the array has to be square (exactly N observations per row)
    # otherwise just drop duplicates
    if square:
        while duplicates.sum() > 0:
            subSampled[:,1:][duplicates] += 1
            duplicates = np.diff(subSampled, axis=1) == 0
        
    return [subSampled[i][a] for i,a in
     enumerate(np.concatenate([np.atleast_2d(
         np.array([True]*duplicates.shape[0])).T, ~duplicates], axis=1))]

if __name__ == '__main__':
    #testing on 5 objects from KeplerSampleFullQ.npy
    ind = np.load("../data/KeplerSampleFullQ.npy")[:5]
    ind = np.array(([i[j] for i in ind
                      for j in range(3)])).reshape(ind.shape[0],3,
                                                   len(i[0]))
    ax = pl.figure().add_subplot(111)
    i=0
    pl.plot(ind[i][0], ind[i][1])
    pl.show()
    

    for i,a in enumerate(sporadicSampling(10, ind, square=True)):
        print (ind[i][:,a].shape)        
        ax.errorbar(ind[i][0,a], ind[i][1,a], yerr=ind[i][2,a])

    ax.set_xlabel("time")
    ax.set_ylabel("flux")
    pl.show()
    
