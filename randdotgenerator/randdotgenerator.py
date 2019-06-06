# Suggestions (feel free to ignore)
# Generating a random image: use numpy to create a square [m, m, 3] RGB color image
# You can set the quadrant lines by setting pixels to a specific color e.g., [m/2, :, :] = 0, for example
# You might not even need an image processing library. If you'd really like to read about them though, skimage (scikit) and opencv are good starting points
# matplotlib will be easy to use to plot the numpy [m, m, 3] array

import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.randint(2, size=(100, 100))
x2 = np.copy(x1)

# need to figure out how to iterate through a subsection of x2
# and then "copy" those values to a one-position offset

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax1.set_axis_off()

ax2 = fig.add_subplot(1, 2, 2)
ax2.set_axis_off()

# need to change left cmap to red/white
img1 = ax1.imshow(x1, cmap='binary')

# need to change right cmap to green/white
img2 = ax2.imshow(x2, cmap='binary')

plt.show()

