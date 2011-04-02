#! /usr/bin/env python

import sys
import struct
import pickle

dic2 = []
for i in range(255):
    dic2.append(chr(i))

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
            print "werd"
        else:

            data.append( dic[word] )
            dic[word+char] = sorted(dic.values())[len(dic.values()) - 1] + 1
            word = char


    #First, we write out the header (first 2 bytes is the length of the
    #dictionary, the rest is the dictionary, then followed by the codes.
    write_dic(o, dic)

    for i in data:
        # Here I write out the code for the characters
        o.write( struct.pack('h', i) )
        
    o.close()
    
    return

def find(dic, key):
    for k, v in dic.iteritems():
        if k == key:
            return True
    return False


def decode(infile, outfile):

    try:
        i = open(infile, "rb")
    except IOError:
        print "Error reading encoded file, exiting..."
        exit(-1)

    o = open(outfile, "wb")

    
    dic = pickle.load(i)

    

    data = i.read();


    w = struct.unpack_from('h', data[0:2] )
    
    text = lookup(w[0], dic)

    for I in range(2, len(data) - 2, 2):
        w = struct.unpack('h', data[I:I+2])
        text = text + lookup(w[0], dic)

    o.write(text)
    i.close()
    o.close()
    
    
    return

def write_dic(o, dic):
    """
    writes the dictionary to output stream.
    Must be part of the LZW encoding scheme.
    """
    serial = pickle.Pickler(o, pickle.HIGHEST_PROTOCOL)
    serial.dump(dic)
    return

def lookup(value, dic):
    for k, v in dic.iteritems():
        if value == v:
            return k
    return ''

def print_dic(dic):
    for k, v in dic.iteritems():
        if( v > 32 and v < 127):
            print "Key: ", k, " Value: ", v



if __name__ == "__main__":
    main()




