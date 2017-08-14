#imports
import os
import cv2
import time
from skimage import measure
import numpy as np
import scipy
import glob
import numpy as np
from sklearn import linear_model
#from sklearn import linear_model as lm
#-------
def trainSGDClf():
    #start=time.time()
    dirs = next(os.walk("img/dataset"))[1]
    dirs=sorted(dirs,key=lambda x:int(x))
    dataset=[]
    imgs=[]
    labels=[]
    for d in dirs:
        files=glob.glob('img/dataset/'+d+'/*.jpg')
        for file in files:
            img=cv2.imread(file)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            (t,img)=cv2.threshold(img,200,1,cv2.THRESH_BINARY)
            imgs.append(cv2.resize(img,(45,45)))
            labels.append(d)
    for img in imgs:
        img=img.flatten()
        dataset.append(np.array(img,dtype=int))
    clf = linear_model.SGDClassifier()
    validlabels = list(range(1,101))
    validlabels=[str(i) for i in validlabels]
    clf.partial_fit(dataset, labels, validlabels)
    #print(dataset)
    #end=time.time()
    #print(end-start)
    return clf