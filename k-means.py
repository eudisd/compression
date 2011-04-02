#! /usr/bin/env python

import random

class Cluster:    
    def __init__(self):
        self.mean = 0
        self.count = 0
        self.error = 0

    

def main():

    d = 10
    
    lim = 100

    #This is randomly generated
    histogram = list(set([random.randint(0, lim) for i in range(256)]))
    N = len(histogram)
    
    # Chose k random clusters
    clusters = list(set([ histogram[ random.randint(0, lim) % N ] for i in range( histogram[ random.randint(0, N) ]) ]))
    K = len(clusters)
    

    # Soft Sequential K-Means
    
    

    
    print histogram 
    print clusters
    
    return

if __name__ == "__main__":
    main()



