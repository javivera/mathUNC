from labo2 import rbisec
import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    def g(y):
        return y - math.exp(-1*(1-x*y)**2)
    return g

a = [j for j in np.arange(0,5,0.2)]
raizg = []

for x in a:
    g = f(x)
    
    hx,hg = rbisec(g, [-10,10], 10e-10, 500)
    raizg.append(hx[-1])

plt.plot(a,raizg)
plt.scatter(a,raizg)
plt.show()
    