import cv2
import numpy as np
img = cv2.imread("thresholding.jpg")
ker = np.ones((5,5),np.uint8)
new_img = cv2.erode(img,ker,iterations = 1)
cv2.imwrite("erosion.jpg", new_img) 
cv2.imshow("erosion", new_img)
