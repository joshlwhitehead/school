"""
written 05Feb2022 for Nucl3100 (Radiation Interactions)
HW 2 problem 7
problem statement is to draw a diagram comparing energy lost in a scattered photon to the 
scattering angle
"""
import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0,np.pi,999)                       #scattering angle (radians)

def percEnergyLost(degree,incedentEnergy):
    return 1 - 1/incedentEnergy/((1-np.cos(degree))/.511+1/incedentEnergy)

for i in np.arange(0,3,.5):
    if i != 0:
        plt.plot(theta*180/np.pi,percEnergyLost(theta,i),label=''.join(['Incident = ',str(i),'MeV']))
plt.legend()
plt.grid()
plt.ylabel('Percent of Energy Lost')
plt.xlabel('Angle of Scattered Photon (degrees)')
plt.xlim(0,180)
plt.title('Compton Scattering')
plt.savefig('HW2_7')