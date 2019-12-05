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
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg

from os import listdir
from os.path import isfile, join
#from mpl_toolkits.mplot3d import Axes3D
#import pywt
#import skimage.measure

#xa=np.linspace()

tf_a=(np.ones([300,300]))*300.0
tf_a[103:197,103:106]=805.0
tf_a[103:197,193:196]=805.0
d_t=0.009
h=0.4
hs=h**2


alphaa=(np.ones([300,300]))*0.18
alphaa[100:200,100:200]=1.0
maska=np.linspace(0,30,300)
maskb=np.linspace(0,30,300)
maska,maskb=np.meshgrid(maska,maskb)
r=((maska-15.0)**2+(maskb-15.0)**2)**0.5
ra= np.where((r<3.3)&(r>3.1),True,False)
rb=r<3.1
rc=r>3.3
rra=ra*0.04+(rb*0.8)
alphaa=(alphaa*rc)+rra




files = [f for f in listdir('boxa/data') if isfile(join('boxa/data', f))]
hh=len(files)+1
if hh > 1:
    d=np.load("boxa/data/data_"+str(hh-1)+".npy")
    tf_a=d[0]
#    alphaa=d[1]


plt.figure(figsize=(16, 16), dpi=100)
plt.plot()
plt.title("Heat transfer simulation")
#II = plt.imshow(tf_a, extent=[np.min(x), np.max(x), np.min(y), np.max(y)], cmap='jet',
#            norm=colors.Normalize(vmin=z.min(), vmax=z.max()))
II = plt.imshow(alphaa)
plt.show()





fig = plt.figure(figsize=(16, 16), dpi=100)
ax1 = fig.add_subplot(111)

k=0

alpha=alphaa[1:-1,1:-1]
def animate(i):
    global k
    global tf_a
    ax1.clear()
    k=k+1
    for j in range (30):
        A=(1.0-(4*d_t*alpha/hs))*tf_a[1:-1,1:-1]
        B=(d_t*alpha/hs)*(tf_a[1:-1,:-2]+tf_a[:-2,1:-1]+tf_a[2:,1:-1]+tf_a[1:-1,2:])
        tf_a[1:-1,1:-1]=A+B
    ax1.imshow(tf_a)
    plt.subplots_adjust(top=0.99, right=0.99, left=0.05, bottom=0.01)
#    ax.margins(x=0)
    print k




plt.rcParams['animation.ffmpeg_path'] ='C:\\ffmpeg\\bin\\ffmpeg.exe'
FFwriter = animation.FFMpegWriter(bitrate=5000,fps=10)

ani = animation.FuncAnimation(fig, animate, frames=200)
ani.save('boxa/result_'+str(hh)+'.mp4', writer=FFwriter)

tf_aa=np.zeros([2,300,300])
#tf_aa=np.append(tf_a,alphaa,axis=1)
tf_aa[0]=tf_a
tf_aa[1]=alphaa
np.save('boxa/data/data_'+str(hh)+'.npy',tf_aa)
##
##
#







