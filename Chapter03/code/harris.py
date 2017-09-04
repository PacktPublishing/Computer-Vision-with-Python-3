from matplotlib import pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.feature import corner_harris, corner_subpix, corner_peaks

#Read an image
image = imread('test.png')
image = rgb2gray(image)

#Compute the Harris corners in the image. This returns a corner measure response for each pixel in the image
corners = corner_harris(image)

#Using the corner response image we calculate the actual corners in the image
coords = corner_peaks(corners, min_distance=5)

# This function decides if the corner point is an edge point or an isolated peak 
coords_subpix = corner_subpix(image, coords, window_size=13)

fig, ax = plt.subplots()
ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)
ax.plot(coords[:, 1], coords[:, 0], '.b', markersize=3)
ax.plot(coords_subpix[:, 1], coords_subpix[:, 0], '+r', markersize=15)
ax.axis((0, 350, 350, 0))
plt.show()
