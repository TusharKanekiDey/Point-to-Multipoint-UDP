import sys
import threading
import datetime as dt
import socket

# Read the information from the CMD
if (len(sys.argv) < 4):
    print("Wrong Input")
MSS = int(sys.argv[-1])
filename = sys.argv[-2]
portno = int(sys.argv[-3])
server_list = list()
for i in range(1, len(sys.argv) - 3):
    server_list.append(sys.argv[i])

# a 16-bit field that has the value 0101010101010101, indicating that this is a data packet.
d_packet = '0101010101010101'
d_packet_last = '1101010101010101'

# where data will be stoted
import os
farg = sys.argv[0]
location = os.path.dirname(farg)

# a 32-bit sequence number, which starts at 0
seqno = 0

# 32 bit header(Randomly selected one)
# header = 32
# The Stop-and-
# Wait protocol buffers the data it receives from rdt send() until it has at least one MSS worth of bytes.
# buffer_period = MSS + header
# Time when the process started

# utcnow is is 117 times faster than now
start_time = dt.datetime.utcnow()

# Sock_Dgram is used for UDP. like sock_stream is for TCP
# socket.AF_INET is for Internet like last time
cl_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def read_text(MSS):
    # with this , we have chunk of file.
    offset = 0
    listo = []
    file = location  + filename
    f = open(file, 'rb')
    text = f.read()
    f.close()
    while offset * MSS < len(text):
        offset += 1
        mo = (offset - 1) * MSS
        mo1 = (offset) * MSS
        listo.append(text[mo:mo1])
    return listo


def checksum(message, l):
    # l is len of message
    # if l is not even , padding an additional zero
    if (l % 2 != 0):
        message += "0".encode('utf-8')

    x = message[0] + ((message[1]) << 8)
    y = (x & 0xffff) + (x >> 16)


    for i in range(2, len(message), 2):
        x = message[i] + ((message[i + 1]) << 8)
        y = ((x + y) & 0xffff) + ((x + y) >> 16)
    return ~y & 0xffff


def magicThread(data, ser_add):
    t1 = threading.Thread(target=runn, args=(data, ser_add,))
    t1.start()


def runn(data, ser_add):
    cl_socket.sendto(data, ser_add)


def rdt_send(data_seg, ack_list):
    t_thread = []

    for ip in ack_list:
        ser_add = (ip, portno)
        magicThread(data_seg, ser_add)

    ack_count = 0
    finish_list = len(ack_list)
    ack_no_recvd = -1

    while ack_count != finish_list:
        cl_socket.settimeout(0.05)
        try:
            ack, add = cl_socket.recvfrom(MSS)
            ack_no_recvd = int(ack[0:32], 2)
            if ack_no_recvd == seqno:
                if add[0] in ack_list:
                    ack_list.remove(add[0])
                    ack_count = ack_count + 1

        except socket.timeout:
            print('Timeout, sequence number = ', seqno)
            for ip in ack_list:
                ser_add = (ip, portno)
                magicThread(data_seg, ser_add)
            continue

    return ack_no_recvd


segments = read_text(MSS)
for seg,idx in enumerate(segments):
    ack_list = list(server_list)
    sequence_number = '{:032b}'.format(int(seqno))
    checksum_calculated = checksum(seg, len(seg))
    checksum_sent = '{:16b}'.format(checksum_calculated)
    if idx == len(segments)-1:
        data_seg = sequence_number.encode('utf-8') + checksum_sent.encode('utf-8') + d_packet_last.encode('utf-8') + seg
    else:
        data_seg = sequence_number.encode('utf-8') + checksum_sent.encode('utf-8') + d_packet.encode('utf-8') + seg
    ack_recvd = rdt_send(data_seg, ack_list)

    if ack_recvd == seqno:
        seqno = seqno + 1
    elif ack_recvd == 2 ** 32 - 1:
        seqno = 0


