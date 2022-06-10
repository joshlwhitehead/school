import numpy as np

R = 8.314                                                       #J/molK

#n-butane
a = 9.487                                                 
b = 0.331
c = -1.11e-4
d = -2.82e-9

t1 = 271
t2 = 386.98

p1 = .1
p2 = 2

def dH(a,b,c,d,t1,t2):
    intcp = a*(t2-t1) + b/2*(t2**2-t1**2) + c/3*(t2**3-t1**3) + d/4*(t2**4-t1**4)
    return intcp                                                                            ###J/mol
# print(dH(-4.224,0.3063,-1.586e-4,3.215e-8,105+273.15,190+273.15))

def dS(a,b,c,d,t1,t2,p1,p2):
    term1 = a*np.log(t2/t1) + b*(t2-t1) + c/2*(t2**2-t1**2) + d/3*(t2**3-t1**3)
    term2 = R*np.log(p2/p1)
    return term1-term2                                                                      #J/mol                   

s1 = -82.634
s2 = -6.28419

print(s2-s1+dS(a,b,c,d,t1,t2,p1,p2))


h1 = -22534
h2 = -3374.43   

# print(dS(a,b,c,d,t1,t2,p1,p2))
print(h2-h1+dH(a,b,c,d,t1,t2))