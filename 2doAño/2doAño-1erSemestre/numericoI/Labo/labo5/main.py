import math
import numpy as np

def f (x):
    return x*math.exp(-x)

def simpson(f,i):
    cant_intervalos = 3
    l = 0
    suma_final=0 
    while l < 10:# error > 10e-5:
        dm = np.linspace(i[0],i[1],cant_intervalos)
        h = (dm[2]-dm[0])/6
        suma = 0
        for j in range(2,cant_intervalos,2):
            suma += h*(f(dm[j-2]) + 4*f(dm[j-1]) + f(dm[j]))
        l+=1
        suma_final = suma
        cant_intervalos *=2
    print(suma_final)
    return suma_final
    
simpson(f,[0,1])
