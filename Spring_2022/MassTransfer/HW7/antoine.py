def antoine( a, T ):
    #
    # Ps = antoine( a, T )
    #
    # Uses Antoine's equation to obtain the vapor pressure of a substance given
    # the coefficients of the equation:
    #  Ps = a1 - a2/(a3+T)
    #
    # INPUTS:
    #  a - the antoine coefficients with coeffients in columns and species in
    #      rows. Typically with T in Celsius and P in mmHg.
    #  T - the temperature to evaluate the vapor pressure at.  Typically in C
    #
    # OUTPUT:
    #  Ps - row vector of species vapor pressures at the specified temperature,
    #       typically in mmHg.
    #
    # The units depend on the units used for the coefficients.  The user is
    # responsible for maintaining consistency with units.  Customarily,
    # coefficients are supplied for pressure in mmHg and T in Celsius.

    Ps = 10.0**( a[:,0]-a[:,1] / ( a[:,2] + T ) )
    return Ps
