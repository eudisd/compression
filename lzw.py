#! /usr/bin/env python

import sys
import struct
import pickle

dic2 = " ,a,b,c,d,e,f,g,i,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9"
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
            
            decode(sys.argv[2], sys.argv[3])

        else:
            print "\nError: No valid command given! Type: python lzw.py for help.\n"
            exit(-1)

        i.close()  
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
    o = open(sys.argv[3], "wb")

    data = []
    
    
    word = message[0]
    for i in range(1,len(message)):
        char = message[i]
        if find(dic, word+char) == True:
            word = word + char
        else:
            
            data.append( dic[word] )
            dic[word+char] = sorted(dic.values())[len(dic.values()) - 1] + 1
            word = char


    #First, we write out the header (first 2 bytes is the length of the
    #dictionary, the rest is the dictionary, then followed by the codes.
    write_dic(o, dic)

    for i in data:
        # Here I write out the code for the characters
        o.write( struct.pack('b', i) )
        
    o.close()
    
    return

def find(L, t):
    try:
        L.index(t) 
        return True
    except:
        return False

def decode(infile, outfile):

    try:
        i = open(infile, "rb")
    except IOError:
        print "Error reading encoded file, exiting..."
        exit(-1)

    o = open(outfile, "wb")

    #dic_len = struct.unpack('h', i.read(2) )
    dic = pickle.load(i)

    

    print dic
    
    i.close()
    o.close()
    
    
    return

def write_dic(o, dic):
    """
    writes the dictionary to output stream.
    Must be part of the LZW encoding scheme.
    """

    #write out length first (two byte short gives ~64k range)
    #dic_len = len(dic.values())

    
    #o.write( struct.pack('h', dic_len) )
    serial = pickle.Pickler(o, pickle.HIGHEST_PROTOCOL)
    serial.dump(dic)
    return

if __name__ == "__main__":
    main()



