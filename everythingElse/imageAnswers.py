# from PIL import Image
# import numpy as np

# img = Image.open("Lenna.png")

# r,g,b = img.split()
# # Increase Reds
# #r = r.point(lambda i: i * 1.2)

# # Decrease Greens
# g = g.point(lambda i: i * 0)

# # Decrease Greens
# b = b.point(lambda i: i * 0)

# img = Image.merge('RGB', (r, g, b))
# img.show()

# #img.show()

#second way to do it
import cv2

image = cv2.imread('Lenna.png')

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0


g = image.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0


# RGB - Blue
cv2.imshow('B-RGB', b)

cv2.waitKey(0)