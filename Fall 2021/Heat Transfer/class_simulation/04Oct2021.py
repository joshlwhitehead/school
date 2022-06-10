import numpy as np
import matplotlib.pyplot as plt
################# CONSTANTS ######################3
T1 = 50                         #C
T2 = 100                        #C
T0 = 20             
L = 0.1                                 #m

n = 10          #nodes
dx = L/n
k = 0.2         #w/m/k
cp = 2000       #J/kg/k
ro = 750        #kg/m3
A = 1           #corss section area (m)
dt = 10         #sec

tFin = 3600*10

################## ARRAYS   ######################
x = np.linspace(dx/2,L-dx/2,n)
T = np.ones(n)*T0
dTdt = np.empty(n)

qIn = np.empty(n)
qOut = np.empty(n)

t = np.arange(0,tFin,dt)
plt.figure()

for i in range(1,len(t)):
    qIn[0] = -k * (T[0]-T1) / (dx/2) * A
    qIn[1:n] = -k * (T[1:n]-T[0:n-1]) / (dx/2) * A
    
    qOut[0:n-1] = -k * (T[1:n]-T[0:n-1]) / (dx/2) * A
    qOut[n-1] = -k * (T2-T[n-1]) / (dx/2) * A

    dTdt = (qIn-qOut)/(ro*cp*A*dx)
    T = T + dTdt*dt
    # plt.cla()

    plt.plot(x,T)
    
    # plt.pause(.0000000001)
plt.show()
    
