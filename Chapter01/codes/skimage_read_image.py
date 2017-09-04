#Program to read an image using skimage

from skimage import io 

#Read image
img = io.imread('image.png')
io.imshow(img)
io.show()

