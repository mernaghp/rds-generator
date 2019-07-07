# Suggestions (feel free to ignore)
# Generating a random image: use numpy to create a square [m, m, 3] RGB color image
# You can set the quadrant lines by setting pixels to a specific color e.g., [m/2, :, :] = 0, for example
# You might not even need an image processing library. If you'd really like to read about them though, skimage (scikit) and opencv are good starting points
# matplotlib will be easy to use to plot the numpy [m, m, 3] array

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

#numrows = len(x1)  # you can also use x1.shape, which returns a list I believe
#numcols = len(x1[0])

quad = {1:'bottom', 2:'left', 3:'top', 4:'right'}  # you could also use a list e.g., quad = ['bottom', 'left' ...], and then call quad[i + 1]

cmap1 = colors.ListedColormap(['white', 'red'])
cmap2 = colors.ListedColormap(['white', 'cyan'])

guesses = []

plt.axis('off')
plt.title("Pat's RDS Generator")

def build_RDS():
    x1 = np.random.randint(2, size=(100, 100))  # 500, 500
    x2 = np.copy(x1)

    quadrant = np.random.randint(1,5)
    if quadrant == 1: # bottom
        x2[10:40,35:65] = x1[10:40,36:66] # x2[100:200,200:300] = x1[100:200,201:301] 
    elif quadrant == 2: # left
        x2[35:65,10:40] = x1[35:65,11:41] # x2[200:300,100:200] = x1[200:300,101:201]
    elif quadrant == 3: # top
        x2[60:90,35:65] = x1[60:90,36:66] # x2[300:400,200:300] = x1[300:400,201:301]
    else: # right
        x2[35:65,60:90] = x1[35:65,61:91] # x2[200:300,300:400] = x1[200:300,301:401]

    im1 = plt.imshow(x1, cmap=cmap1, origin='lower')
    im2 = plt.imshow(x2, cmap=cmap2, origin='lower', alpha=0.5)

    plt.draw()
    print(quad[quadrant])


def on_keyboard(event):
    global guesses
    if event.key == 'right':
        build_RDS()
        guesses.append('right')
    elif event.key == 'left':
        build_RDS()
        guesses.append('left')
    elif event.key == 'up':
        build_RDS()
        guesses.append('top')
    elif event.key == 'down':
        build_RDS()
        guesses.append('bottom')
    
plt.gcf().canvas.mpl_connect('key_press_event', on_keyboard)

plt.show()

