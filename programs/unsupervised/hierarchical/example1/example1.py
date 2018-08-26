#!/usr/bin/python3
# based on the tutorial posted on https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import random
from scipy.spatial.distance import pdist
random.seed(1)


def distance(x1, y1, x2, y2):
    # no need to take square root
    # print (x1 - x2, y1 - y2)
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

if __name__ == "__main__":
    random.seed(1)
    numdp = 6
    x = []
    for i in range(numdp):
        x.append([random.randint(-100, 100),
                  random.randint(-100, 100)])
    print (x)
    Z = linkage(x, 'centroid')
    dendrogram(Z)
    plt.show()

    pairdist = []
    for i1 in range(numdp):
        row = [0] * numdp
        pairdist.append(row)
    for i1 in range(numdp):
        for i2 in range(numdp):
            d = distance(x[i1][0], x[i1][1], x[i2][0], x[i2][1])
            pairdist[i1][i2] = d
        print ('pairdist', pairdist[i1])

    y = x[0:numdp-2]
    y.append([(x[numdp-2][0] + x[numdp-1][0])/2,
              (x[numdp-2][1] + x[numdp-1][1])/2,])
    
    print (y)
    print ('-----------------------------')
    numdp = numdp -1
    pairdist = []
    for i1 in range(numdp):
        row = [0] * numdp
        pairdist.append(row)
    for i1 in range(numdp):
        for i2 in range(numdp):
            d = distance(y[i1][0], y[i1][1], y[i2][0], y[i2][1])
            pairdist[i1][i2] = d
        print ('pairdist', pairdist[i1])
