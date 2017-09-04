from skimage import measure
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import sobel
import matplotlib.pyplot as plt

#Read an image
img = imread('contours.png')

#Convert the image to grayscale
img_gray = rgb2gray(img)

#Find edges in the image
img_edges = sobel(img_gray)

#Find contours in the image
contours = measure.find_contours(img_edges, 0.2)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(img_edges, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
