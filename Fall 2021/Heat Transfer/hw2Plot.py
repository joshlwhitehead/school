import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(.02,.3)



def T(r):
    eq = 120 + 5.5 * np.log(r)
    return eq

def q2(r):
    eq = -2* 5.5 / r
    return eq

def q(r):
    eq = 2 * np.pi * r * q2(r)
    return eq
def plot1():
    plt.plot(x,T(x),label='T(r) (C)')
    plt.plot(x,q2(x),label="q_r'' (W/m^2)")
    plt.plot(x,q(x),label='q_r (W)')
    plt.grid()
    # plt.title()
    plt.legend()
    plt.xlabel('Radius (m)')
    plt.savefig('HW2_2_plot.png')



def plot(name):
    plt.plot(x,q2(x))
    plt.grid()
    plt.title('Temperature Profile (HW6.2)')
    plt.ylabel('Temperature (C)')
    plt.xlabel('Radius (m)')
    plt.savefig(name)
plot("t.png")