#Program to convert a color image to grayscale image 

from skimage import color, io 

#Read an image from a file
img = io.imread('image.png')

#Convert the image tp grayscale
hsv_image = color.rgb2hsv(img)

io.imshow(hsv_image)
io.show()
