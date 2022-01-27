import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,.2,.4,.6,.65,.7,.75,.8,.85,.9])
r = np.array([2,2.73,4.29,10,10,10,6.67,5,4,3.33])/60
FA0 = 1
a,b = np.polyfit(x[-5:],FA0/r[-5:],1)
# print(a,b)
def full():
    plt.figure()
    plt.plot(x,r,'o')
    plt.title('Reaction Rate $X_A$: [0,0.9] (Plot A)')
    plt.xlabel('$X_A$')
    plt.ylabel(''.join(['-$r_A$ ','(',r'$\frac{mol}{L*sec}$',')']))
    plt.grid()
    plt.savefig('HW2_2_total')


def firstPart():
    plt.figure()
    plt.plot(x[:4],FA0/r[:4],'o')
    # plt.plot(x[:4],a*x[:4]+b,label='fit')
    plt.title('Reaction Rate $X_A$: [0,0.6] (Plot B)')
    plt.xlabel('$X_A$')
    plt.grid()
    # plt.legend()
    # plt.text(.1,17,''.join([r'$\frac{F_{A_0}}{-r_A}$ = ',str(round(a,1)),'X+',str(round(b,1))]))
    plt.ylabel(''.join([r'$\frac{F_{A_0}}{-r_A}$',' (L)']))
    plt.savefig('HW2_2_first')
    


def lastPart():
    plt.figure()
    plt.plot(x[-5:],FA0/r[-5:],'o',label='data')
    plt.plot(x[-5:],a*x[-5:]+b,label='fit')
    plt.title('Reaction Rate $X_A$: [0.7,0.9] (Plot C)')
    plt.xlabel('$X_A$')
    plt.grid()
    plt.legend()
    plt.text(.825,12,''.join([r'$\frac{F_{A_0}}{-r_A}$ = ',str(round(a,1)),'$X_A$+',str(round(b,1))]))
    plt.ylabel(''.join([r'$\frac{F_{A_0}}{-r_A}$',' (L)']))
    plt.savefig('HW2_2_last')

def fullConfig():
    plt.figure()
    plt.plot(x,r,color='black')
    plt.vlines(.6,r[0],r[3])
    plt.hlines(r[0],0,.6)
    plt.vlines(.85,r[0],r[-2],color='orange')
    plt.hlines(r[0],.6,.85,color='orange')
    plt.hlines(r[-2],.6,.85,color='orange')
    plt.text(.65,.05,'CSTR',size=15)
    plt.text(0.4,.05,'PFR',size=15)
    
    plt.title('Reaction Rate $X_A$: [0,0.9] (Plot D)')
    plt.xlabel('$X_A$')
    plt.ylabel(''.join(['-$r_A$ ','(',r'$\frac{mol}{L*sec}$',')']))
    plt.grid()
    plt.savefig('HW2_2_totalConfig')
lastPart()
firstPart()
full()
fullConfig()



print(r)