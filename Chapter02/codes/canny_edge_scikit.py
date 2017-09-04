from skimage import io
from skimage import feature
from skimage import color
img = io.imread("image.jpg")
img = color.rgb2gray(img)
edge = feature.canny(img,3)
io.imshow(edge)
io.imsave("canny_edge.jpg", edge)
io.show()