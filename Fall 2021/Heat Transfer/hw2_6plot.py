import matplotlib.pyplot as plt
import numpy as np

def T(r):
    eq = (200-50) / np.log(.1/.5) * np.log(r/.5) + 50
    return eq
def q2(r):
    eq = -2.4 * -93.2002 / r
    return eq
def q(r):
    eq = q2(r) *2*np.pi*r*10
    return eq


x = np.linspace(.1,.5)
print(q(x))


plt.plot(x,q2(x))
plt.grid()
plt.title('Heat Flux (HW6.6)')
plt.xlabel('Radius (m)')
plt.ylabel('Flux (W/m^2)')
plt.savefig('q2_6.png')