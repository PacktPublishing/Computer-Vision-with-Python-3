import cv2
import numpy as np
import random

image = cv2.imread('image.jpg')
image_rot = cv2.imread('image_rot.jpg')
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray_rot = cv2.cvtColor(image_rot,cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create()

kp, desc = surf.detectAndCompute(gray,None)
kp_rot, desc_rot = surf.detectAndCompute(gray_rot, None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(desc,desc_rot, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.4*n.distance:
        good.append([m])
random.shuffle(good)

# cv2.drawMatchesKnn expects list of lists as matches.
image_match = cv2.drawMatchesKnn(image,kp,image_rot,kp_rot,good[:10],flags=2, outImg=None)

cv2.imwrite('surf_matches.jpg',image_match)
