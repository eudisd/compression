#! /usr/bin/env python

import sys
import struct
import pickle

def main():


    if len(sys.argv) == 1:
        usage()
    elif len(sys.argv) >= 3:
        try:
            i = open(sys.argv[2], "rb")

        except IOError:
            print "Error opening: %s" % sys.argv[2]
            exit(-1)

        if sys.argv[1] == "-c":
            msg = i.read()
            encode(msg)
                
        elif sys.argv[1] == "-d":
            
            decode(sys.argv[2], sys.argv[3])

        else:
            print "\nError: No valid command given! Type: 'python arithmetic.py' for help.\n"
            exit(-1)

        i.close()  
    return

def usage():
    print "\nUsage: arithmetic.py [command] inputfile outputfile"
    print " [Commands] "
    print "    -c: Compress file with arithmetic codec."
    print "    -d: Decompress file. "
    print

    return

def encode(message):
   
    
    return

def decode(infile, outfile):

   
    return



if __name__ == "__main__":
    main()
