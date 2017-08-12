# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 10:21:22 2017

@author: waleedaman
"""
import pymongo
import numpy as np
import json
from pymongo import MongoClient
def maketext(labels):
    connection = MongoClient()
    db = connection.fyp
    collection = db.strings
    labels=np.flipud(labels)
    text=""
    for label in labels:
        string=collection.find_one({"folder":label})
        text+=string["text"]+" "
    return text