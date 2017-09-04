import cv2
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
new_img = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
cv2.imwrite("thresholding.jpg", new_img[1]) 
cv2.imshow("thresholding", new_img[1])
