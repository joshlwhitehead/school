# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:24:55 2020

@author: joshl
"""

###IMPORTS###
import matplotlib.pyplot as plt
import numpy as np


###CONSTANTS###
a = -500    #kPa/m**3
b = 500     #kPa
V_1 = .8    #m**3
V_2 = .10   #m**3
vol = np.linspace(0,V_1+.1,1000)    #create array of indep. variable values




###FUNCTIONS###
def P(V):
    return a*V+b    #P=aV+b as per prompt (P vs. V)


###CALCULATE###

A_a = .5*(np.abs(V_2-V_1))*np.abs(P(V_1)-P(V_2))  #area of top portion (triangle)
A_b = (np.abs(V_2-V_1))*P(V_1)  #area of bottom portion (rectangle)
print(A_b)
print(np.average(P(vol)))


###PLOT###
plt.close('all')

plt.plot(vol,P(vol),lw=5)
plt.hlines(100,V_1,V_2,linestyles='dashed',lw=5)
plt.title('Compression of a Gas',size=40)
plt.text(.25,250,'a',size=40)
plt.text(.45,50,'b',size=40)
plt.text(.75,400,'Work=Area(a)+Area(b)',size=30)
plt.xlabel('Volume (m$^3$)',size=30)
plt.ylabel('Pressure (kPa)',size=30)
plt.tick_params(labelsize=30)
plt.xlim(V_1,V_2)
plt.ylim(0,b)
plt.grid()

plt.show()