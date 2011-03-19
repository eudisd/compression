#! /usr/bin/env python

import sys

dic2 = "a,b,c,d,e,f,g,i,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9"
dic2 = dic2.split(",")

dic = {}
for i in range(len(dic2)):
    dic[dic2[i]] = i





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
            msg = i.read()
            decode(msg)

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
    global dic
    if len(sys.argv) >= 5:
        try:
            o = open(sys.argv[4], "wb")
        except IOError:
            print "Error opening file %s for writing." % sys.argv[4]
            exit(-1)
    
    word = message[0]
    for i in range(1,len(message)):
        char = message[i]
        if find(dic, word+char) == True:
            word = word + char
        else:
            
            dic[word+char] = dic.values()[len(dic.keys()) - 1] + str(1)
            word = char
    
    
        
    
    print dic
    return

def find(L, t):
    try:
        L.index(t) 
        return True
    except:
        return False

def decode(message):

    return


if __name__ == "__main__":
    main()



