#Program to convert a color image to grayscale image 

from skimage import color, io 

#Read an image from a file
img = io.imread('image.png')

#Convert the image tp grayscale
gray_image = color.rgb2gray(img)

io.imshow(gray_image)
io.show()
