from antoine import antoine
import numpy as np

def raoult_law_kvalue( T, P, a, *gamma ):
    # Calculates the equilibrium coefficient from Raoult's law
    #
    # INPUTS:
    #
    #  T - temperature in Kelvin
    #
    #  P - pressure in Pa
    #
    #  a - Antoine equation coefficients with coefficients for each species in
    #      a row. It is assumed that these are for vapor pressure in mmHg and
    #      temperature in Celsius.  Conversions are performed internally.
    #
    #  gamma - OPTIONAL activity coefficients for use in a modified Raoult's law.
    #
    #
    # OUTPUT:
    #
    #  K - row vector containing the K-valye for each species
    #
    # Author: James C. Sutherland

    ns,nc = a.shape

    K = np.zeros(ns)
    Ps = antoine(a, T - 273.15) * 133.3  # convert mmHg to Pa and T to C
    K = Ps/P
    if gamma:
        K *= gamma

    return K



# This is intended to test things to ensure that it is working properly.
if __name__ == '__main__':
    from scipy.optimize import newton

    P = 101325  # Pressure in Pa

    propane = [6.80398, 803.810,  246.990]
    benzene = [6.90565, 1211.033, 220.79 ]
    antoineCoefs = np.array( [propane, benzene] )

    z = [0.5,0.5] 

    def resfun_bubble( T ):
        return 1 - np.sum( z * raoult_law_kvalue(T,P,antoineCoefs) )

    def resfun_dew( T ):
        return 1 - np.sum( z / raoult_law_kvalue(T,P,antoineCoefs) )

    Tb = newton(resfun_bubble,300)
    Td = newton(resfun_dew,   300)

    if abs( Tb - 248 ) > 0.2:
        print('FAILED.  Expected bubble point temperature of 248.0 but found {:.1f}'.format(Tb))
    if abs( Td - 333.0 ) > 0.2:
        print('FAILED.  Expected dew point temperature of 333.0 but found {:.1f}'.format(Td))


    print('\n\t-> Bubble point: {:.1f} K\n\t-> Dew    point: {:.1f} K'.format(Tb,Td))
