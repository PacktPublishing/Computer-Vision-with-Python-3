"""
===============================
Markers for watershed transform
===============================

The watershed is a classical algorithm used for **segmentation**, that
is, for separating different objects in an image.

Here a marker image is built from the region of low gradient inside the image.
In a gradient image, the areas of high values provide barriers that help to
segment the image.
Using markers on the lower values will ensure that the segmented objects are
found.

See Wikipedia_ for more details on the algorithm.

.. _Wikipedia: http://en.wikipedia.org/wiki/Watershed_(image_processing)

"""
from sys import exit
from scipy import ndimage as ndi
import matplotlib.pyplot as plt

from skimage.morphology import watershed, disk
from skimage import data
from skimage.io import imread
from skimage.filters import rank
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte

img = data.astronaut()
img_gray = rgb2gray(img)

image = img_as_ubyte(img_gray)

#Calculate the local gradients of the image
#and only select the points that have a
#gradient value of less than 20
markers = rank.gradient(image, disk(5)) < 20
markers = ndi.label(markers)[0]

gradient = rank.gradient(image, disk(2))

#Watershed Algorithm
labels = watershed(gradient, markers)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharex=True, sharey=True, subplot_kw={'adjustable':'box-forced'})
ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax[0].set_title("Original")

ax[1].imshow(gradient, cmap=plt.cm.spectral, interpolation='nearest')
ax[1].set_title("Local Gradient")

ax[2].imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
ax[2].set_title("Markers")

ax[3].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax[3].imshow(labels, cmap=plt.cm.spectral, interpolation='nearest', alpha=.7)
ax[3].set_title("Segmented")

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()
