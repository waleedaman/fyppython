#imports
import os
import cv2
import time
from skimage import measure
import numpy as np
import scipy
import glob
from sklearn.neighbors import KNeighborsClassifier as KNN
import numpy as np
from sklearn import linear_model
#from sklearn import linear_model as lm
#-------
def trainKNN():
    #start=time.time()
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
    clf = linear_model.SGDClassifier()
    #clf.partial_fit(X, Y,range(1,101))
    #print(dataset)
    knn.fit(dataset,labels)
    #end=time.time()
    #print(end-start)
    return knn