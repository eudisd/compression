#! /usr/bin/env python

import random, time

class Cluster:    
    def __init__(self):
        self.mean = 1.0
        self.count = 1.0
        self.error = 1.0

def min_index(K, p):
    """ Returns the index to the cluster with the
    minimum distance"""
    #find max element first
    M = 0
    m_ = 0
    for i in range(len(K)):
        if ( K[i].mean > M ):
           m_ = i
           M = K[i].mean

    # Now we find Min
    m = m_

    for i in range(len(K)):
        if ( abs(K[i].mean - p) < K[m].mean ):
            m = i


    return m
def argmin(K, p):
    """ Returns minimum distance"""
    #find max element first
    M = 0
    m_ = 0
    for i in range(len(K)):
        if ( K[i].mean > M ):
           m_ = i
           M = K[i].mean

    # Now we find Min
    m = m_
    for i in range(len(K)):
        if ( abs(K[i].mean - p) < K[m].mean ):
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
    RANGE = 5

    random.seed(time.time())

    #This is randomly generated
    histogram = list(set([random.randint(0, lim) for i in range(RANGE)]))
    N = len(histogram)

    K = N/2
    clusters = []
    # Create K-Means
    for i in range(K):
        c = Cluster()
        # k-mean should not be zero, this next line handles that.
        c.mean = histogram[random.randint(1, N - 1)] if (histogram[random.randint(1, N - 1)] != 0) else histogram[random.randint(1, N - 1)]
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
           
    # Recalculate K size
    K = len(clusters)

    print "\nData Points: ",
    for i in histogram:
        print i,
    print

    print "\nMean Points: ",
    for i in range(len(clusters)):
        print clusters[i].mean,
    print "\n\n"


    # We make a limited amout of passes.  3 should give us > 90% refinement

    count = 0
    limiter = 3 # 3 gives good convergence
    while(count < limiter ):
                print "Pass # ", count + 1
                
                # SEQUENTIAL K-MEANS.  Calculate new mean on the fly.
                for i in histogram:
                    m =  min_index(clusters, i)
                    print "\nPoint: %d - Argmin Mean: %f -  Belongs to Cluster: %d - Total K-Points: %d" % (i, clusters[m].mean, m, clusters[m].count)
                    clusters[m].count += 1
                    clusters[m].mean += i
                    clusters[m].mean /= clusters[m].count
                    print "New Mean Mean: ", clusters[m].mean

                    #Reset Counters
                for i in range(len(clusters)):
                    clusters[i].count = 1.0

                count += 1

                print "\n\n"
    print "New Cluster Information: ", len(clusters)

    for i in range(len(clusters)):
        print "Cluster: ", i
        print "New Cluster Mean: ", clusters[i].mean
        print "New Cluster Error: ", clusters[i].error

        print
        


if __name__ == "__main__":
    main()

