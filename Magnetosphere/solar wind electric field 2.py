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


# pii=pi/50
# angle=0.2
x=np.arange(0,50)
y=np.arange(0,50)
earthx=50/2*grid
earthy=50/2*grid

X,Y = np.meshgrid(x,y)

X=X*grid
Y=Y*grid

L=np.multiply(Y,efield)

plt.figure()
plt.contour(X,Y,L)
plt.scatter(earthx,earthy)
plt.show()

# plt.scatter(xx, yy, label='contour')
# plt.xlabel('Sumbu X')
# plt.ylabel('Sumbu Y')
# plt.title('Electric Field')
# plt.legend()
# plt.show()