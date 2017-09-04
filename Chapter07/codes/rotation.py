import cv2
img = cv2.imread("image.jpg")
r,c = img.shape[:2]
M = cv2.getRotationMatrix2D((c/2,r/2),90,1)
new_img = cv2.warpAffine(img,M,(c,r))
cv2.imwrite("rotate_img.jpg", new_img) 
cv2.imshow("rotate", new_img)
