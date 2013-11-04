# -*- coding: utf-8 -*-
from scipy import *
from scipy import signal
from matplotlib.pyplot import *
import scipy.signal as signal
# time constant is unity. So step of 0.1 is ok.
t=linspace(0,20,201)


num=poly1d([0.1,0,0])
den=poly1d([1,0,1])
sys1=signal.lti(num,den)
y=sys1.step(T=t)[1]
figure(0)
plot(t,y,'r')
xlabel(r'$t$')
title("Q2: Time Response using sys1.step")


num=poly1d([0.1,0])
den=poly1d([1,0,1])
sys1=signal.lti(num,den)
y=sys1.impulse(T=t)[1]
figure(1)
plot(t,y,'r')
xlabel(r'$t$')
title("Q2: Time Response using sys1.impulse")


L=1e-6
# L is 1\muH
C=1e-6
# C is 1\muF
R=100
# R is 100\Omega
omega=logspace(3,9,61).reshape((61,1)) # 4 decades in 41 steps
H=1/((1-omega*omega*L*C) + 1j*omega*R*C)
figure(1)
cla()
subplot(211)
loglog(omega,abs(H),'-ro')
title("Frequency Response")
xlabel(r"$\omega$")
ylabel(r"$|H|$")
subplot(212)
semilogx(omega,180*angle(H)/pi,'-ro')
xlabel(r"$\omega$")
ylabel(r"Arg$(H)$")


figure(2)
cla()
f=omega/(2*pi)
subplot(211)
loglog(f,abs(H),'-ro')
title("Frequency Response")
xlabel(r"$f\;(Hz)$")
ylabel(r"$|H|$")
subplot(212)
semilogx(f,180*angle(H)/pi,'-ro')
xlabel(r"$f\;(Hz)$")
ylabel(r"Arg$(H)$")


den=poly1d([L*C,R*C,1.0]) # s^{2}LC+sRC+1
print roots(den)

sys = signal.lti(1,den)

time=linspace(0,1e-3,1000)
step_response = sys.step(X0=[0,0],T=time)[1]
figure(3)
plot(time, step_response)
axhline(0, color='black')
xlabel(r'$t$')
title('Step response')


Rvals=[0.5,0.8,1.2,1.6,2.01]
time1=linspace(0,3e-5,300)
figure(4)
cla()
ii=where(time<=3e-5) # clip the previous plot
plot(1e6*time[ii],step_response[ii])
str=[r"$R=100\Omega$"]
for R in Rvals:
    den1=poly1d([L*C,R*C,1])
    sys1=signal.lti(1,den1)
    step_response1 = sys1.step(X0=[0,0],T=time1)[1]
    plot(1e6*time1,abs(step_response1))
    str.append(r"$R=%.1f\Omega$" % R)
xlabel(r"$t\;(\mu s)$")
legend(str)


R=2.01
# Critical damping
omega0=5e5
# below resonance but not by much
num2=poly1d([omega0,0]) # \omega_{0}s+0
den2=polymul(den1,poly1d([1,0,omega0*omega0]))
sys2 = signal.lti(num2,den2)
step_response2 = sys2.step(T=time1)[1]
figure(5)
plot(1e6*time1,step_response2)
plot(1e6*time1,sin(omega0*time1),'r')
xlabel(r"$t\;(\mu s)$")
title(r"Response to $\sin(\omega_0 t)u_0(t)$")
legend([r"$v_o(t)$",r"$v_i(t)$"])

show()
