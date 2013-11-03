
from numpy import zeros, append
from scipy import *
from matplotlib import *
from pylab import *
from sys import *


n = 100
M = 5
Msig = 2
nk = 500
u0 = 7
p = 0.5

if( len(sys.argv) == 6 ):
    
    n = sys.argv[0]
    M = sys.argv[1]
    Msig = sys.argv[2]
    nk = sys.argv[3]
    u0 = sys.argv[4]
    p = sys.argv[5]


xx = zeros( n*M )
u = zeros( n*M )
dx = zeros( n*M )

I = []
X = []
V = []


ii = where( xx > 0 )


for k in range(1,nk+1):
        
    dx[ii] = u[ii] + 0.5
    xx[ii] = xx[ii] + dx[ii]
    u[ii] = u + 1


    jj = where(xx>n);     
    u[jj] = 0
    dx[jj] = 0
    xx[jj] = 0


    kk = where(u>=u0)

    ll = where(rand(len(kk[0]))<=p);
    kl = kk[0][ll]
    u[kl] = 0
    rho = random()
    xx[kl] = xx[kl] - u[kl]*rho - 0.5*rho*rho

    I.extend(xx[kl].tolist())


    m = randn()*Msig + M

    mm = where(xx == 0)

    if(len(mm)>=m):
        xx[mm[0][0:m]] = 1
    else:
        xx[mm[0][0:len(mm)]] = 1


    ii = where(xx>0)

    X.extend(xx[ii].tolist())
    V.extend(xx[ii].tolist())


figure('0') 
pop_count, bins, rect = hist(X,100)

figure('1')
hist(I,100)

figure('2')
plot(X,V, 'ro')

show()

