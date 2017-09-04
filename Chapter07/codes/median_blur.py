import cv2
img = cv2.imread("image.jpg")
new_img = cv2.medianBlur(img,5)
cv2.imwrite("median_blur.jpg", new_img) 
cv2.imshow("median_blur", new_img)
