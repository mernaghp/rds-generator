import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

#numrows = len(x1)  # you can also use x1.shape, which returns a list I believe
#numcols = len(x1[0])

quad = ['bottom', 'left', 'top', 'right']

cmap1 = colors.ListedColormap(['white', 'red'])
cmap2 = colors.ListedColormap(['white', 'cyan'])

guesses = []

plt.title("Pat's RDS Generator")
plt.axis('off')

t = ('You should see a square pop out near the top, right, bottom, or left.'
     '\nUse the arrow keys to denote which quadrant contains this square.'
     '\n\nPress any arrow to continue.')

plt.text(0.5, 0.5, t, ha='center')

def build_RDS():
    x1 = np.random.randint(2, size=(100, 100))  # 500, 500
    x2 = np.copy(x1)

    quadrant = np.random.randint(0,4)
    if quadrant == 0: # bottom
        x2[10:40,35:65] = x1[10:40,36:66] # x2[100:200,200:300] = x1[100:200,201:301] 
    elif quadrant == 1: # left
        x2[35:65,10:40] = x1[35:65,11:41] # x2[200:300,100:200] = x1[200:300,101:201]
    elif quadrant == 2: # top
        x2[60:90,35:65] = x1[60:90,36:66] # x2[300:400,200:300] = x1[300:400,201:301]
    else: # right
        x2[35:65,60:90] = x1[35:65,61:91] # x2[200:300,300:400] = x1[200:300,301:401]

    plt.clf()

    im1 = plt.imshow(x1, cmap=cmap1, origin='lower')
    im2 = plt.imshow(x2, cmap=cmap2, origin='lower', alpha=0.5)

    plt.axis('off')
    plt.draw()
    print(quad[quadrant])

    guesses.append(quadrant)


def on_keyboard(event):
    if event.key == 'down':
        guesses.append(0)
        build_RDS()
    elif event.key == 'left':
        guesses.append(1)
        build_RDS()
    elif event.key == 'up':
        guesses.append(2)
        build_RDS()
    elif event.key == 'right':
        guesses.append(3)
        build_RDS()

    
plt.gcf().canvas.mpl_connect('key_press_event', on_keyboard)


def output_results():
    # there must be a cleaner way to handle that initial arrow
    # test if guesses isn't empty
    del guesses[0] # initial arrow press before plot loads
    print(guesses)

plt.show()
output_results()

