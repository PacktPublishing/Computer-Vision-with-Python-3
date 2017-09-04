import numpy as np

from skimage.transform import (hough_line, probabilistic_hough_line)
from skimage.feature import canny

#Read an image
image = io.imread('image.png')

#Apply your favorite edge detection algorithm. We use 'canny' for this example.
edges = canny(image, 2, 1, 25)

#Once you have the edges, run the hough transform over the image
lines = hough_lines(image)
probabilistic_lines = probabilistic_hough_line(edges, threshold=10, line_length=5, line_gap=3)

#As an exercise you can compare the results of both the methods.
