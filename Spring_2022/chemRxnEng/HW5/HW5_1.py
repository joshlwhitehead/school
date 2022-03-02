import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt

vDotIn = 10
vDotOut = 1.5*vDotIn
t = np.linspace(0,2)
V0 = 1000
V = V0+t*(vDotIn-vDotOut)
nA = 200
cA0 = nA/V0
k = .02*3600


def rhs(AP,t):
    cA = AP[0]
    cP = AP[1]
    dcadt = -cA*(k*cA + (vDotIn-vDotOut)/(V0+t*(vDotIn-vDotOut)))
    
    dcpdt = 2*k*cA**2 - (vDotIn-vDotOut)*cP/(V0+t*(vDotIn-vDotOut))
    
    
    return [dcadt,dcpdt]
xy = [cA0,0]
sol = integ.odeint(rhs,xy,t)

plt.plot(t,sol[:,0],label='cA')
plt.plot(t,sol[:,1],label='cP')
plt.legend()
plt.grid()
plt.ylabel('Concentratoin (mol/L)')
plt.xlabel('Time (hr)')
plt.title('Molar Concentration of A and P')
plt.savefig('HW5_1b')

print(2*vDotOut*sol[:,0][-1])
print(2*vDotOut*sol[:,1][-1])