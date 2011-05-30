#! /usr/bin/env python


import sys

def main():

    if len(sys.argv) == 2:
        encode(sys.argv[1])

    else:
        usage()
    return


def usage():
    print "\nUsage: python rle.py [commands] [input file]"
    print "Commands: "
    print "    -h : print help screen/usage info\n"

    return

def encode(filename):
    """ Practical implementation """

    try:
        i = open(filename, "rb")
    except IOError:
        print "Error opening file, exiting..."
        exit(-1)

    text = i.read()
    if(len(text) == 0):
        print "Empty file!"
        exit(-1)
    binary = []

    text_size = len(text)
    for i in text:
        binary.append(str(ord(i)))
    print binary    

    binary_size = len(binary)*8
    binary_str = "".join(reversed(binary))
    binary = int(binary_str)

    # Uncompressed bit sequence
    bit_pos = 0
    while( bit_pos < binary_size):
        print "%d" % ((binary >> bit_pos) & 0x1),
        bit_pos = bit_pos + 1
    

    print "\nCompression...\n"
    bit_pos = 1
    count = 1
    val = binary  & 0x1
    # Print first character out, so we know the alternating sequence
    print "\nBinary: ", binary
    print "Initial Val: ", val
    print "Binary Length: ", binary_size
    print
    while(bit_pos < binary_size):
        if(val == ((binary  >> bit_pos) & 0x1)):
            count = count + 1
            
        else:
            print count,
            count = 1
            val = (binary >> bit_pos) & 0x1
            
        bit_pos = bit_pos + 1
        
    print count
    
   

    return

def concept():
    """ Proof of concept """    
    binary = "010101010110111111100000000000000000000000"
    
    count = 1
    val = binary[0]
    i = 0
    print val # Initial value
    while(i < len(binary)):
        if( val == binary[i] ):
            count = count + 1
        else:
            print count
            count = 1
            val = binary[i]

        i = i + 1

    return 

if __name__ == "__main__":
    main()
