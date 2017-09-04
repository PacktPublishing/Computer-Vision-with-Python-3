#Program to enhance an image

from PIL import Image
from PIL import ImageEnhance

#Read an image 
img = Image.open('image.png')

enchancer = ImageEnhance.Brightness(img)
bright_img = enhancer.enhance(2)

bright_img.show()
