# Python program to demonstrate erosion and
# dilation of images.
import numpy as np
import cv2
import json
from matplotlib import pyplot as plt

#from scratch 
def read_this(image_file):
    image_src = cv2.imread(image_file, 0)
    return image_src

def convert_binary(image_src, thresh_val):
    color_1 = 255
    color_2 = 0
    initial_conv = np.where((image_src <= thresh_val), image_src, color_1)
    final_conv = np.where((initial_conv > thresh_val), initial_conv, color_2)
    return final_conv

def binarize_this(image_file, thresh_val=127):
    image_src = read_this(image_file=image_file)
    image_b = convert_binary(image_src=image_src, thresh_val=thresh_val)
    return image_b


def erode_lib(image_file, level=3, with_plot=True):
    level = 3 if level < 3 else level
    image_src = binarize_this(image_file=image_file)
    # library method
    image_eroded = cv2.erode(src=image_src, kernel=np.ones((level, level)), iterations=1)

    if with_plot:
        cmap_val = 'gray'
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 20))

        ax1.axis("off")
        ax1.title.set_text('Original')

        ax2.axis("off")
        ax2.title.set_text("Eroded - {}".format(level))

        ax1.imshow(image_src, cmap=cmap_val)
        ax2.imshow(image_eroded, cmap=cmap_val)
        plt.show()
        return True
    return image_eroded

erode_lib(image_file='burple.jpg', level=3, with_plot=True)

# # Reading the input image
# img = cv2.imread('greyscale.png', 0)
 
# # Taking a matrix of size 5 as the kernel
# kernel = np.ones((5, 5), np.uint8)
 
# # The first parameter is the original image,
# # kernel is the matrix with which image is
# # convolved and third parameter is the number
# # of iterations, which will determine how much
# # you want to erode/dilate a given image.
# img_erosion = cv2.erode(img, kernel, iterations=1)
# img_dilation = cv2.dilate(img, kernel, iterations=1)
 
# cv2.imshow('Input', img)
# cv2.imshow('Erosion', img_erosion)
# cv2.imshow('Dilation', img_dilation)
 
# cv2.waitKey(0)

