from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

nn=5
xxx = np.linspace(-20,20,nn)
yyy = np.linspace(-20,20,nn)
xxx,yyy = np.meshgrid(xxx,yyy)

d=np.abs(yyy)
zzz=np.divide(yyy,d)
k=np.zeros(0).tolist()
n=0

while n < nn :
    n=n+1
    k.append(zzz)

# print k
xx = np.linspace(-20,20,6)
yy = np.linspace(-20,20,6)
zz = np.linspace(-20,20,6)
xx,yy,zz = np.meshgrid(xx,yy,zz)

uu=np.multiply(k,xx)
print uu

# mask = np.logical_or(np.sqrt(np.square(x) + np.square(z)+ np.square(y)) < 1, np.sqrt(np.square(x) + np.square(z)+ np.square(y)))
# x= np.ma.masked_array(x, mask)