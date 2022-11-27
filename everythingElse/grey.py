import cv2
import numpy as np

def grayConversion(image):
    grayValue = 0.07 * image[:,:,2] + 0.72 * image[:,:,1] + 0.21 * image[:,:,0]
    gray_img = grayValue.astype(np.uint8)
    return gray_img

orig = cv2.imread(r'lenna.png', 1)
g = grayConversion(orig)

cv2.imshow("Original", orig)
cv2.imshow("GrayScale", g)
cv2.waitKey(0)
cv2.destroyAllWindows()
