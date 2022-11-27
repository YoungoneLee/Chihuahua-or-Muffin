# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:30:05 2022

@author: etuba
"""

from PIL import Image, ImageFilter
import numpy as np
###############################################################################
# OPEN IMAGE with PIL: it will create variable of type Image
##### For full specification of the type Image based on the image type, visit
##### https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
img = Image.open("lenna.png")
###############################################################################

###############################################################################
# SHOW IMAGE with PIL:
img.show()
###############################################################################

###############################################################################
# To extract color channels and use them as matrices
colorChannels = np.asarray(img)
# To create an image from
newImg = Image.fromarray(colorChannels)
############################################################################### 

###############################################################################
# CONVERTING IMAGE INTO DIFFERENT COLOR MODELS
# input image to be of mode GRAYSCALE (L)
#img = img.convert("L")
# convert to other color models with PIL
# To see all supported modes, visit
# https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
# good read: https://holypython.com/python-pil-tutorial/color-modes-explained-for-digital-image-processing-in-python-pil/
imgYCbCr = img.convert("YCbCr")
# Extract only Cb channel
cb = np.array(imgYCbCr)
cb[:,:,0] *= 0 # set Y channel to 0
cb[:,:,2] *= 0 # set Cr channel to 0
cb = Image.fromarray(cb,mode='YCbCr')
cb.show()

# The best representation is given by setting all channels to C
cb = np.array(imgYCbCr)
cb[:,:,0] = cb[:,:,1]
cb[:,:,2] = cb[:,:,1]
cb = Image.fromarray(cb,mode='YCbCr')
cb.show()
###############################################################################

###############################################################################


# NEGATIVE
from PIL import ImageOps
imgNegative = ImageOps.invert(img)
imgNegative.show()
###############################################################################

###############################################################################
# APPLY ANY FILTER by defining mask and its size
# Mean filter
imgMean = img.filter(ImageFilter.Kernel((3, 3), (1/9, 1/9, 1/9, 1/9, 1/9,        
                                               1/9, 1/9, 1/9, 1/9), 1, 0))  
imgMean.show()


# Calculating Edges using the passed laplican Kernel
edges = img.filter(ImageFilter.Kernel((3, 3), (-1, -2, -1, -2, 12,
                                          -2, -1, -2, -1), 1, 0))

# Median filter (built in)
imgMedian = img.filter(ImageFilter.MedianFilter(size = 5))
###############################################################################

# THRESHOLDING
# use lambda expressions


###############################################################################
# Morphological operations - It can be written better!!! 
# You can use methods from skimage.morphology - Find how!
from skimage.morphology import (erosion, dilation, closing, opening,
                                area_closing, area_opening)
def erosion(red,maskSize):
    resImg = np.ones(red.shape)*255
    for i in range(red.shape[0]-maskSize):
        for j in range(red.shape[1]-maskSize):
            black = False
            for k in range(i,i+maskSize):
                for l in range(j,j+maskSize):
                    if red[k,l] == 0:
                        black = True
            if black:
                for k in range(i,i+maskSize):
                    for l in range(j,j+maskSize):
                        resImg[k,l] = 0
    return resImg

def diletation(red,maskSize):
    resImg = np.zeros(red.shape)
    for i in range(red.shape[0]-maskSize):
        for j in range(red.shape[1]-maskSize):
            white = False
            for k in range(i,i+maskSize):
                for l in range(j,j+maskSize):
                    if red[k,l] == 255:
                        white = True
            if white:
                for k in range(i,i+maskSize):
                    for l in range(j,j+maskSize):
                        resImg[k,l] = 255
    return resImg

def binarization(red,thresholdValue):
    resImg = np.zeros(red.shape,dtype=int)
    for i in range(red.shape[0]):
        for j in range(red.shape[1]):
            if red[i,j] <= thresholdValue:
                resImg[i,j] = 255
            else:
                resImg[i,j] = 0
    return resImg

def betterBinarization(img,threshold):
    resImg = np.asarray(img)
    avgVal = np.average(resImg)
    resImg[resImg<=threshold] = 0
    resImg[resImg>threshold] = 255
    return Image.fromarray(resImg)

betterBinarization(img, 127).show()

def opening(red,maskSize):
    resImg = np.zeros(red.shape,dtype=int)
    resImg = erosion(red, maskSize)
    resImg = diletation(resImg, maskSize)
    return resImg

###############################################################################



###############################################################################
# SAVE IMAGE
edges.save("EDGE_sample.png")
###############################################################################
