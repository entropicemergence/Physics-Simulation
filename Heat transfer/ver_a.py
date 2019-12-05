# -*- coding: utf-8 -*-
"""
Created on Tue Apr 02 19:25:02 2019

@author: Bad Boy
"""

import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import cm
#from mpl_toolkits.mplot3d import Axes3D
#import pywt
#import skimage.measure

#xa=np.linspace()

tf_a=(np.ones([300,300]))*300.0
tf_a[100:109,50:240]=305.0
d_t=0.009
h=0.4
hs=h**2
alpha=(np.ones([300,300]))*1.0
alpha[115:119,50:240]=0.09
alpha=alpha[1:-1,1:-1]


for k in range (3000):
    A=(1.0-(4*d_t*alpha/hs))*tf_a[1:-1,1:-1]
    B=(d_t*alpha/hs)*(tf_a[1:-1,:-2]+tf_a[:-2,1:-1]+tf_a[2:,1:-1]+tf_a[1:-1,2:])
#    C=A+B
    tf_a[1:-1,1:-1]=A+B



plt.figure(figsize=(16, 16), dpi=100)
plt.plot()
plt.title("Heat transfer simulation")
#II = plt.imshow(tf_a, extent=[np.min(x), np.max(x), np.min(y), np.max(y)], cmap='jet',
#            norm=colors.Normalize(vmin=z.min(), vmax=z.max()))
II = plt.imshow(tf_a)
plt.show()
















import matplotlib.pyplot as plt
import matplotlib.animation as animation

import matplotlib.image as mpimg

fig = plt.figure()
ax1 = fig.add_subplot(111)

k=0
global k

def animate(i):
    try:
        img = mpimg.imread(str(k)+'.png')
    except IOError:
        c=3
    ax1.clear()
    k=k+1
    global k
    # ax1.imshow(img,extent=[np.min(x),np.max(x),np.min(y),np.max(y)],cmap='jet',norm=colors.Normalize(vmin=v.min(),vmax=v.max()))
    ax1.imshow(img)
    print k


plt.rcParams['animation.ffmpeg_path'] ='C:\\ffmpeg\\bin\\ffmpeg.exe'
FFwriter = animation.FFMpegWriter(bitrate=5000,fps=10)


ani = animation.FuncAnimation(fig, animate, frames=300)
ani.save('SGD Progress.mp4', writer=FFwriter)


















