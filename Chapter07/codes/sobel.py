import cv2
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x_edges = cv2.Sobel(gray,-1,1,0,ksize=5)
cv2.imwrite("sobel_edges_x.jpg", x_edges) 
y_edges = cv2.Sobel(gray,-1,0,1,ksize=5)
cv2.imwrite("sobel_edges_y.jpg", y_edges) 
cv2.imshow("xedges", x_edges)
cv2.imshow("yedges", y_edges)
