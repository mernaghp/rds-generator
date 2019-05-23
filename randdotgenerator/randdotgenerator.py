# Suggestions (feel free to ignore)
# Generating a random image: use numpy to create a square [m, m, 3] RGB color image
# You can set the quadrant lines by setting pixels to a specific color e.g., [m/2, :, :] = 0, for example
# You might not even need an image processing library. If you'd really like to read about them though, skimage (scikit) and opencv are good starting points
# matplotlib will be easy to use to plot the numpy [m, m, 3] array

import numpy as np
import matplotlib.pyplot as plt

# Create random points
N = 3000
x = np.random.rand(N)
y = np.random.rand(N)
area = 18

# Plot
plt.scatter(x, y, s=area, marker='s', edgecolors='none')
plt.show()

