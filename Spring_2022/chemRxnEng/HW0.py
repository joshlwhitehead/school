"""Josh Whitehead
14Jan2022
This code is to solve the system of
equations in HW0 problem 6 in ChEn3353"""

import scipy.integrate as sc
import matplotlib.pyplot as plt
import numpy as np
k = .0266                                               # define constants
f = 1.08
a = .0166
e = -.15
y0 = 1
x0 = 0
tend = 61
t = np.arange(0,tend)


def rhs(xy,t):                                          # define function that returns diff eq
    x = xy[0]
    y = xy[1]
    dxdw = k*y/f*((1-x)/(1+e*x))
    dydw = -a*(1+e*x)/2/y
    return [dxdw,dydw]


xy0 = [x0,y0]                                       

sol = sc.odeint(rhs,xy0,t)                              # vector of x(w),y(w)

x = sol[:,0]                                            #separate x(w),y(w)
y = sol[:,1]

plt.plot(t,x,label='X(W)')                              # plot x(w), y(w) 
plt.plot(t,y,label='y(W)')
plt.title('HW #0 Problem 6')
plt.legend()
plt.grid()
plt.xlabel('W')
plt.savefig('HW0_6')