import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import math

rp=6.7*(10**6)
grid=1
pi=math.pi
efield=0.0004
omega=(2*pi)/(3600*24)
Bnol=31*(10**-6)

uM=Bnol*4*pi*(rp**3)

# pii=pi/50
# angle=0.2
x=np.arange(1,21)
z=np.arange(1,21)
earthx=0
earthz=((20/2)*grid)+1

x=np.multiply(x,grid)
z=np.multiply(z,grid)
X,Z = np.meshgrid(x,z)

X=X
Z=(Z-earthz)
rx=np.multiply(X,X)
rz=(Z)**2
# print X
# print rx

r=(rx+rz)
r=np.sqrt(r)
l=np.arctan(Z/X)

rr=(r**3)
Br=np.sin(l)
Br=(-uM/(2*pi))*Br
Br=np.divide(Br,rr)

Bl=np.cos(l)
Bl=(uM/(4*pi))*Bl
Bl=np.divide(Bl,rr)

# Brr=(Br**2)
# Bll=(Bl**2)
# B=Brr+Bll
# B=B**(0.5)

ll=np.arctan(Bl/Br)
print l
print "deasdef"
ll=ll+l
print ll

Bx=np.cos(ll)
# Bx=np.multiply(Bx,B)

Bz=np.sin(ll)
# Bz=np.multiply(Bz,B)
Bz=np.multiply(Bz,1)



# plt.box(on='on')
# plt.axis('scaled')

# print Bll

plt.figure()
plt.quiver(X,Z,Bx,Bz)
# plt.quiver(X,Z,Br,Bl)
plt.show()

