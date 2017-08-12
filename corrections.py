# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 02:26:18 2017

@author: waleedaman
"""
import os
import pymongo
def addcorrection(text,img):
    connection = pymongo.MongoClient()
    db = connection.fyp
    collection = db.strings
    folder = collection.find_one({"text":text})
    if folder:
        os.rename("C:/img/"+img,"C:/img/dataset/"+str(folder["folder"])+"/"+img+'.jpg')
    else:
        lastfolder=collection.find_one(sort=[("_id", -1)])
        d="C:/img/dataset/"+str(int(lastfolder["folder"])+1)
        os.makedirs(d)
        os.rename("c:/img/"+img+'.jpg',d+'/'+img+'.jpg')
        collection.insert_one({"folder":str(int(lastfolder["folder"])+1),"text":text})