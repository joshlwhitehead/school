frac = [0,.2,.4,.6,.8,1]

bp = [48.75,75.15,101.5,127.9,154.3,180.7]
dp = [48.8,57.1,68.9,86.8,117.2,180.7]




import matplotlib.pyplot as plt


plt.plot(frac,bp,label='Bubble')
plt.plot(frac,dp,label='Dew')
plt.grid()
plt.legend()
plt.title('Pxy Mehtanol, n-Propanol @ 80C')
plt.ylabel('Pressure (kPa)')
plt.xlabel('x1, y1 (Methanol)')
plt.savefig('hw6.png')