import cv2
import numpy as np
import time

start_time = time.time()

cap = cv2.VideoCapture("/Users/salil/Work/DeepMagic/Data/DM_Shopping_Data/dm170317_1a/ch03_20170317113600.mp4", cv2.CAP_FFMPEG)
cap.set(cv2.CAP_PROP_POS_FRAMES, 1800)
ret, frame1 = cap.read()
frame1 =cv2.resize(frame1, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255

count = 0

while(1):
    print("Processing frame " + str(count) + " ...")
    count = count + 1
    if count % 3 == 0:
        continue
    ret, frame2 = cap.read()
    if ret == None:
        break

    frame2 = cv2.resize(frame2, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, pyr_scale=0.5, levels=3, winsize=15, iterations=3, poly_n=5, poly_sigma=1.2, flags=0)
 
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

    #cv2.imshow('motion',bgr)
    #cv2.imshow('video', frame2)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png',frame2)
        cv2.imwrite('opticalhsv.png',bgr)
    prvs = next

print("Run time: " % (time.time() - start_time))
cap.release()
cv2.destroyAllWindows()
