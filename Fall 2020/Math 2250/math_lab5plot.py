# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:02:32 2020

@author: joshl
"""

import numpy as np
import matplotlib.pyplot as plt

###CONSTANTS###
a = .2009
b = -.5659
c = 1.454

x = np.linspace(0,10,1000)

###FUNCTION###
def p(t):
    return a*np.e**t+b*np.log(t)+c*t
print(p(0.8))


###PLOT STUFFS###
plt.close('all')

plt.plot()
plt.title('Bacterial Growth',size=50)
plt.plot(x,p(x),lw=5)
plt.xlim(0,2)
plt.ylim(0,5)
plt.grid('show')
plt.tick_params(labelsize=30)
plt.xlabel('Time (hr)',size=30)
plt.ylabel('Population (x1000)',size=30)

plt.show()

