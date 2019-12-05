import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import math


rp=6.3*(10^6)
grid=10^6
pi=math.pi
psi=-1
efield=0.0004


# pii=pi/50
# angle=0.2
x=np.arange(0,50)
y=np.arange(0,50)
earthx=50/2
earthy=50/2

X,Y = np.meshgrid(x,y)


while psi <= 1 :
    while angle < (pi - 0.2):
        L = -psi / (efield * rp * (math.sin(angle)))
        y = L * rp * math.cos(angle)
        x = L * rp * math.sin(angle)
        yy.append(x)
        xx.append(y)
        angle = angle + pii
    angle=0.2
    psi=psi+0.1


print yy
uprint xx

plt.scatter(xx, yy, label='contour')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Electric Field')
plt.legend()
plt.show()














