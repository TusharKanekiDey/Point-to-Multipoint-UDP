import sys
import os
import random as rnd


#a 16-bit field that has the value 1010101010101010, indicating that this is an ACK packet.
ACKmagicno =  '1010101010101010'
#Read the information from the CMD

if(len(sys.args)!=3):
    print("Wrong Input")

prob = float(sys.args[3])
file = sys.args[2]
port = int(sys.args[1])
buff_size = 2048
seqno = 0

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

def sequence_generator():
    if seqno == int ((2**32)-1):
        seqno = 0
    else:
        seqno+=1

def prob_gen():
    return rnd.random(seed=5)

fname = file+'.txt'
f = open(fname,'w')

data_recvd, add = cl_socket.recvfrom(buff_size)
#get the sequence number from the data_recd
seq_recvd = int(data_recvd[0:32],2)
checksum_recvd = int(data_recvd[32:48],2)
payload_recvd = data_recvd[64:]

#calculate checksum in server side of the payload_recvd
checker = checksum(payload_recvd,len(payload_recvd))

#random number
r_got = prob_gen()

if r_got <= prob or seq_recvd != seqno:
    print('Timeout, sequence number = ',seqno)

else:
    if seq_recvd == seqno and checksum_recvd == checker:
        f.write(payload_recvd.decode('utf-8'))
        send_ack = '{:032b}'.format(int(seqno))
        data = send_ack.encode('utf-8')+ ACKmagicno.encode('utf-8')
        cl_socket.sendto(data,add)

sequence_generator()
f.close()
print('Done')





