#! /usr/bin/env python

import sys
import struct
import pickle

# Frequency Table ( f : symbol -> prob, low, high )

freq = {}
for i in range(256):    
    freq[chr(i)] = [0.0, 0.0, 0.0]    


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
    
    if( len(sys.argv) >= 4 ):
        o = open(sys.argv[3], "wb")
    
    print "Message: ", message
    # Calculate frequencies First
    for i in range(256):
        for j in message:
            if j == chr(i):
                freq[j][0] = freq[j][0] + 1
    
    # Get Total Amount of Relevant Chars
    total = 0.0
    for i in range(256):
        if ( freq[chr(i)][0] != 0 ):
            total = total + 1.0
    
    high = 0
    low = 0

    # Calculate the high and low values of the table
    for i in range(256):
        if ( freq[chr(i)][0] != 0 ):
            high = low + freq[chr(i)][0]/total
            freq[chr(i)][1] = low
            freq[chr(i)][2] = high
            low = high
            
    
    # Use a smaller table  
    freqs = {}
    for i in range(256):
        if ( freq[chr(i)][0] != 0 ):
            freqs[chr(i)] = freq[chr(i)]
            print "Symbol: %c -- Prob: %f -- Low: %f -- High: %f" % (chr(i), freqs[chr(i)][0], freqs[chr(i)][1], freqs[chr(i)][2])
    
    Range = high - low
    low = 0.0
    high = 1.0

    print "\nEncoding"
    for i in message:
        Range = high - low
        high = low + Range * freqs[i][2]
        low = low + Range * freqs[i][1]
        print "Symbol: %c -- Range: %f -- Low: %f -- High: %f" % (i, Range, low, high)
        
    #First, we write the size of the string out, so we have a stopping case
    # during decompression. 'h' is for short, so we use only two bytes to hold the filesize

    o.write( struct.pack('h', total) )

    #Then, we write out the frequency table

    serial = pickle.Pickler(o, pickle.HIGHEST_PROTOCOL)
    serial.dump(freqs)
    
    #Finally, we write out the actual value encoded in 'f' (4 bytes)
    o.write(struct.pack('f', low)) 

    o.close()
    

    return

def decode(infile, outfile):
        
    

    try:
        inf = open(infile, "rb")
    except IOError:
        print "Error opening file for decoding, exiting..."
        exit(-1)

    out = open(outfile, "wb")

    total = struct.unpack('h', inf.read(2))[0]

    freqs = pickle.load(inf)

    encoded_value = struct.unpack('f', inf.read(4))[0]

    print "Total: ", total
    print "Encoded Value: ", encoded_value
    

    print "Decoding"

    data = ''
    symbol = ''
    
    size = total
    count = 0

    while count < size:
        # Get the symbol that has the encoded value withing it's range
        for k, v in freqs.iteritems():
            if ( encoded_value < v[2] and encoded_value >= v[1] ):
                symbol = k
                data = data + symbol

        Range = freqs[symbol][2] - freqs[symbol][1]
        encoded_value = (encoded_value - freqs[symbol][1]) / Range
        print "Encoded: ", encoded_value
        count += 1 


    out.write(data)
    out.close()
    
   
    return



if __name__ == "__main__":
    main()
