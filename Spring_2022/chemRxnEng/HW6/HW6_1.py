import numpy as np
import scipy.integrate as inte
import matplotlib.pyplot as plt

Ea = 500                                #j/mol
k_arr = .0055                           #L/mol/sec
T_arr = 300                             #k
R = 8.314                               #j/mol/k
V = 150                                 #L
cp = 150                                #j/mol/k
dHR = -7000                             #j/mol
dcp = 0
F0 = 5                                  #mol/s
v0 = 50                                 #L/sec
yA0 = .2
yB0 = .6
yC0 = .2
T0 = 500                                #k
eps = yA0*(1-2-1)
thetA = 1
thetB = yB0/yA0
thetC = yC0/yA0
FA0 = F0*yA0
thet = np.array([thetA,thetB,thetC])
cA0 = FA0/v0


A = k_arr/np.exp(-Ea/T_arr/R)

def k(temp):
    return A*np.exp(-Ea/R/temp)

def mass(x,V):
    T = T0-x*dHR/sum(thet)/cp
    

    cB = cA0*(thetB-2*x)*T0/T/(1+eps*x)
    
    dxdv = k(T)*cB**2/FA0
    return dxdv

sol = inte.odeint(mass,0,np.linspace(0,V))

print(sol[-1][0])
print(T0-sol[-1][0]*dHR/sum(thet)/cp)

# plt.plot(sol)
# plt.show()


print(A)

def prob(V,x):
    T = 600
    T0 = T+x*dHR/sum(thet)/cp
    cb = cA0*(thetB-2*x)*T0/(1+eps*x)/T
    
    dvdx = FA0/k(T)/cb**2
    return dvdx

sol = inte.odeint(prob,0,np.linspace(0,.95))
plt.plot(np.linspace(0,.96),sol)
plt.show()
print(np.linspace(0,.95)[-1],sol[-1][0])
T0 = 600+.95*dHR/sum(thet)/cp
print(T0)


