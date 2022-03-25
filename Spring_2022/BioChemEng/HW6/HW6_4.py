import numpy as np
import matplotlib.pyplot as plt

l = np.linspace(0,1)


def S(D,a,y):
    return np.exp(a/D*((y**2)/2-y))

plt.plot(l,S(2,2,l),label='D=2,a=2')
plt.plot(l,S(20,2,l),label='D=20,a=2')
plt.plot(l,S(2,.02,l),label='D=2,a=0.02')
plt.grid()
plt.xlabel('Length (cm)')
plt.ylabel('Substrate Concentration')
plt.title('Substrate Concentration')
plt.legend()
plt.savefig('HW6_4b')
