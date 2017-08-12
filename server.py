# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 09:56:40 2017

@author: waleedaman
"""
import corrections
import socket
import plot_labels
import trainknn
import recognition
import generatestring
import threading
import struct
import sys
import time
#imports-

def saveimage(client,addr,knn):
    buf = b''
    c=''
    stop=True
    while stop:
        c = client.recv(1)
        if c == b'-':
        	stop=False
        else:
        	buf+=c
    size = struct.unpack('!i', buf)[0]
    buf = b''
    c=''
    stop=True
    while stop:
        c = client.recv(1)
        if c == b'-':
        	stop=False
        else:
        	buf+=c
    dataType=str(buf)
    print ("receiving %s bytes" % size)
    if dataType == "b'image'":
        imagename='C:/img/'+str(time.time())+str(addr)
        with open(imagename+'.jpg', 'wb') as img:
            btr=10
            while size>0:
                if size<btr:
                    btr=size
                data = client.recv(btr)
                img.write(data)
                size=size-btr
            img.close()
        client.close()
        time.sleep(8)
        plot_labels.segmentation(imagename)
        labels = recognition.predict(knn,imagename)
        string = generatestring.maketext(labels)
        sock = socket.socket()
        sock.connect((addr[0],2023))
        sock.send(string.encode())
    if dataType == "b'correction'":
        print('correction')
        stop = True
        buf = b''
        text = ''
        while stop:
            c = client.recv(1)
            if c == b'-':
                stop = False
            else:
                buf += c
        imgpath = 'C:/img/'
        imagename = str(time.time())+str(addr)
        with open(imgpath+imagename+'.jpg', 'wb') as img:
            btr=10
            while size>0:
                if size<btr:
                    btr=size
                data = client.recv(btr)
                img.write(data)
                size=size-btr
        client.close()
        print(text)
        corrections.addcorrection(buf.decode("utf-8"),imagename)
        global retrain
        retrain = True


def callmethods(client,addr,knn):
    start=time.time()
    saveimage(client,addr,knn)
    end=time.time()
    print(end-start)


address = ("0.0.0.0", 2020)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except (socket.error):
    sys.exit()
print ('Socket Created')
s.bind(address)
knn=trainknn.trainKNN()
retrain = False
s.listen(5)
while True:
    (client, addr) = s.accept()
    print ('got connected from', client,addr)
    if retrain:
        knn=trainknn.trainKNN()
        retrain = False
    thread=threading.Thread(target=callmethods,args=(client,addr,knn))
    print('started thread')
    thread.start()
    
    