import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import math


rp=6.3*(10**6)
grid=10**6
pi=math.pi
efield=0.0004
omega=(2*pi)/(3600*24)
Bnol=31*(10**-6)


# pii=pi/50
# angle=0.2
x=np.arange(0,50)
y=np.arange(0,50)
earthx=50/2*grid
earthy=50/2*grid

x=np.multiply(x,grid)
y=np.multiply(y,grid)
X,Y = np.meshgrid(x,y)

rx=(X-earthx)**2
ry=(Y-earthy)**2
r=(rx+ry)
r=np.sqrt(r)

Psi=-(omega*Bnol*(rp**3))/(r)

plt.figure()
plt.contour(X,Y,Psi)
plt.scatter(earthx,earthy)
plt.show()


# plt.scatter(xx, yy, label='contour')
# plt.xlabel('Sumbu X')
# plt.ylabel('Sumbu Y')
# plt.title('Electric Field')
# plt.legend()
# plt.show()