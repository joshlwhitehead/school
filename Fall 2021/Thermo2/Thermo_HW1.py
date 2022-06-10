m = 25                              #g
n = m/78                            #mol


gone = -33.92
gtwo = .4739
gthree = -3.017e-4
gfour = 7.13e-8

lone = -6.211
ltwo = 5.65e-1
lthree = -3.141e-4
lfour = 0



tl = 25+273.15
th = 50+273.15
tvap = 80+273.15

dHvap = 30.765                                                                  ###kJ/mol

def intCp(a,b,c,d,t1,t2):
    first = (a*t2 + (b*t2**2)/2 + (c*t2**3)/3 + (d*t2**4)/4)/1000                   ###kJ/mol
    last = (a*t1 + (b*t1**2)/2 + (c*t1**3)/3 + (d*t1**4)/4)/1000
    return first-last

def cp(a,b,c,d,T):
    return a + b*T + c*T**2 + d*T**3



liq1 = .25*n*intCp(lone,ltwo,lthree,lfour,tl,th)
liq2 = .75*n*intCp(lone,ltwo,lthree,lfour,tl,tvap)
vap = .75*dHvap*n
vap1 = .75*n*intCp(gone,gtwo,gthree,gfour,tvap,th)

x = liq1+liq2+vap+vap1
y = x/n

print(x,'\n',y)











