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
#Sock_Dgram is used for UDP. like sock_stream is for TCP
#socket.AF_INET is for Internet like last time
cl_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



def read_text():
    # with this , we have chunk of file.
    offset = 0
    listo = []
    file = location+'\\'+filename
    f = open(file,'rb')
    text = f.read()
    f.close()
    while offset * MSS < len(text):
        offset += 1
        mo = (offset-1) * mss
        mo1 = (offset) * mss
        listo.append(data[mo:mo1])
        return listo


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

def magicThread(data,ser_add):
    t1 = threading.Thread(target=runn, args=(data,ser_add,))

def runn(data,ser_add):
    client_sock.sendto(data, ser_add)


def rdt_send():
    pass

