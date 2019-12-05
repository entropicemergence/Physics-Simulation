from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# unit in 1000 km
#
nn=12
Bt=1.04063948e-04

x = np.linspace(-40,40,nn)
y = np.linspace(-40,40,nn)
z = np.linspace(-40,40,nn)
uM=1                   #replacing uM/4pi

x,y,z = np.meshgrid(x,y,z)


fig = plt.figure()
ax = fig.gca(projection='3d')


xxx = np.linspace(-20,20,nn)
yyy = np.linspace(-20,20,nn)
# xxx=np.ones(nn)
# xxx,yyy = np.meshgrid(xxx,xxx)
# yyy=yyy*-1

d=np.abs(xxx)
xxx=np.divide(xxx,d)
kk=np.zeros(0).tolist()
n=0

while n < nn :
    n=n+1
    kk.append(xxx)
# n=0
# while n < nn/2 :
#     n=n+1
#     kk.append(yyy)

kk=np.multiply(kk,Bt)


# print kk

def B(x,y,z):
    r=np.sqrt((x)**2+(y)**2+(z)**2)
    k=1
    # i = 1                                           #Amps in the wire
    # mu = 1.26 * 10**(-6)                            #Magnetic constant
    # mag = (mu/(2*np.pi))*(i/np.sqrt((x)**2+(y)**2)) #Magnitude of the vector B
    # by = mag * (np.cos(np.arctan2(y,x)))           #By
    # bx = mag * (-np.sin(np.arctan2(y,x)))           #Bx
    # bz = z*0                                        #Bz (zero, using the right-hand rule)
    # print mag
    bx=-(uM*3*x*z)/((r)**(5))+ kk
    by = -(uM * 3 * y * z) / ((r) ** (5))
    bz = -((uM * 3 * z * z) / ((r) ** (5)))+2*(1/ ((r) ** (3)))
    # print bx
    return bx,by,bz

# Plot of the fields
bx,by,bz = B(x,y,z)                                   #Magnetic field
# mask = np.logical_or(np.sqrt(np.square(x) + np.square(z)+ np.square(y)) < 1, np.sqrt(np.square(x) + np.square(z)+ np.square(y)))
# x= np.ma.masked_array(x, mask)
# y = np.ma.masked_array(y, mask)
# z = np.ma.masked_array(z, mask)
# bx= np.ma.masked_array(bx, mask)
# by = np.ma.masked_array(by, mask)
# bz = np.ma.masked_array(bz, mask)


# Plot of the 3d vector field
ax.quiver(x,y,z,bx,by,bz,color='b',length=4)        #Plot the magnetic field
# ax.quiver(x,z,bx,bz,color='b',length=1)

# plt.title('Magnetic field of a straight wire')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('scaled')
plt.show()