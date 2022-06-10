import numpy as np
import matplotlib.pyplot as plt



T = [300,350,400,450,500]
T1 = [300,350,400,450]
isopentane = [0.097607,0.42178,1.241833,2.894625]
toluene = [.004362,.035032,.156578,.48456,1.179623]
methylcyclohexane = [.007131,.049252,.198638,.572401,1.324834]
butanol = [.00156,.021843,.138834,.541695,1.55029]
water = [.003001,.038553,.238663,.928862,2.66311]

iso1 = [10.0277,14.63,20.11,26.385,33.358]
tol1 = [3.092896,5.2177,8.089357,11.746,16.19369]
meth1 = [2.05e-5,.000137,.000525,.00142,.003059]
but1 = [6.92204,13.35895,23.07139,36.59395,54.299]
wat1 = [8.950459,16.97813,29.10978,46.124,68.63743]



plt.plot(T1,isopentane,label='Isopentane PR')
plt.plot(T,toluene,label='Toluene PR')
plt.plot(T,methylcyclohexane,label='Methylcyclohexane PR')
plt.plot(T,butanol,label='Butanol PR')
plt.plot(T,water,label='Water PR')
plt.plot(T,iso1,'o',label='Isopentane Antoine')
plt.plot(T,tol1,'v',label='Toluene Antoine')
plt.plot(T,meth1,'^',label='Methylcyclohexame Antoine')
plt.plot(T,but1,'p',label='Butanol Antoine')
plt.plot(T,wat1,'>',label='Water Antoine')
plt.grid()
plt.legend()
plt.ylabel('Pressure (MPa)')
plt.xlabel('Temperature (K)')
plt.title('Vapor Pressure')

plt.savefig('hw4.png')