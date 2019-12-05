# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import style
# import numpy as np
# import random
# import math
#
# x= np.arange(0,5)
# y= np.arange(0,5)
# n=0
# # z=np.zeros(0).tolist()
# # zz = np.arange(0, 5)
#
# # while n < 5 :
# #     z.append(zz)
# #     n=n+1
#
# # z=np.random.rand(5,5)
# #
# X,Y = np.meshgrid(x,y)
# #
#
# Z=(X-2)^2
# print Z
# # plt.figure()
# # plt.contour(X,Y,z)
# # plt.show()
#
# # area = funcarea(L,D,H,W,X,Y) #L,D,H and W are all constants defined elsewhere.
#
# # plt.figure()
# # plt.contourf(X,Y,area)
# # plt.show()



# from pylab import *
# X,Y = meshgrid( arange(-2,2,.2),arange(-2,2,.2) )
# U = -2*X*exp(-(X*X + Y*Y))
# V = -2*Y*exp(-(X*X + Y*Y))
# figure()
# Q = quiver( U, V)
# l,r,b,t = axis()
# dx, dy = r-l, t-b
# axis([l-0.05*dx, r+0.05*dx, b-0.05*dy, t+0.05*dy])
# savefig('convfield.png')


import numpy as np
import matplotlib.pyplot as plt

N = 20      # Size of NxN array.
R = 0.25    # Size of the two circular masks.
l = 1.0     # Length of the rod.
l2 = l/2.0  # Saves on typing l/2.0 all the time.

# Define s and z
s_delt = 1.0/(N/2)
s_max =  1*(1.0 + 0.5*s_delt)
s_min =  -1*(1.0 - 0.5*s_delt)
# Square Axes
z_delt = 1.0/(N/2)
z_min = -1*(1.0 - 0.5*z_delt)
z_max =  1*(1.0 + 0.5*z_delt)

s_space_1D = np.arange(s_min,s_max,s_delt)
z_space_1D = np.arange(z_min,z_max,z_delt)

s, z = np.meshgrid(s_space_1D,z_space_1D)

# Find each term in turn
Bs = 1.0/np.sqrt(s**2 + (z - l2)**2) - 1.0/np.sqrt(s**2 + (z + l2)**2)
Bs = Bs + (z + l2)**2 / (s**2 + (z + l2)**2)**1.5 - (z - l2)**2 / (s**2 + (z - l2)**2)**1.5
Bs = (1.0/(l*s))*Bs
Bz = (z + l2) / (s**2 + (z + l2)**2)**1.5 - (z - l2) / (s**2 + (z - l2)**2)**1.5
Bz = (-1.0/l)*Bz

mask = np.logical_or(np.sqrt(s**2 + (z-l2)**2) < R,np.sqrt(s**2 + (z+l2)**2) < R)
Bs = np.ma.masked_array(Bs, mask)
Bz = np.ma.masked_array(Bz, mask)

# plt.close()
plt.box(on='on')
plt.axis('scaled')
plt.axis((-1.1, 1.1, -1.1, 1.1))
plt.title('Magnetic Field Surrounding a Thin Magnetic Needle')
plt.xlabel(r'$\bf s$', fontsize=20)
plt.ylabel(r'$\bf z$', fontsize=20)
plt.quiver(s,z,Bs,Bz,pivot='middle')
plt.show()
# plt.savefig("Magnetic_Field_of_Needle.pdf", format="pdf", transparent=True, bbox_inches='tight')
# plt.savefig("Magnetic_Field_of_Needle.png", format="png", transparent=False, bbox_inches='tight')





# d=13208098098
# c=453
# def func(x):
#     k=d+(c**3)
#     return x+((0.231*(x**3)+0.564*(x**-6))**3)+21+(d/c)+k
#     # return x + 2 * np.cos(x)
# sol=root(func , 0.3)
# a=sol.x
# sol.fun
# print a
