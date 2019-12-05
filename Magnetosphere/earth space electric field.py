import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import math
from matplotlib.colors import LogNorm


rp=6.7*(10**6)
grid=10**6
pi=math.pi
efield=0.0004
omega=(2*pi)/(3600*24)
Bnol=31*(10**-6)


# pii=pi/50
# angle=0.2
x=np.arange(0,200)
y=np.arange(0,200)
earthx=(200/2)*grid
earthy=(200/2)*grid

x=np.multiply(x,grid)
y=np.multiply(y,grid)
X,Y = np.meshgrid(x,y)

rx=(X-earthx)**2

YY=Y-earthy
ry=(Y-earthy)**2

r=(rx+ry)
r=np.sqrt(r)

Psi1=np.multiply(YY,efield)
Psi2=-(omega*Bnol*(rp**3))/(r)


Psi=Psi1+Psi2

P=-(2*rp)*(Bnol*rp*omega*efield)**0.5
print P



# print Psi1
# P=Psi[:,25]
# print P


plt.figure()
levels = [P-170000,P-70000,P-40000,P-20000,P-1000,P,P+1000,P+10000,P+15000,P+17500,P+20000,P+21000
    ,P+22000,P+23000,P+24000,P+25000,P+26000,P+27000, P+27500, P+28000,P+28500, P+29000, P+29500, P+30000]
plt.contour(X,Y,Psi,levels)
plt.scatter(earthx,earthy)
plt.axis('equal')
plt.show()
#
#
