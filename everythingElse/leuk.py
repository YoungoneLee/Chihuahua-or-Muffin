# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:01:26 2022

@author: etuba
"""


import numpy as np
# from scipy import fftpack
from PIL import Image


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

def opening(red,maskSize):
    resImg = np.zeros(red.shape,dtype=int)
    resImg = erosion(red, maskSize)
    resImg = diletation(resImg, maskSize)
    return resImg

img = Image.open('burple.jpg')

# create an image for the resulting image 
pix = np.array(img)
# use only one channel
red = pix[:,:,0].astype(float)
green = pix[:,:,1].astype(float)
blue = pix[:,:,2].astype(float)
imsize = red.shape

binary = binarization(red, 220)

cleanImg = opening(binary,5)
for i in range(imsize[0]):
    for j in range(imsize[1]):
        if binary[i,j] == 255: 
            cleanImg[i,j] = 255


# Image.fromarray(binary).show()
Image.fromarray(cleanImg).show()


# Image.fromarray(red).show()

# maskSize = 3


# resImg = diletation(red, maskSize)
# erosionImg = Image.fromarray(resImg)
# erosionImg.show()



















