import numpy as np
import scipy.integrate as integ

vDotIn = 10/3600
vDotOut = 1.5*vDotIn
t = np.arange(0,2*3600)
V0 = 1000
V = V0#V0+t*(vDotIn-vDotOut)
nA = 200
cA0 = nA/V#np.ones(len(V))*nA/V0
k = .02


def rhs(xy,t):
    x = xy[0]
    y = xy[1]
    dcdt = x*(-k*x-vDotIn/V)
    dccdt = -2*k*x - vDotOut*y/V
    return [dcdt,dccdt]
xy = [cA0,0]
sol = integ.odeint(rhs,xy,t)
print(sol)