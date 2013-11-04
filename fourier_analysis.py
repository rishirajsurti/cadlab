# -*- coding: utf-8 -*-
from scipy import *
from matplotlib.pyplot import *
t=linspace(-25,25,257)*1e-6;t=t[0:-1]
vi=zeros(shape(t))
ii=where( (t>=-5e-6)*(t<=5e-6)>0 )
vi[ii]=1
figure(0)
cla()
plot(t,vi,'r')


Vi=fft(vi)
wmax=1/(t[1]-t[0])
frq=linspace(-0.5,0.5,257)*wmax
frq=frq[0:-1]
Vi=hstack([Vi[128:256],Vi[0:128]])
figure(1)
subplot(211)
plot(frq,abs(Vi),'k')
subplot(212)
plot(frq,angle(Vi)*180/pi,'k')


omega=2*pi*frq
den=poly1d([-1e-12,1e-6j,1.0]) # -\omega^{2}LC+j\omega RC+1
H=1/den(omega)


Vo=Vi*H
figure(2)
subplot(211)
plot(frq,abs(Vo),'k')
subplot(212)
plot(frq,angle(Vo)*180/pi,'k')

Vo=hstack([Vo[128:256],Vo[0:128]])
vo=ifft(Vo)
figure(0)
plot(t,vo,'g')
show()
