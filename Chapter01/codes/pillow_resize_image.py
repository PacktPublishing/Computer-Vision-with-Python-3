#Program to resize a given image

from PIL import Image

#Read the image that you want to resize
img = Image.open('image.png')

#Resize the image
resize_img = img.resize((200, 200))

resize_img.show()
