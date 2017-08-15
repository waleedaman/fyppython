#imports
import time
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import scipy
import cv2
import os
#-------

def segmentation(imgname):
    #start=time.time()
    image = cv2.imread(imgname+'.jpg')
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    (t,image)=cv2.threshold(image,200,1,cv2.THRESH_BINARY)
    image=(1-image)
    (h,w)=np.shape(image);
    #cv2.imshow('grey',image)
    rowsum=np.zeros(h,dtype=int)
    
    for i in range(h-1):
        s=0
        for j in range(w-1):
            s+=image[i][j]
        rowsum[i]=s
    maxh=0
    temp=0
    for i in range(h-1):
        if(rowsum[i]<w-5):
            temp=temp+1
        else:
            if(maxh<temp):
                maxh=temp
            temp=0
                
        
    pin=0
    img=[]
    arr1=[]
    for i in range(h-1):
        if(rowsum[i]>w-5):
            if(rowsum[i-1]<w-5):
                img=image[pin:i-1,0:w-1]
                result=np.zeros((maxh,w-1),dtype=int)
                result[:img.shape[0],:img.shape[1]] = img
                if(len(arr1)==0):
                    arr1=result
                else:
                    arr1=np.concatenate((result,arr1),axis=1)
                pin=i+1
            else:
                pin=pin+1
            
    image = measure.label(arr1)
    
    (h,w)=np.shape(image)
    for i in range(w-1):
        tag=0
        for j in range(h-1):
            if ((image[j][i]!=0) & (tag==0)):
                tag=image[j][i]
            if ((image[j][i]!=tag) & (tag!=0) & (image[j][i]!=0)):
                image[image==image[j][i]]=tag

    #slices = measure.regionprops(image)
    slices = scipy.ndimage.find_objects(image)
    os.makedirs(imgname)
    for i,j in enumerate(slices):
        if type(j) is tuple:
            plt.imsave(imgname+'/'+str(j[1].start)+'.jpg',image[j])
    #end=time.time()
    #print(end-start)
    return imgname

