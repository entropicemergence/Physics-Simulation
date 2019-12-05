from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.colors as colors

# unit in 1000 km

nn=50
Bt=0.00015
u=0.31
pi=np.pi


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

    bx=-(u*3*x*z)/((r)**(5))+yyy*Bt
    bz = -((u * 3 * z * z) / ((r) ** (5)))+u*(1/ ((r) ** (3)))
    Bx=bx*100000
    Bz = bz * 100000
    BB = np.sqrt(np.square(Bx) + np.square(Bz))
    # print BB
    # BB=np.log(BB)
    # BB=np.abs(BB)
    #
    # # BB=np.square(BB)
    # # BB=np.square(BB)
    # # BB=np.sqrt(BB)
    # # print BB
    BB=BB*0.0000073
    # print BB
    bx=bx/BB
    bz=bz/BB

    # print bx
    return bx,bz,BB

# Plot of the fields
bx,bz,BB= B(x,z)

# print BB
mask = np.logical_or(np.sqrt(np.square(x) + np.square(z)) < 1, np.sqrt(np.square(x) + np.square(z))< 0.5)
x= np.ma.masked_array(x, mask)
z = np.ma.masked_array(z, mask)
bx= np.ma.masked_array(bx, mask)
bz = np.ma.masked_array(bz, mask)
# BB = np.ma.masked_array(BB, mask)
# colors = BB
# norm = Normalize()
# norm.autoscale(colors)
# colormap = cm.inferno

# Plot of the 3d vector field
# plt.quiver(x,z,bx,bz,color='b',length=4)        #Plot the magnetic field
# ax.quiver(x,z,bx,bz,color='b',length=1)
BB=BB
a=BB.max()
b=BB.min()

# print a
# print b

ex=np.zeros(0).tolist()
ez=np.zeros(0).tolist()
n=0
while n <= 2*pi:
    exx=np.cos(n)
    ezz=np.sin(n)
    ex.append(exx)
    ez.append(ezz)
    n=n+(pi/10)

# print ex


Q=plt.figure()
QQ=Q.gca()
QQ=QQ.quiver(x, z, bx, bz, BB,cmap='coolwarm',
           norm=colors.LogNorm(vmin=BB.min(),vmax=BB.max()),headwidth=5, headlength=10, scale=60)

# QQ.quiver(x, z, bx, bz, BB,cmap='autumn',
#            norm=colors.LogNorm(vmin=BB.min(),vmax=BB.max()),headwidth=5, headlength=10, scale=60)
# qk = plt.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   # coordinates='figure')


I=plt.imshow(BB,extent=[np.min(x),np.max(x),np.min(z),np.max(z)],cmap='autumn',norm=colors.LogNorm(vmin=BB.min(),vmax=BB.max()))

Q.colorbar(I,extend='max')
Q.colorbar(QQ,extend='max')
plt.plot(ex,ez)


plt.xlabel('x')
plt.ylabel('y')
plt.axis('scaled')
plt.show()