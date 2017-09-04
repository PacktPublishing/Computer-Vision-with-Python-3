#Program to rotate an image

from PIL import Image

#Read the image
img = Image.read('image.png')

#Rotate the image by 90 degress anti-clockwise
rotated_img = img.rotate(90)

rotated_img.show()
