import numpy as np

UA = 4
Ta = 350
T0 = 300
cpa = 25
cpb = 35
cpc = 60
F = 300

def T():
    T = (UA/F*Ta-cp*T0+sigCp*T0)/(sigCp+UA/F-cp)
    return T

print(T())


Q = F*cp*(T0-T())
Q = UA*(Ta-T())
print(Q)