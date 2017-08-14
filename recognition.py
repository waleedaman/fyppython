# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 03:44:06 2017

@author: waleedaman
"""
import scipy
import cv2
import numpy as np
import os

def sortfiles(x):
    x=x.replace(".jpg","")
    x=int(x)
    return x

def predict(clf,imagepath):
    files=next(os.walk(imagepath+"/"))[2]
    files=sorted(files,key=lambda x:sortfiles(x))
    images=[]
    for file in files:
        img=cv2.resize(cv2.imread(imagepath+'/'+file),(45,45))
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        (t,img)=cv2.threshold(img,200,1,cv2.THRESH_BINARY)
        img=img.flatten()
        img=np.array(img,dtype=int)
        images.append(img)
    arr=clf.predict(images)
    return arr
#predict(trainknn.trainKNN(),"C:/img/1502095133.3304038('192.168.8.119', 53203)")
