import sys
import threading

#Read the information from the CMD
if(len(sys.args)<4):
    print("Wrong Input")
MSS = int(sys.args[-1])
filename = sys.args[-2]
portno = int(sys.args[-3])
server_list =  list()
for i in range(1, len(sys.args)-3):
    server_list.append(sys.argv[i])
#a 16-bit field that has the value 0101010101010101, indicating that this is a data packet.
magicno =  int('0101010101010101')
#where data will be stoted
#location =
#a 32-bit sequence number, which starts at 0
seqno = 0
# 32 bit header(Randomly selected one)
header = 32
# The Stop-and-
# Wait protocol buffers the data it receives from rdt send() until it has at least one MSS worth of bytes.
buffer_period = MSS + header
# Time when the process started
import datetime as dt
#utcnow is is 117 times faster than now
start_time = dt.datetime.utcnow()

import socket
cl_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def read_text():
    file = location+'\\'+filename
    f = open(file,'rb')
    text = f.read()
    f.close()
    return text

def checksum(message,l):
    #l is len of message

    # if l is not even , padding an additional zero
    if (l % 2 != 0):
        message += "0".encode('utf-8')

    w = message[0] + ((message[1]) << 8)
    s = (w & 0xffff) + (w >> 16)

    for i in range(2, len(msg), 2):
        w = message[i] + ((message[i + 1]) << 8)
        s = ((w+s) & 0xffff) + ((w+s) >> 16)
    return ~s & 0xffff

def rdt_send():
    pass
