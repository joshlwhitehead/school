import numpy as np
import matplotlib.pyplot as plt

wage = np.linspace(19,30)
# yearsUntilGrad = np.linspace(1,5)


fullYearAt19 = 25000
monthDuringSem = wage*15*4*4
fullYearAtNew = wage*40*4*12
estGradSal = 70000

def shortGrad():
    return fullYearAt19 + 2*monthDuringSem + 2.5*estGradSal

def longGrad(yearsToGrad):
    return yearsToGrad*fullYearAtNew + (4.5-yearsToGrad)*estGradSal

# print(shortGrad()-longGrad(4))
# print(wage*40*4*12)

plt.plot(wage,shortGrad(),label='current')
plt.plot(wage,longGrad(4),label='possible')
plt.legend()
plt.grid()
plt.show()
# plt.plot(yearsUntilGrad,np.ones(len(yearsUntilGrad))*shortGrad(),label='current')
# plt.plot(yearsUntilGrad,longGrad(yearsUntilGrad),label='possible')
# plt.legend()
# plt.grid()
# plt.show()

