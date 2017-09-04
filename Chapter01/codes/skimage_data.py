#Program to get default images in scikit-image 

from skimage import data
from skimage import io 

#Get the camera image 
img_camera = data.camera()

#Get an image with handwritten text
img_text = data.text()

io.show(img_text)
