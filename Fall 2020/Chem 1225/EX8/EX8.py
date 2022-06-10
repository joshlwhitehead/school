# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:10:23 2020

@author: joshl
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('EX8.csv')
vol = data['vol']
ph = data['ph']

vol1 = np.linspace(0,50,231)

def deriv(x,y):
    count = 0
    curv = []
    for i in range(0,231):
        curv.append((y[count+1]-y[count])/(x[count+1]-x[count]))
        count += 1
    curv.append(0)
    return np.array(curv)

plt.close('all')
plt.title('Titration of HAc with NaOH',size=50)
plt.plot(vol,ph,lw=4,label='Titration Curve')
plt.plot(vol,deriv(vol,ph),lw=4,label='1st Derivative')
plt.ylim(0,14)
plt.xlim(0,50)
plt.xlabel('Volume (mL)',size=30)
plt.ylabel('pH',size=30)
plt.xticks(size=30)
plt.yticks(size=30)
plt.legend(prop = {'size':40})
plt.grid()
plt.show()

print(10**-(
        (ph[29]+ph[28])/2))

