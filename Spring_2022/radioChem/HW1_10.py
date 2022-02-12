import matplotlib.pyplot as plt
import numpy as np
"""NB = lama/(lamb-lama)na0(e-lamat-e-lambt)"""
lama = np.log(2)/(1101686/3600/24)
lamb = np.log(2)/(145029/3600/24)

def NB(t,NA0,lama,lamb):
    return lama/(lamb-lama)*NA0*(np.exp(-lama*t)-np.exp(-lamb*t))

time = np.linspace(0,100,999)

plt.plot(time,NB(time,1,lama,lamb))
plt.grid()
plt.title(''.join(['Number of Atoms of La']))
plt.xlabel('Time (hrs)')
plt.ylabel(r'$N_{La}$ (atoms)')
plt.savefig('HW1_10_plot')
print(time[NB(time,1,lama,lamb).tolist().index(np.max(NB(time,1,lama,lamb)))])
print(lamb)
