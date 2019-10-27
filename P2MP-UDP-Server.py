#a 16-bit field that has the value 1010101010101010, indicating that this is an ACK packet.
ACKmagicno =  int('1010101010101010')
#Read the information from the CMD
import sys
if(len(sys.args)!=3):
    print("Wrong Input")

prob = float(sys.args[-1])
file = sys.args[-2]
port = int(sys.args[-3])

import socket
#https://wiki.python.org/moin/UdpCommunication
cl_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
cl_socket.bind('',port)

def checksum(message,l):
    #l is len of message

    # if l is not even , padding an additional zero
    if (l % 2 != 0):
        message += "0".encode('utf-8')

    x = message[0] + ((message[1]) << 8)
    y = (x & 0xffff) + (x >> 16)

    for i in range(2, len(msg), 2):
        x = message[i] + ((message[i + 1]) << 8)
        y = ((x+y) & 0xffff) + ((x+y) >> 16)
    return ~s & 0xffff

def prob_gen():
    import random as rnd
    return rnd.random(seed=5)


