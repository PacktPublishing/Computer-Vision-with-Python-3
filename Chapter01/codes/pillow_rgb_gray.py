#Program to convert RGB images to Gray scale images

from PIL import Image

#Read the image that you wnat to convert
img = Image.open('image.png')

#Convert the image to grayscale
gray_image = img.convert("L")

gray_image.show()
