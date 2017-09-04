import cv2
img = cv2.imread("image.jpg")
img_crop = img[0:200, 150:350]
cv2.imwrite("crop_img.jpg", img_crop) 
cv2.imshow("crop", img_crop)
