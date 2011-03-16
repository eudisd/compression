#! /usr/bin/env python

import sys

dictionary = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,
                  'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,
                  's':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,
                  '0':26,'1':27,'2':28,'3':39,'4':40,'5':41,'6':42,'7':43,
                  '8':44,'9':45}

def main():

    

    if len(sys.argv) == 1:
        usage()
    elif len(sys.argv) >= 3:
        if sys.argv[1] == "-c":
            encode(sys.argv[2])
        elif sys.argv[1] == "-d":
            decode(sys.argv[2])
        else:
            print "\nError: No valid command given! Type: python lzw.py for help.\n"
            exit(-1)
            
    return

def usage():
    print "\nUsage: lzw.py [command] inputfile outputfile"
    print " [Commands] "
    print "    -c: Compress file with lzw."
    print "    -d: Decompress file. "
    print

    return

def encode(message):
    global dictionary
    print dictionary
    return

def decode(message):

    return

if __name__ == "__main__":
    main()



