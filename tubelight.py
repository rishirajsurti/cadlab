from scipy import *
from matplotlib.pyplot import *
from numpy import zeros, append
from sys import *
n=input("Enter spatial grid size:")
M=input("Enter number of electrons injected per turn:")
nk=input("Enter Number of turns to simulate:")
u0=input("Threshold velocity:")
p=input("Probability that ionization will occur:")
nM=n*M
Msig=2
print n, M, nk, u0, p, nM
xx=zeros(nM) #electron position
u=zeros(nM) #electron velocity
dx=zeros(nM) #displacement in current turn dx

I=[] #intensity
X=[] #position
V=[] #velocity

    
for k in range(1,nk+1):
    ii=where(xx>0)
    #print 
    dx[ii]=u[ii]+0.5
    xx[ii]=xx[ii]+dx[ii]
    u[ii]=u[ii]+1 

    jj=where(xx>n) #which particles have hit the anode

    xx[jj]=0
    u[jj]=0
    dx[jj]=0

    kk=where(u>=u0) #where velocity greater than threshold
    #kk=kk[0]

    ll=where(rand(len(kk[0]))<=p);
    #ll=ll[0]
    kl=(kk[0])[ll]
    u[kl]=0

    # to find the actual point of  collission
    r=rand()
    xx[kl]=xx[kl]-u[kl]*r-0.5*r*r

    #xx[kl]=xx[kl]-(dx[kl]*rand(1))


    I.extend(xx[kl].tolist())
    m=randn()*Msig+M
    
    # to find unused slots
    aa=where(xx==0) #unused slots
    #aa=aa[0]
    if(len(aa[0])<m):
        xx[aa[0][0:len(aa[0])]]=1
    else:
        xx[aa[0][0:m]]=1

    ii=where(xx>0) #find existing electrons
    #ii=ii[0]
    X.extend(xx[ii].tolist())
    V.extend(u[ii].tolist())

figure('0')
count,bins,rect=hist(X,100)
title('Population plot of X')
figure('1')
hist(I,100)
title('Population plot of light intensity I')
figure('2')
plot(X,V,'o')
title('Electron phase space')
legend(['X vs. V'])


# bins=hist(a)[1]
#xpos=0.5(bins[0:-1]+bins[1:])
show()


print "done!"
    
    
     

    



