#! /usr/bin/env python

import random, time

class Cluster:    
    def __init__(self):
        self.mean = 0
        self.count = 0
        self.error = 0

    
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

def main():

    d = 5
    
    lim = 100
    random.seed(time.time())
    #This is randomly generated
    histogram = list(set([random.randint(0, lim) for i in range(256)]))
    N = len(histogram)
    
    K = N/2

    k = []
    # Soft Sequential K-Means
    c = Cluster()
    c.mean = histogram[0]
    c.count += 1
    k.append(c)
    for i in range(1, N):
        if( len(k) < K ):
            
            min_distance = argmin(k, histogram[i])
            if ( min_distance > d ):
                c = Cluster()
                c.mean = histogram[i]
                c.count += 1
                k.append(c)
            else:
                index = min_index(k, histogram[i])

                # Compute K means
                pass
             
        
    
    
    
    return

if __name__ == "__main__":
    main()



