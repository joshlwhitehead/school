import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,.2,.4,.6,.65,.7,.75,.8,.85,.9])
r = np.array([2,2.73,4.29,10,10,10,6.67,5,4,3.33])/60
FA0 = 1
def full():
    plt.plot(x,r,'o')
    plt.title('Reaction Rate')
    plt.xlabel('X')
    plt.ylabel(''.join(['-$r_B$ ','(',r'$\frac{mol}{L*sec}$',')']))
    plt.grid()
    plt.savefig('HW1_2_plot')


def part():

    plt.plot(x[:4],FA0/r[:4])
    plt.title('Reaction Rate')
    plt.xlabel('X')
    plt.grid()
    plt.ylabel(''.join([r'$\frac{F_{A_0}}{-r_B}$',' (',r'$\frac{mol}{L*sec}$',')']))
    plt.savefig('HW1_2_plot2')
    
part()
full()

