import numpy as np
import matplotlib.pyplot as plt

L = 0.1                     #m
Ts1 = 584.7                             #k
Ts2 = 465.3                 #k
T0 = 300                    #k
ro = 1150                   #kg/m3
cp = 468                    #J/kg/k
k = 6.4                     #w/m/k
tfin = 600                   #sec

n = 10                      #number of nodes
dx = L/n                    #
alpha = k/ro/cp             #
dt = 1

x = np.linspace(dx/2,L-dx/2,n)

T = np.ones(n)*T0
dTdt = np.empty(n)
t = np.arange(0,tfin,dt)
# q2 = np.empty(n)

for i in range(1,len(t)):
    
    for j in range(1,n-1):
        dTdt[j] = alpha*(T[j+1]-2*T[j]+T[j-1])/dx**2
        # q2[j] = -k*dTdt[j]
    dTdt[0] = alpha*(T[1]-2*T[0]+Ts1)/dx**2
    # q2[0] = -k*dTdt[0]
    dTdt[n-1] = alpha*(Ts2-2*T[n-1]+T[n-2])/dx**2
    # q2[n-1] = -k*dTdt[n-1]
    T = T+dTdt*dt
    if T[0] >= 550:
        if T[0] < 550.2:
            print(T[0],i)
    # plt.cla()
plt.plot(x,T)
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (k)')

plt.pause(0.0001)
plt.title('T(x) at 600 sec')
plt.grid()
plt.savefig('600sec.png')
plt.show()




