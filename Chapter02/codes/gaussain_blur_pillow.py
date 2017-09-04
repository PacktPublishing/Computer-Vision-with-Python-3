from PIL import Image
from PIL import ImageFilter
img = Image.open("image.jpg")
blur_img = img.filter(ImageFilter.GaussianBlur(5))
blur_img.save("GaussianBlur.jpg")
blur_img.show()