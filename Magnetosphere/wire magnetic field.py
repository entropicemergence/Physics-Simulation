from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4,4,10)
y = np.linspace(-4,4,10)
z = np.linspace(-4,4,10)

x,y,z = np.meshgrid(x,y,z)

# 3d figure
fig = plt.figure()
ax = fig.gca(projection='3d')

def B(x,y):
    i = 1                                           #Amps in the wire
    mu = 1.26 * 10**(-6)                            #Magnetic constant
    mag = (mu/(2*np.pi))*(i/np.sqrt((x)**2+(y)**2)) #Magnitude of the vector B
    by = mag * (np.cos(np.arctan2(y,x)))            #By
    bx = mag * (-np.sin(np.arctan2(y,x)))           #Bx
    bz = z*0                                        #Bz (zero, using the right-hand rule)
    # print mag
    return bx,by,bz

def cylinder(r):
    phi = np.linspace(-2*np.pi,2*np.pi,100)
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    return x,y

# Plot of the fields
bx,by,bz = B(x,y)                                   #Magnetic field
cx,cy = cylinder(0.2)                               #Wire

# Plot of the 3d vector field
ax.quiver(x,y,z,bx,by,bz,color='b',length=1)        #Plot the magnetic field
for i in np.linspace(-4,4,800):                     #Plot the wire
    ax.plot(cx,cy,i,label='Cylinder',color='r')

plt.title('Magnetic field of a straight wire')
plt.xlabel('x')
plt.ylabel('y')
plt.show()