from skimage import io
from skimage import filters
img = io.imread("image.jpg")
out = filters.gaussian(img, sigma=5)
io.imsave("gaussian_filter_scikit.jpg", out)
io.imshow(out)
io.show()