from scipy.special import erfinv
import numpy as np

l = 40
v = 40/60
tmax = 100
sigTmax = 14
y1 = .9

t2 = np.sqrt(2)*sigTmax*erfinv(2*y1-1)+tmax

sig1 = sigTmax/tmax
v2 = 60/60

sig2 = sig1*np.sqrt(v2)/np.sqrt(v)


sig = 