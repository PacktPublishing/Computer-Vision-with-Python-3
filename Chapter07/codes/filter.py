import cv2
import numpy as np
img = cv2.imread("image.jpg")
ker = np.array([[1, 1, 1],
	[1, 1, 1],
	[1, 1, 1]])
new_img = cv2.filter2D(img,-1,ker)
cv2.imwrite("filter.jpg", new_img)
cv2.imshow("filter", new_img)
