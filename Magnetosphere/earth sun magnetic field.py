from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# unit in 1000 km
#
x = np.linspace(-20,20,15)
y = np.linspace(-20,20,15)
z = np.linspace(-20,20,15)
uM=1                   #replacing uM/4pi

x,y,z = np.meshgrid(x,y,z)

# 3d figure
fig = plt.figure()
ax = fig.gca(projection='3d')

def B(x,y,z):
    r=np.sqrt((x)**2+(y)**2+(z)**2)
    k=1000
    # i = 1                                           #Amps in the wire
    # mu = 1.26 * 10**(-6)                            #Magnetic constant
    # mag = (mu/(2*np.pi))*(i/np.sqrt((x)**2+(y)**2)) #Magnitude of the vector B
    # by = mag * (np.cos(np.arctan2(y,x)))           #By
    # bx = mag * (-np.sin(np.arctan2(y,x)))           #Bx
    # bz = z*0                                        #Bz (zero, using the right-hand rule)
    # print mag
    bx=(-(uM*3*x*z)/((r)**(5)))*k
    by = (-(uM * 3 * y * z) / ((r) ** (5)))*k
    bz = (-((uM * 3 * z * z) / ((r) ** (5)))+2*(1/ ((r) ** (3))))*k
    # print bz
    return bx,by,bz

# Plot of the fields
bx,by,bz = B(x,y,z)                                   #Magnetic field

# Plot of the 3d vector field
ax.quiver(x,y,z,bx,by,bz,color='b',length=1)        #Plot the magnetic field
# ax.quiver(x,z,bx,bz,color='b',length=1)

# plt.title('Magnetic field of a straight wire')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('scaled')
plt.show()