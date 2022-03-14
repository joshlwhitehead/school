import numpy as np

tA = 14.325
tB = 432.6
tC = 2.144e6
tD = 26.975/ 365.25
tE = 2.592e5
lamA = np.log(2)/tA
lamB = np.log(2)/tB
lamC = np.log(2)/tC
lamD = np.log(2)/tD
lamE = np.log(2)/tE

def bate(t,NA0,lamA,lamB,lamC,lamD,lamE):
    CA = NA0*lamA*lamB*lamC*lamD/(lamB-lamA)/(lamC-lamA)/(lamD-lamA)/(lamE-lamA)
    CB = NA0*lamA*lamB*lamC*lamD/(lamA-lamB)/(lamC-lamB)/(lamD-lamB)/(lamE-lamB)
    CC = NA0 *lamA*lamB*lamC*lamD/(lamA-lamC)/(lamB-lamC)/(lamD-lamC)/(lamE-lamC)
    CD = NA0*lamA*lamB*lamC*lamD/(lamA-lamD)/(lamB-lamD)/(lamC-lamD)/(lamE-lamD)
    CE = NA0*lamA*lamB*lamC*lamD/(lamA-lamE)/(lamB-lamE)/(lamC-lamE)/(lamD-lamE)

    NC = CA*np.exp(-lamA*t)+CB*np.exp(-lamB*t)+CC*np.exp(-lamC*t)+CD*np.exp(-lamD*t)+CE*np.exp(-lamE*t)
    return NC

print(bate(10000,650,lamA,lamB,lamC,lamD,lamE))
print(lamD,lamE)