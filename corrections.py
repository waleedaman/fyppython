# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 02:26:18 2017

@author: waleedaman
"""
import os
import pymongo
import numpy as np
import cv2
def addcorrection(text,img):
    connection = pymongo.MongoClient()
    db = connection.fyp
    collection = db.strings
    folder = collection.find_one({"text":text})
    img=cv2.imread("img/"+img)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    (t,img)=cv2.threshold(img,200,1,cv2.THRESH_BINARY)
    img = cv2.resize(img,(45,45))
    img = img.flatten()
    img = np.array(img,dtype=int)
    if folder:
        os.rename("img/"+img,"img/dataset/"+str(folder["folder"])+"/"+img+'.jpg')
        folder = str(folder["folder"])
    else:
        lastfolder=collection.find_one(sort=[("_id", -1)])
        d="img/dataset/"+str(int(lastfolder["folder"])+1)
        folder = str(int(lastfolder["folder"])+1)
        os.makedirs(d)
        os.rename("img/"+img+'.jpg',d+'/'+img+'.jpg')
        collection.insert_one({"folder":str(int(lastfolder["folder"])+1),"text":text})
    return (img,folder)