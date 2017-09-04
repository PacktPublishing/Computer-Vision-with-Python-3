from skimage import segmentation, color
from skimage.io import imread
from skimage.future import graph
from matplotlib import pyplot as plt

img = imread('test.jpeg')

img_segments = segmentation.slic(img, compactness=20, n_segments=500)
superpixels = color.label2rgb(img_segments, img, kind='avg')

fig, ax = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True, figsize=(6, 8))

ax[0].imshow(img)
ax[1].imshow(superpixels)

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
