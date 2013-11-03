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

#print x.shape
#X=array([x,ones_like(x)]).T 
#print X
#print X.shape

#y=log(errors)
#y=y*2.303
#result=lstsq(X,y,rcond=-1)
#coeff=result[0]
#z=coeff[0]*(e**coeff[1])
#plot(x,z)
#print m,c
#plot(x,m*X[0:,0]+c*X[0:,1])
