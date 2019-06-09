# Suggestions (feel free to ignore)
# Generating a random image: use numpy to create a square [m, m, 3] RGB color image
# You can set the quadrant lines by setting pixels to a specific color e.g., [m/2, :, :] = 0, for example
# You might not even need an image processing library. If you'd really like to read about them though, skimage (scikit) and opencv are good starting points
# matplotlib will be easy to use to plot the numpy [m, m, 3] array

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

x1 = np.random.randint(2, size=(100, 100))
x2 = np.copy(x1)

# will need a loop to randomly choose one of these
x2[10:30,40:60] = 0 #top
x2[40:60,70:90] = 0 #right
x2[70:90,40:60] = 0 #bottom
x2[40:60,10:30] = 0 #left

# make a color map of fixed colors - need to make green more "green"
cmap1 = colors.ListedColormap(['white', 'red'])
cmap2 = colors.ListedColormap(['white', 'green'])

fig, axs = plt.subplots(1, 2)

im1 = axs[0].imshow(x1, cmap=cmap1)
axs[0].axis('off')

im2 = axs[1].imshow(x2, cmap=cmap2)
axs[1].axis('off')
 
plt.subplots_adjust(left=0.02, bottom=0.02, right=0.98, top=0.98, wspace=0.05)
plt.show()

