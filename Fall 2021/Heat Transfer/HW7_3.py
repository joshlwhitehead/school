import matplotlib.pyplot as plt
import numpy as np
v = np.linspace(10,100)


ro = .8485
Pr = .689
Ts = 523
Tinf = 300
k = 3.46e-2
mu = 2.34e-5
L=.15

Re = ro*v*1000/3600*L/mu

Nu = .037*Re**(4/5)*Pr**(1/3)

h = Nu*k/L

q1 = 2*h*L*(Ts-Tinf)


plt.plot(v,q1)
plt.title("Heat Rate per Unit Length")
plt.xlabel('Velocity (km/hr)')
plt.ylabel("q' (w/m)")
plt.grid()
plt.savefig('HW7_3')
plt.show()




