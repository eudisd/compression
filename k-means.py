#! /usr/bin/env python

import time, random, math

def main():

    point_range = 100
    n = 100

    K = []
    d = 0
    P = []


    random.seed(time.time())
    # Generate Random Points
    for i in range(n):
        P.append(random.randint(0, point_range))


    # Randomly chose K means ( len(K) < n )
    for i in range(random.randint(0, n - 1)):
        K.append(P[i])

    print "P", P
    print
    print "K", K

    for i in P:
        for j in K:
            Min = point_range
            if ( abs( i - j ) < Min ):
               Min = abs( i - j )

    return

if __name__ == "__main__":
    main()




