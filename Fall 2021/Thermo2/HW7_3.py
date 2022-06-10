import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(0,1,1000)
x2 = 1-x1

psat1 = 900
psat2 = 600
A = 0.5


gam1 = np.exp(A*(1-x1)**2)
gam2 = np.exp(A*(1-x2)**2)

bub = x1*psat1*gam1 + x2*psat2*gam2
dew = 1/(x1/(psat1*gam1)+x2/(psat2*gam2))

plt.plot(x1,bub,label='Bubble')
plt.plot(x1,dew,label='Dew')
plt.title('A-B Pxy @ 80C')
plt.ylabel('Pressure (mmHg)')
plt.xlabel('xA')
plt.grid()
plt.legend()
plt.savefig('hw7_3plot')
bub = bub.tolist()
print(bub.index(max(bub)))
print(x1[905])
# print(max(dew))