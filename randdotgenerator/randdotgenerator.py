# for the moment only perfectly overlay the two plots, but add options for divergence and convergence
# fix colormaps. 
# ideas - autostereogram
# random line stereogram
# fill the blank area after offset with new random dots
# add another option for how many iterations of RDS to serve up
# refactor RDS build

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.widgets import Slider, RadioButtons, Button
import itertools

fig, ax = plt.subplots()

quad = ['bottom', 'left', 'top', 'right']

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

o0 = 1
delta_o = 1

sizeax = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=axcolor)
offsetax = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=axcolor)

ssize = Slider(sizeax, 'Size', 100, 500, valinit=s0, valfmt='%0.0f', valstep=delta_s)
soffset = Slider(offsetax, 'Offset', 1, 10, valinit=o0, valfmt='%0.0f', valstep=delta_o)

def update(val):
    global s0, o0
    s0 = int(ssize.val)
    o0 = int(soffset.val)
    initial_build_RDS(s0, s0, color1, color2, o0, rdsax)
ssize.on_changed(update)
soffset.on_changed(update)

resetax = plt.axes([0.65, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    ssize.reset()
    soffset.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red/cyan', 'red/blue'), active=0)

# default colors
color1 = 'red'
color2 = 'cyan' 

def colorfunc(label):
     global color1, color2
     pos = label.find("/")
     color1 = label[:pos]
     color2 = label[-pos-1:]
     initial_build_RDS(s0, s0, color1, color2, o0, rdsax)
radio.on_clicked(colorfunc)
     
def initial_build_RDS(x, y, color1, color2, offset, ax):
    x1 = np.random.randint(2, size=(x, y)) 
    x2 = np.copy(x1)

    quadrant = np.random.randint(0,4) 
    if quadrant == 0: # bottom
        x2[int(x*.1):int(x*.4),int(y*.35):int(y*.65)] = x1[int(x*.1):int(x*.4),int(y*.35)+offset:int(y*.65)+offset]
    elif quadrant == 1: # left
        x2[int(x*.35):int(x*.65),int(y*.1):int(y*.4)] = x1[int(x*.35):int(x*.65),int(y*.1)+offset:int(y*.4)+offset]
    elif quadrant == 2: # top
        x2[int(x*.6):int(x*.9), int(y*.35):int(y*.65)] = x1[int(x*.6):int(x*.9), int(y*.35)+offset:int(y*.65)+offset]
    else: # right
        x2[int(x*.35):int(x*.65), int(y*.6):int(y*.9)] = x1[int(x*.35):int(x*.65), int(y*.6)+offset:int(y*.9)+offset]

    ax.axis('off')

    cmap1 = colors.ListedColormap(['white', color1])
    cmap2 = colors.ListedColormap(['white', color2])

    im1 = ax.imshow(x1, cmap=cmap1, origin='lower')
    im2 = ax.imshow(x2, cmap=cmap2, origin='lower', alpha=0.5)

    fig.canvas.draw_idle()


rdsax = plt.axes([0.25, 0.2, 0.5, 0.5])
initial_build_RDS(s0, s0, color1, color2, o0, rdsax)

def build_RDS(x, y, color1, color2, offset):
    x1 = np.random.randint(2, size=(x, y)) 
    x2 = np.copy(x1)

    quadrant = np.random.randint(0,4) 
    if quadrant == 0: # bottom
        x2[int(x*.1):int(x*.4),int(y*.35):int(y*.65)] = x1[int(x*.1):int(x*.4),int(y*.35)+offset:int(y*.65)+offset]
    elif quadrant == 1: # left
        x2[int(x*.35):int(x*.65),int(y*.1):int(y*.4)] = x1[int(x*.35):int(x*.65),int(y*.1)+offset:int(y*.4)+offset]
    elif quadrant == 2: # top
        x2[int(x*.6):int(x*.9), int(y*.35):int(y*.65)] = x1[int(x*.6):int(x*.9), int(y*.35)+offset:int(y*.65)+offset]
    else: # right
        x2[int(x*.35):int(x*.65), int(y*.6):int(y*.9)] = x1[int(x*.35):int(x*.65), int(y*.6)+offset:int(y*.9)+offset]

    plt.clf()
    plt.axis('off')

    cmap1 = colors.ListedColormap(['white', color1])
    cmap2 = colors.ListedColormap(['white', color2])

    im1 = plt.imshow(x1, cmap=cmap1, origin='lower')
    im2 = plt.imshow(x2, cmap=cmap2, origin='lower', alpha=0.5)

    fig.canvas.draw_idle()
    print(quad[quadrant])

    guesses.append(quadrant)


def on_keyboard(event):
    if event.key == 'down':
        guesses.append(0)
        build_RDS(s0, s0, color1, color2, o0)
    elif event.key == 'left':
        guesses.append(1)
        build_RDS(s0, s0, color1, color2, o0)
    elif event.key == 'up':
        guesses.append(2)
        build_RDS(s0, s0, color1, color2, o0)
    elif event.key == 'right':
        guesses.append(3)
        build_RDS(s0, s0, color1, color2, o0)

    
plt.gcf().canvas.mpl_connect('key_press_event', on_keyboard)

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def output_results():
    # there must be a cleaner way to handle that initial arrow
    if guesses:
        del guesses[0] # initial arrow press before plot loads

        numright = 0
        numwrong = 0

        for x, y in pairwise(guesses):
            numright = numright + (x==y)
            numwrong = numwrong + (x!=y)

        print('You got {} right out of {}.'.format(numright, numright + numwrong))
plt.show()
output_results()

