from scipy import *
import numpy as np
import pylab as pl
from matplotlib.pylab import *
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#for 3d plots
Nx=25
Ny=25
Nbegin=8
Nend=17
Niter=2000

phi=zeros((Nx,Ny))
phi[0,Nbegin:Nend+1]=1.0
print phi
print phi.shape

errors=zeros(Niter)

for k in arange(Niter):
    #save copy of phi
    oldphi=phi.copy();
    #update phi array
    phi[1:-1,1:-1]=0.25*(phi[1:-1,0:-2]+phi[1:-1,2:]+phi[0:-2,1:-1]+phi[2:,1:-1]);

        #assert boundaries
    phi[1:-1,0]=phi[1:-1,1]
    phi[1:-1,-1]=phi[1:-1,-2]
    phi[0,1:-1]=phi[1,1:-1]
    phi[-1,1:-1]=phi[-2,1:-1]

    errors[k]=(abs(phi-oldphi)).max();
#end


print error
print error.shape
x=arange(1,Niter+1)
def powerlaw(x,a,b):
    return a*(x**b)

figure(0)
pars, covar=curve_fit(powerlaw,x,errors)
pl.semilogy(x,errors,'o')
#pl.semilogy(x,powerlaw(x,*pars),'r--')

fig4=figure(4)
ax=p3.Axes3D(fig4)
xx=arange(1,Nx+1)
yy=arange(1,Ny+1)
X,Y=meshgrid(xx,yy)
title('The 3D surface plot of the potential')
surf=ax.plot_surface(Y,X,phi,rstride=1,cstride=1, cmap=cm.jet,linewidth=1)


figure(5)
Jx=0.5*(phi[1:-1,0:-2]-phi[1:-1,2:])
Jy=0.5*(phi[0:-2,1:-1]-phi[2:,1:-1])

quiver(yy,xx,Jy.transpose(),Jx.transpose())


show()
