import cv2
img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh_img = cv2.threshold(gray,127,255,0)
im, contours, hierarchy = cv2.findContours(thresh_img[1],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (255,0,0), 3)
cv2.imwrite("contours.jpg", img) 
cv2.imshow("contours", img)
