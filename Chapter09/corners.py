from matplotlib import pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.draw import circle
from skimage.feature import corner_harris, corner_subpix, corner_peaks
import math
import numpy as np 

#Read an image
image = imread('test.png')
image = rgb2gray(image)

#Compute the Harris corners in the image. This returns a corner measure response for each pixel in the image
corners = corner_harris(image)

#Using the corner response image we calculate the actual corners in the image
coords = corner_peaks(corners, min_distance=5)

# This function decides if the corner point is an edge point or an isolated peak 
coords_subpix = corner_subpix(image, coords, window_size=13)
image_corner = np.copy(image)

for corner in coords_subpix:
    if math.isnan(corner[0]) or math.isnan(corner[1]):
        continue
    corner = [int(x) for x in corner]
    rr, cc = circle(corner[0], corner[1], 5)
    image_corner[rr, cc] = 255

print(image)
image = image * 255 + image_corner

fig, ax = plt.subplots()
ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)
#ax.plot(coords[:, 1], coords[:, 0], '.b', markersize=3)
#ax.plot(coords_subpix[:, 1], coords_subpix[:, 0], '+r', markersize=15)
#ax.axis((0, 350, 350, 0))
plt.show()
