# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:09:11 2020

source code from http://firsttimeprogrammer.blogspot.com/2014/09/generate-slope-fields-in-r-and-python.html
edited by: joshl
"""

import numpy as np
from matplotlib import pyplot as plt

left = -4
right = 4
bottom = -4
top = 4

# Differential equation
def diff(x,y):
    return y-np.sin(x)

x = np.linspace(left,right,20)
y = np.linspace(bottom,top,20)
plt.close('all')

# use x,y
for j in x:
    for k in y:
        slope = diff(j,k)
        domain = np.linspace(j-.2,j+.2,2)   #adjust j-x to change length of slope dash
        def fun(x1,y1):
            z = slope*(domain-x1)+y1
            return z
        plt.plot(domain,fun(j,k),solid_capstyle='projecting',solid_joinstyle='bevel')
plt.title("Slope field P'",size=30)
plt.tick_params(labelsize=30)
plt.xlabel('t',size=30)
plt.ylabel('P',size=30)
plt.xlim(left,right)
plt.ylim(bottom,top)

plt.grid(True)
plt.show()

