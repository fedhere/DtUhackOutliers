# DtUhackOutliers

## Goals
Using a set of sparse light curves and a set of densely-sampled light curves, apply different outlier detection methods and compare their performance (possibly in a framework for voting on "weirdness"). 

After we generate a list of outliers, we hope to have astronomer "citizen scientists" examine the resulting outliers to see if they understand why these objects were found to be outliers. 

## Algorithms to test

1. Unsupervised random forest
2. Conditional entropy (Rényi entropy)
3. Persistent homology
4. Isolation tree 

## Data

We wanted to use both densely- and sparsely-sampled light curves. 

Proposed dataset: Kepler lcvs (dense), Kepler lcvs (sparse), Gaia lcvs (sparse and different number of points) 

To download the data, go to the data directory, click on the .npy files, and click download on the upper right in the file preview. 
