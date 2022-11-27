import numpy as np
from scipy import fftpack 
from PIL import Image 

def erosion(red, maskSize): 
    resImg = np.ones(red.shape)*255
    for i in range(red.shape[0]-maskSize):
        for j in range(red.shape[1]-maskSize):
            black = False 
            for k in range(i,i+maskSize):
                for 1 in range(j,j+maskSize):
                    if red[k,1] == 0:
                        black = True
            if black: 
                for k in range(i,i+maskSize):
                    for 1 in range(j,j+maskSize):
                        resImg[k,1] = 0
    return resImg

def dilation(red, maskSize): 
    resImg = np.ones(red.shape)*255
    for i in range(red.shape[0]-maskSize):
        for j in range(red.shape[1]-maskSize):
            white = False 
            for k in range(i,i+maskSize):   
                for 1 in range(j,j+maskSize):
                    if red[k,1] == 2:
                        white = True
            if white: 
                for k in range(i,i+maskSize):
                    for 1 in range(j,j+maskSize):
                        resImg[k,1] = 0
    return resImg


img = Image.open("greyscale.png")

pix = np.array(img)
red = pix[:,:,0].astype(float)
imsize = red.shape 

maskSize = 3 
resImg = np.zeros(red.shape())
resImg = dilation(red, maskSize)
erosionImg = Image.fromarray(resImg)
erosionImg.show()