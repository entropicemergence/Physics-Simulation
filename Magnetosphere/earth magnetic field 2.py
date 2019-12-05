import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import math

rp=6.7*(10**6)
grid=(10**6)
pi=math.pi
efield=0.0004
omega=(2*pi)/(3600*24)
Bnol=31*(10**-6)
uM=Bnol*4*pi*(rp**3)

ldel=pi/50

# angle=0.2
earthx=(20/2)*grid
earthz=(20/2)*grid

xx=np.zeros(0).tolist()
zz=np.zeros(0).tolist()

ro=6*grid


while ro < 100*grid :
    l=-pi/2
    while l < pi / 2:
        r = ro * ((np.cos(l)) ** 2)
        x = r * np.cos(l)
        z = r * np.sin(l)
        l = l + ldel
        xx.append(x)
        zz.append(z)
    ro=ro+(2*grid)

ro=6*grid
while ro < 100*grid :
    l=-pi/2
    while l < pi / 2:
        r = ro * ((np.cos(l)) ** 2)
        x = r * np.cos(l)
        z = r * np.sin(l)
        l = l + ldel
        xx.append(-x)
        zz.append(z)
    ro=ro+(2*grid)


mask = np.logical_or(np.sqrt(np.square(xx) + np.square(zz)) < rp, np.sqrt(np.square(zz)) > (30*grid))
mask2 = np.logical_or(np.sqrt(np.square(xx)) > (60*grid),  np.sqrt(np.square(xx)) > (60*grid))
xx= np.ma.masked_array(xx, mask)
xx= np.ma.masked_array(xx, mask2)
zz = np.ma.masked_array(zz, mask)
zz = np.ma.masked_array(zz, mask2)



plt.plot(xx, zz)
plt.axis('scaled')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Z')
plt.show()



