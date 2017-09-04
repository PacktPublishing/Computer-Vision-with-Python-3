from PIL import Image
from PIL import ImageFilter
img = Image.open("image.jpg")
img = img.convert("L")
new_img = img.filter(ImageFilter.Kernel((3,3),[1,0,-1,5,0,-5,1,0,1]))
new_img.save("create_filter_image.jpg")
new_img.show()
