#Program to write an image

from skimage import io 

#Read an image 
img = io.imread('image.png')

#Write an image to a file 
io.imsave('new_image.png', img)
