import cv2
img = cv2.imread("image.jpg")
new_img = cv2.GaussianBlur(img,(5,5),0)
cv2.imwrite("gaussian_blur.jpg", new_img) 
cv2.imshow("gaussian_blur.jpg", new_img)
