import numpy as np
import matplotlib.pyplot as plt


k1 = 10
K = .01/.001**2
betaA = 1
betaB = 40
FA0 = 100
v0 = 100*.001
Ac = 2*.01
L = 10*.1
cA0 = FA0/v0

time = np.linspace(0,L/v0)
print(time)


def cA(t):
    c = cA0
    cA = []
    for i in t:
        cA.append(c)
        c = cA0-c*betaA*i
    return cA
plt.plot(cA(time))
plt.show()
