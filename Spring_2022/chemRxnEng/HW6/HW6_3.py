import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


T0 = 300                                    #k
V = 10                                      #L
v0 = 2                                      #L/s
c = 6                                       #mol/L
Ha0 = -10                                   #kcal/mol @273k
Hb0 = -5                    
Hc0 = -20
Cpa = 10/1000                               #kcal/mol/k
Cpb = 12/1000                               
Cpc = 22/1000  
k300 = .02                                     #L/mol/s @300k
E = 8                                       #kcal/mol
cA0 = 6
FA0 = cA0*v0
R = 1.986e-3
A = k300/np.exp(-E/R/300)
def k(temp):
    return A*np.exp(-E/R/temp)

dCp = -(Cpa+Cpb-Cpc)
TR = 273
dHR = Hc0-Hb0-Ha0

def prob(x):
    T = T0-x*dHR/(Cpa+Cpb)
    ca = cA0*(1-x)*T0/T
    cb = ca
    # cc = cA0*(x)*T0/T
    r = k(T)*ca*cb
    vol = FA0*x/r
    # eb = FA0*(Cpa+Cpb-Cpc)+FA0*x*(dHR+dCp*(T-TR))
    return vol
plt.plot(np.linspace(0,1),prob(np.linspace(0,1)))
plt.ylim(0,20)
plt.grid()
plt.show()
# sol = opt.fsolve(prob,[.9,500])
# print(sol)

ca = cA0*(1-.9)*T0/500

v = FA0*.9/k(500)/ca**2

# print(dCp)
T = T0-.9*dHR/(Cpa+Cpb)
print(T)