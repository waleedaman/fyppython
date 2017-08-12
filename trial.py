# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 09:23:06 2017

@author: waleedaman
"""
import os
import cv2
import time
from skimage import measure
import numpy as np
import scipy
import glob
from sklearn.neighbors import KNeighborsClassifier as KNN

def sortfiles(x):
    x=x.replace(".jpg","")
    x=int(x)
    return x


start=time.time()
dirs = next(os.walk("C:/img/dataset"))[1]
dirs=sorted(dirs,key=lambda x:int(x))
dataset=[]
imgs=[]
labels=[]
for d in dirs:
    files=glob.glob('C:/img/dataset/'+d+'/*.jpg')
    for file in files:
        img=cv2.imread(file)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        (t,img)=cv2.threshold(img,200,1,cv2.THRESH_BINARY)
        imgs.append(cv2.resize(img,(45,45)))
        labels.append(d)
for img in imgs:
    img=img.flatten()
    dataset.append(np.array(img,dtype=int))
knn=KNN(n_neighbors=1)
#print(dataset)
knn.fit(dataset,labels)

imagepath="C:/img/1502099642.3551896('192.168.8.119', 53690)"
files1=next(os.walk(imagepath+"/"))[2]
files1=sorted(files1,key=lambda x:sortfiles(x))
images1=[]
for file in files1:
    img1=cv2.resize(cv2.imread(imagepath+'/'+file),(45,45))
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    (t,img1)=cv2.threshold(img1,200,1,cv2.THRESH_BINARY)
    img1=img1.flatten()
    img1=np.array(img1,dtype=int)
    images1.append(img1)
arr=knn.predict(images1)
print(arr)
end=time.time()
print(end-start)