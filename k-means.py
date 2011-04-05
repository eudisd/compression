#! /usr/bin/env python

import random, time

class Cluster:    
    def __init__(self):
        self.mean = 0
        self.count = 0
        self.error = 0
        self.points = []

    
def min_index(K, p):
    """ Returns the index to the cluster with the
    minimum distance"""
    m = 1000
    for i in range(len(K)):
        if ( abs(K[i].mean - p) < m ):
            m = i

    return m
def argmin(K, p):
    """ Returns minimum distance"""
    m = 1000
    for i in range(len(K)):
        if ( abs(K[i].mean - p) < m ):
            m = abs(K[i].mean - p)

    return m
def check_all(k, e):
    """ Checks to see if all errors are below the threshold """
    flag = False
    for i in k:
        if i.error < e:
            flag = True
        else:
            return False

    return flag

def main():

    d = 5
    
    lim = 100
    random.seed(time.time())
    #This is randomly generated
    histogram = list(set([random.randint(0, lim) for i in range(256)]))
    N = len(histogram)
    
    K = N/2
    error = 0.2
    k = []
    # Soft Sequential K-Means
    c = Cluster()
    c.mean = histogram[0]
    c.count += 1
    k.append(c)

    # While there errors in any cluster:
    
    while (check_all(k, error) == True):
        j = 0
        for i in range(1, N):
            if( len(k) < K ):
                
                min_distance = argmin(k, histogram[i])
                if ( min_distance > d ):
                    c = Cluster()
                    c.mean = histogram[i]
                    c.count += 1
                    k.append(c)
                else:
                    # First, search for the index with the argmin index
                    index = min_index(k, histogram[i])
                    # Then, assign this to the cluster in a points array
                    # that stores the list of indexes of points for that 
                    # cluster
                    k[index].points.append(i) 
                    # Compute K means
                    pass
        j += 1
        error -= j
    
    
    
    return

if __name__ == "__main__":
    main()



