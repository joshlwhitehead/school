import numpy as np
from scipy.integrate import odeint

T0 = 700
dHR = -5000
thet = 1
cp = 35
k = .1
v = 5

def ode(x,V):
    T = T0 + -dHR*x/thet/cp
    dxdv = k/v*(1-x)/(1+.2*x)*T0/T
    
    return dxdv

V = np.linspace(0,59)
init = 0

x = odeint(ode,init,V)
print(x[-1][-1])
T = T0 + -dHR*x/thet/cp
print(T[-1][-1])
