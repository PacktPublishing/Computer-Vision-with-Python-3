import cv2

cam = cv2.VideoCapture('/Users/salil/Downloads/VID_20170701_160759.mp4')

while (cam.isOpened()):

         ret, frame = cam.read()
         frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
         gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         cv2.imshow('gray_frame',gray_frame)
         cv2.imshow('original_frame',frame)

         if cv2.waitKey(1) & 0xFF == ord('q'):
                  break
               
cam.release()
cv2.destroyAllWindows()
