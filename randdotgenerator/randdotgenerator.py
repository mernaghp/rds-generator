# Suggestions (feel free to ignore)
# Generating a random image: use numpy to create a square [m, m, 3] RGB color image
# You can set the quadrant lines by setting pixels to a specific color e.g., [m/2, :, :] = 0, for example
# You might not even need an image processing library. If you'd really like to read about them though, skimage (scikit) and opencv are good starting points
# matplotlib will be easy to use to plot the numpy [m, m, 3] array

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

x1 = np.random.randint(2, size=(500, 500))
x2 = np.copy(x1)

numrows = len(x1)
numcols = len(x1[0])

quadrant = np.random.randint(1,5)
if quadrant == 1:
    x2[100:200,200:300] = 0
elif quadrant == 2:
    x2[200:300,100:200] = 0
elif quadrant == 3:
    x2[300:400,200:300] = 0
else:
    x2[200:300,300:400] = 0

# make a color map of fixed colors - need to make green more "green"
cmap1 = colors.ListedColormap(['white', 'red'])
cmap2 = colors.ListedColormap(['white', 'green'])

fig, axs = plt.subplots(1, 2)

im1 = axs[0].imshow(x1, cmap=cmap1, origin='lower')
axs[0].axis('off')

im2 = axs[1].imshow(x2, cmap=cmap2, origin='lower')
axs[1].axis('off')
 
plt.subplots_adjust(left=0.02, bottom=0.02, right=0.98, top=0.98, wspace=0.05)
plt.show()

