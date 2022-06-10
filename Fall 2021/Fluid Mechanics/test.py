import matplotlib.pyplot as plt
import numpy as np

def f(x,si):
    return np.sqrt(2/3*(si+x**2))

indVar = np.linspace(-3,3)



plt.grid()
plt.show()