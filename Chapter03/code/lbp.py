from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data
from skimage.color import label2rgb
import numpy as np

# settings for LBP
radius = 3
n_points = 8 * radius

# Get three different images to test the algorithm with
brick = data.load('brick.png')
grass = data.load('grass.png')
wall = data.load('rough-wall.png')

# Calculate the LBP features for all the three images
brick_lbp = local_binary_pattern(brick, 16, 2, 'uniform')
grass_lbp = local_binary_pattern(grass, 16, 2, 'uniform')
wall_lbp = local_binary_pattern(wall, 16, 2, 'uniform')

# Next we will augment these images by rotating the images by 22 degrees
brick_rot = rotate(brick, angle = 22, resize = False)
grass_rot = rotate(grass, angle = 22, resize = False)
wall_rot = rotate(wall, angle = 22, resize = False)

# Let us calculate the LBP features for all the rotated images
brick_rot_lbp = local_binary_pattern(brick_rot, 16, 2, 'uniform')
grass_rot_lbp = local_binary_pattern(grass_rot, 16, 2, 'uniform')
wall_rot_lbp = local_binary_pattern(wall_rot, 16, 2, 'uniform')

# We will pick any one image say brick image and try to find
# its best match among the rotated images
# Create a list with LBP features of all three images

bins_num = int(brick_lbp.max() + 1)
brick_hist = np.histogram(brick_lbp, normed=True, bins=bins_num, range=(0, bins_num))

lbp_features = [brick_rot_lbp, grass_rot_lbp, wall_rot_lbp]
min_score = 1000 # Set a very large best score value initially
idx = 0 # To keep track of the winner

for feature in lbp_features:
    histogram, _ = np.histogram(feature, normed=True, bins=bins_num, range=(0, bins_num))
    p = np.asarray(brick_hist)
    q = np.asarray(histogram)
    filter_idx = np.logical_and(p != 0, q != 0)
    score = np.sum(p[filter_idx] * np.log2(p[filter_idx] / q[filter_idx]))
    if score < min_score:
        min_score = score
        winner = idx
    idx = idx + 1

if idx == 0:
    print('Brick matched with Brick Rotated')
elif idx == 1:
    print('Brick matched with Grass Rotated')
elif idx == 2:
    print('Brick matched with Wall Rotated')
