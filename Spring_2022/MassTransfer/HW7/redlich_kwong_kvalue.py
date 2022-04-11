from warnings import warn
import numpy as np

def redlich_kwong_kvalue( Tc, Pc, T, P, x, y, *acentric ):
    #---------------------------------------------
    # K = redlich_kwong_kvalue( Tc, Pc, T, P, x, y )
    # K = redlich_kwong_kvalue( Tc, Pc, T, P, x, y, w )
    #
    # INPUTS:
    #  Tc - vector of critical temperatures (K) for each species
    #  Pc - vector of critical pressure (Pa) for each species
    #  T  - temperature (K)
    #  P  - pressure (Pa)
    #  x  - liquid phase mole fractions
    #  y  - vapor  phase mole fractions
    #  w  - accentric factor (OPTIONAL). If provided, Soave-Redlich-Kwong is used.  Otherwise, Redlich-Kwong is used.
    #
    # OUTPUT:
    #  K - vector of equilibrium coefficients (K values)
    #
    # Author: James C. Sutherland
    #---------------------------------------------

    R = 8.3144  # Gas constant, (m ^ 3 Pa) / (mol K)

    #---------------------------------------------
    # Set the species parameters, ai, bi, Ai, Bi


    if acentric:
      # we have the accentric factor, so use it in determining the parameters
      # for the EOS (Soave-Redlich-Kwong)
      w = acentric[0];
      f  = 0.48 + 1.574*w - 0.176*w**2
      Tr = T/Tc
      a  = 0.42748 * R**2 * Tc**2 *(1+f*(1-np.sqrt(Tr)))**2 / Pc  # Pa-m^6/mol^2
    else:
      # we don't have the accentric factor, so revert to the Redlich-Kwong EOS
      a = 0.42748 * R**2 * Tc**2.5/(Pc*T**0.5)  # Pa-m^6/mol^2

    b = 0.08664 * R * Tc/Pc  # m^3/mol
    A = a*P/(R*T)**2          # no units
    B = b*P/(R*T)             # no units
    #---------------------------------------------

    #---------------------------------------------
    # Mixing rules to get mixture parameters for the vapor and liquid phases.
    # it is important that the x, y, and a vectors are row vectors here so that
    # we can use "sum" properly.
    amixV = sum(sum( np.outer(y,y) * np.sqrt( np.outer(a,a) ) ))
    bmixV = sum(y*b)
    AmixV = amixV*P/(R*T)**2
    BmixV = bmixV*P/(R*T)

    amixL = sum(sum( ( np.outer(x,x) * np.sqrt( np.outer(a,a) ) ) ))
    bmixL = sum(x*b)
    AmixL = amixL*P/(R*T)**2
    BmixL = bmixL*P/(R*T)
    #---------------------------------------------

    #---------------------------------------------
    # calculate the compressibility factor for the vapor and liquid phases
    # from the Redlich-Kwong equation of state.
    # Put this in polynomial form to get all of the roots of the polynomial.
    vcoefs = np.array([1, -1, (AmixV-BmixV-BmixV**2), -(AmixV*BmixV)])
    lcoefs = np.array([1, -1, (AmixL-BmixL-BmixL**2), -(AmixL*BmixL)])
    ZL = min(np.roots(lcoefs))  # liquid Z value
    ZV = max(np.roots(vcoefs))  # vapor  Z value

    if abs( ZL - ZV ) < 1e-4:
      warn('It appears that the mixture is above its critical point!')
    #---------------------------------------------


    #---------------------------------------------
    # calculate partial molar fugacity coefficients and then the K values
    phiV = np.exp( (ZV-1)*B/BmixV - np.log(ZV-BmixV) - AmixV/BmixV*(2*np.sqrt(A/AmixV) - B/BmixV) * np.log(1+BmixV/ZV) )
    phiL = np.exp( (ZL-1)*B/BmixL - np.log(ZL-BmixL) - AmixL/BmixL*(2*np.sqrt(A/AmixL) - B/BmixL) * np.log(1+BmixL/ZL) )

    K = phiL/phiV
    #---------------------------------------------

    return K.real



















# This is intended to test things to ensure that it is working properly.
if __name__ == '__main__':
    from raoult_law_kvalue import raoult_law_kvalue
    from scipy.optimize import newton

    P = 101325  # Pressure in Pa

    propane = [6.80398, 803.810,  246.990]
    benzene = [6.90565, 1211.033, 220.79 ]
    antoineCoefs = np.array( [propane, benzene] )

    z = 0.5

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
    