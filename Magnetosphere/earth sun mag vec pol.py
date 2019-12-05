from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# unit in 1000 km

nn=50
Bt=0.00015
u=0.31


x = np.linspace(-40,20,nn*2)
z = np.linspace(-20,20,nn)
                 #replacing uM/4pi

x,z = np.meshgrid(x,z)


xxx = np.linspace(-20,20,nn*2)
yyy = np.linspace(-20,20,nn)
xxx,yyy = np.meshgrid(xxx,yyy)
d=np.abs(yyy)
yyy=np.divide(yyy,d)

# print yyy

# print kk

def B(x,z):
    r=np.sqrt((x)**2+(z)**2)
    # i = 1                                           #Amps in the wire
    # mu = 1.26 * 10**(-6)                            #Magnetic constant
    # mag = (mu/(2*np.pi))*(i/np.sqrt((x)**2+(y)**2)) #Magnitude of the vector B
    # by = mag * (np.cos(np.arctan2(y,x)))           #By
    # bx = mag * (-np.sin(np.arctan2(y,x)))           #Bx
    # bz = z*0                                        #Bz (zero, using the right-hand rule)
    # print mag
    bx=-(u*3*x*z)/((r)**(5))+yyy*Bt
    # by=-(u*3*y*z)/((r)**(5))
    bz = -((u * 3 * z * z) / ((r) ** (5)))+u*(1/ ((r) ** (3)))

    BB = np.sqrt(np.square(bx) + np.square(bz))
    bx=bx/BB
    bz=bz/BB

    # print bx
    return bx,bz,BB

# Plot of the fields
bx,bz,BB= B(x,z)                                   #Magnetic field
print BB
# print BB
mask = np.logical_or(np.sqrt(np.square(x) + np.square(z)) < 1, np.sqrt(np.square(x) + np.square(z))< 0.5)
x= np.ma.masked_array(x, mask)
z = np.ma.masked_array(z, mask)
bx= np.ma.masked_array(bx, mask)
bz = np.ma.masked_array(bz, mask)


# Plot of the 3d vector field
# plt.quiver(x,z,bx,bz,color='b',length=4)        #Plot the magnetic field
# ax.quiver(x,z,bx,bz,color='b',length=1)

Q=plt.figure()
QQ=Q.gca()
QQ.quiver(x, z, bx, bz, color='b',headwidth=5, headlength=10, scale=60)
# qk = plt.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   # coordinates='figure')
#
plt.xlabel('x')
plt.ylabel('y')
plt.axis('scaled')
plt.show()