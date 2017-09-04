import cv2
import numpy as np
img = cv2.imread("image.jpg") 
r,c = img.shape[:2]
M = np.float32([[1,0,100],[0,1,100]])
new_img = cv2.warpAffine(img,M,(c,r))
cv2.imwrite("translation.jpg", new_img) 
cv2.imshow("translation", new_img)
