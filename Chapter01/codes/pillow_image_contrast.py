#Program to change the brightness

from PIL import Image
from PIL import ImageEnhancer

#Read the image 
img = Image.open('image.png')

#Change the constrast of the image
enhancer = ImageEnhancer.Contrast(img)

new_img = enhancer.enchance(2)

new_img.show()
