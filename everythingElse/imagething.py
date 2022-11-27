from PIL import Image
import numpy as np
import math



#run parameters
runResize = True
runGray = True
runNeg = False
runAnti = False
runFunky = False
runGray2 = True

#getting image
img = Image.open("download.jpg")
img.show()
width, height = img.size
rBruh, gBruh, bBruh = img.split()
img = Image.merge('RGB', (rBruh, gBruh, bBruh))

if runResize:
    #shrinking image by dis factor
    resFactor = 2
    teenyImage = Image.new('RGB',(int(width/resFactor), int(height/resFactor)))
    for x in range(int(width/resFactor)):
        for y in range(int(height/resFactor)):
            (r,g,b) = img.getpixel((x*resFactor, y*resFactor))
            teenyImage.putpixel((x, y), (r,g,b))

    teenyImage.show()

#DOES NOT WORK YET UHHHH CAN I GET UHhhh..
#for x in range(width-1):
#    for y in range(height-1):       
#        (r1,g1,b1) = img.getpixel((x, y))
#        (r2,g2,b2) = img.getpixel((x + 1, y))
#        (r3, g3, b3) = img.getpixel((x, y + 1))
#        (r4, g4, b4) = img.getpixel((x + 1, y + 1))
#        (avgR, avgG, avgB) = (((r1 + r2 + r3 + r4)/4), ((g1 + g2 + g3 + g4)/4), ((b1 + b2 + b3 + b4)/4))

if runGray:
    #gray scale from RGB Image
    grayImage = Image.new('RGB', (width, height))
    for x in range(0,width):
        for y in range(0,height):
            red = rBruh.getpixel((x,y))
            green = gBruh.getpixel((x,y))
            blue = bBruh.getpixel((x,y))
            gray = math.floor(((red + green + blue)/3))
            grayImage.putpixel((x,y), (gray,gray,gray))
    grayImage.show(title='Ayo where da puffin color go')

grayNeg = Image.new('RGB', (width, height))
rG, gG, bG = grayImage.split()

if runNeg:
    #inverse gray scale

    for x in range(0,width):
        for y in range(0,height):
            newVal = 255 - rG.getpixel((x,y))
            grayNeg.putpixel((x,y), (newVal, newVal, newVal))
    grayNeg.show()

if runAnti:
    antiPuff = Image.new('RGB', (width, height))
    for x in range(0, width):
        for y in range(0, height):
            newValR = 255 - rBruh.getpixel((x,y))
            newValG = 255 - gBruh.getpixel((x,y))
            newValB = 255 - bBruh.getpixel((x,y))
            antiPuff.putpixel((x,y),(newValR, newValG, newValB))

    antiPuff.show()

if runGray2:
    #gray scale from RGB Image
    grayImage = Image.new('RGB', (width, height))
    for x in range(0,width):
        for y in range(0,height):
            red = rBruh.getpixel((x,y))
            green = gBruh.getpixel((x,y))
            blue = bBruh.getpixel((x,y))
            gray = math.floor(((red + green + blue)/3))
            grayLog = 20*math.floor(math.log(1 + gray)) #darker image -- slightly lighter dark because of the shift
            lightPower = 20*math.floor((1 + gray)^2) #darkens image
            grayImage.putpixel((x,y), (grayLog,grayLog,grayLog))
    grayImage.show(title='Ayo where da puffin color go')

grayNeg = Image.new('RGB', (width, height))
rG, gG, bG = grayImage.split()


#
if runFunky:
    splitVal = 128
    funkyImage = Image.new('RGB', (width, height))
    for x in range(0, width):
        for y in range(0, height):
            if (rG.getpixel((x,y))<splitVal):
                newerValR = 0
            else:
                newerValR = 255
            if (gG.getpixel((x,y))<splitVal):
                newerValG = 0
            else:
                newerValG = 255
            if (bG.getpixel((x,y))<splitVal):
                newerValB = 0
            else:
                newerValB = 255
            funkyImage.putpixel((x,y),(newerValR, newerValG, newerValB))

    funkyImage.show()

