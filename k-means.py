#! /usr/bin/env python

import random, time

class Cluster:    
    def __init__(self):
        self.mean = 0.0
        self.count = 0.0
        self.error = 0.0

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

    print error
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
    RANGE = 10

    random.seed(time.time())

    #This is randomly generated
    histogram = list(set([random.randint(0, lim) for i in range(RANGE)]))
    N = len(histogram)

    K = N/2
    clusters = []
    # Create K-Means
    for i in range(K):
        c = Cluster()
        c.mean = histogram[random.randint(0, N - 1)]
        c.error = 0
        clusters.append(c)

    # Remove duplicates from clusters

    i, j = 0, 0
    while( i < len(clusters) ):
           j = i + 1
           while ( j < len(clusters) ):
                 if( clusters[i].mean == clusters[j].mean ):
                     del clusters[j]
                 j += 1
                 
           i += 1





    print "\nData Points: ",
    for i in histogram:
        print i,
    print



    print "\nMean Points: ",
    for i in clusters:
        print i.mean,
    print


    # We make a limited amout of passes.  3 should give us > 90% refinement
    

    count = 0
    limiter = 1 # 3 is good enough to get a good convergence
    while(count < limiter):
                for i in histogram:
                    m =  min_index(clusters, i)
                    #print "Point: %d  -  Belongs to Cluster: %d" % (i, m)
                    clusters[m].count += 1
                    print clusters[m].mean
                    clusters[m].mean += i
                    clusters[m].mean /= clusters[m].count

                count += 1


    
    return

if __name__ == "__main__":
    main()



