# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:02:29 2020

@author: joshl
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

na_data = pd.read_csv('EX2_FPD.csv')
time_na = na_data['time']/60
temp_na = na_data['T']

ca_data = pd.read_csv('EX2_FPD.csv')
time_ca = ca_data['time2']/60
temp_ca = ca_data['T2']


plt.close('all')
f, ax=plt.subplots()
plt.title('Freezing Point Depression (NaCl in water)',size=40)
ax.plot(time_na,temp_na,lw=5,label='Freezing Point Depression (NaCl)')
ax.tick_params(labelsize=30)
ax.text(3.2,.5,'Freezing point\nof pure water: 0$^\circ$C',size=20)
ax.text(5.7,-1.2,'Freezing point of\nwater with NaCl: -1.74$^\circ$C',size=20)
plt.xlabel('Time (min)',size=30)
plt.xlim(0,np.max(time_na))
plt.ylabel('Temperature ($^\circ$C)',size=30)
plt.ylim(-2,26)
plt.yticks(np.arange(-2,26,2))
plt.grid()

g, ax=plt.subplots()
plt.title('Freezing Point Depression (Ca(N'+r'$O_3$'+r'$)_2$ in water)',size=40)
ax.plot(time_ca,temp_ca,lw=5)
ax.tick_params(labelsize=30)
ax.text(4.8,.5,'Freezing point\nof pure water: 0$^\circ$C',size=20)
ax.text(7.5,-.7,'Freezing point of water\nwith Ca(N'+r'$O_3$'+r'$)_2$: -1.02$^\circ$C',size=20)
plt.xlabel('Time (min)',size=30)
plt.xlim(0,np.max(time_ca))
plt.yticks(np.arange(-2,26,2))
plt.ylim(-2,26)
plt.ylabel('Temperature ($^\circ$C)',size=30)
plt.grid()



plt.show()