from labo2 import rbisec
import math
import numpy as np
import matplotlib.pyplot as plt


def fun_lab2ej2a(x):
    return 2*x - math.tan(x)

def fun_lab2ej2b(x):
   return x**2 - 3

#hx,hf = rbisec(fun_lab2ej2a,[0.8,1.4],1e-5,100)
hx,hf = rbisec(fun_lab2ej2a,[0,2],1e-5,100)
hx1,hf1 = rbisec(fun_lab2ej2a,[4,6],1e-5,1000)

#print(hx)
#print(hf)
#print("La solucion es:", hx[-2])

dominio=[j for j in np.arange(0,10,0.05)]
evaluaciones = [fun_lab2ej2a(j) for j in np.arange(0,10,0.05)]

# Data for plotting

plt.scatter(hx, hf)
plt.scatter(hx1, hf1)
plt.plot([-1,10],[0,0])
plt.plot(dominio,evaluaciones,color='black')
plt.show()
 