# still to do - make size dynamic instead of hardcoded 100 or 500
# stats window at the end - how many successful guesses
# increase offset
# for the moment only perfectly overlay the two plots, but add options for divergence and convergence
# fix colormap - maybe not needed

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.widgets import Slider, RadioButtons, Button

fig, ax = plt.subplots()

quad = ['bottom', 'left', 'top', 'right']

cmap1 = colors.ListedColormap(['white', 'red'])
cmap2 = colors.ListedColormap(['white', 'cyan'])

guesses = []

plt.title("Pat's RDS Generator")
plt.axis('off')

t = ('You should see a square pop out near the top, right, bottom, or left.'
     '\nUse the arrow keys to denote which quadrant contains this square.'
     '\n\nPress any arrow to continue.')

plt.text(0.5, 0.8, t, ha='center')

axcolor = 'lightgoldenrodyellow'

s0 = 100
delta_s = 1

sizeax = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=axcolor)
ssize = Slider(sizeax, 'Size', 50, 500, valinit=s0, valfmt='%0.0f', valstep=delta_s)

def update(val):
    global s0
    s0 = int(ssize.val)
ssize.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    ssize.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red/green', 'red/blue'), active=0)
       
def build_RDS(x, y):
    x1 = np.random.randint(2, size=(x, y))  # 500, 500
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
    plt.axis('off')

    im1 = plt.imshow(x1, cmap=cmap1, origin='lower')
    im2 = plt.imshow(x2, cmap=cmap2, origin='lower', alpha=0.5)

    fig.canvas.draw_idle()
    #plt.draw()
    print(quad[quadrant])

    guesses.append(quadrant)


def on_keyboard(event):
    if event.key == 'down':
        guesses.append(0)
        build_RDS(s0, s0)
    elif event.key == 'left':
        guesses.append(1)
        build_RDS(s0, s0)
    elif event.key == 'up':
        guesses.append(2)
        build_RDS(s0, s0)
    elif event.key == 'right':
        guesses.append(3)
        build_RDS(s0, s0)

    
plt.gcf().canvas.mpl_connect('key_press_event', on_keyboard)


def output_results():
    # there must be a cleaner way to handle that initial arrow
    if guesses:
        del guesses[0] # initial arrow press before plot loads
        print(guesses)
   

plt.show()
output_results()

