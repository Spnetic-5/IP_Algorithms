import numpy as np
import cv2
img = cv2.imread('logo.png', cv2.IMREAD_COLOR)
print(img.shape)
img = cv2.resize(img, (500,500))
cv2.line(img, (0,0), (500,500), (128, 0, 128), thickness=10)
cv2.rectangle(img, (0,0), (500,500), (128, 0, 128), thickness=10)
cv2.circle(img, (50,50), 25, (128, 0, 128), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Pransau OP!', (200,250),font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()