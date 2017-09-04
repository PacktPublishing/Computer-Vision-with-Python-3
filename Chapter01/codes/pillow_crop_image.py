#Program to crop an image

from PIL import Image

#Read the image that you want to crop
img = Image.open('image.png')

#Create a dimension tuple
dim = (100, 100, 400, 400)
crop_img = img.crop(dim)

crop_img.show()
