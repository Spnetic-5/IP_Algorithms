import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('logo.png',cv2.IMREAD_GRAYSCALE)
# img1 = cv2.imread('logo.png',cv2.IMREAD_COLOR)
# img2 = cv2.imread('logo.png',cv2.IMREAD_UNCHANGED)
#IMREAD_COLOR   1
#IMREAD_UNCHANGED  -1
cv2.imshow('image', img)
# cv2.imshow('image1', img1)
# cv2.imshow('imag2e', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Purplelogo.png", img)

# plt.imshow(img, cmap='Purples', interpolation='bicubic')
# plt.plot([50,100],[80,100], 'c', linewidth=5)
# plt.show()
