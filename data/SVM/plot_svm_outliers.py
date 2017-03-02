#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from sklearn import svm

datafile = 'KeplerSampleWErr.npy'
data = np.load(datafile)
# data shape is (2500, 3, 100)
# (targets, (time, flux, error), epochs)

train = data[:500,1,:]
test = data[500:,1,:]

outliers_fraction = 0.01

n_samples = 500

n_outliers = int(outliers_fraction * n_samples)
ground_truth = np.ones(n_samples, dtype=int)
ground_truth[-n_outliers:] = -1

clf = svm.OneClassSVM(nu=0.95 * outliers_fraction + 0.05,
                                     kernel="rbf", gamma=0.1)

# fit the data and tag outliers
clf.fit(train)
scores_pred = clf.decision_function(test)
y_pred = clf.predict(test)
# n_errors = (y_pred != ground_truth).sum()

# get sorted indices
inds = np.squeeze(scores_pred).argsort()

top = 200

print(scores_pred[inds][:top])
print(inds[:top])

# save results to text file
np.savetxt(datafile.replace('npy', 'txt'),
           np.transpose((500+inds[:top], np.squeeze(scores_pred)[inds][:top])),
           fmt='%d %.4e')

# plot top 25 outliers
f, axarr = plt.subplots(5, 5, figsize=(25,25))
for k,i in enumerate(inds[-25:][::-1]):
    axarr[k//5,k%5].errorbar(data[500+i,0,:], test[i], yerr=data[500+1,2,:], fmt='.')

plt.show()
