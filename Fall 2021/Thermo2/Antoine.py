#Toluene

a = 6.95087
b = 1342.31
c = 219.187

def antoine(a,b,c,T):                                       ###returns Psat at given T (mmHg)
    logP = a - b/(T+c)
    return 10**logP

kPa = antoine(a,b,c,75)*.133322
print(kPa)
print(.7*kPa/30)
