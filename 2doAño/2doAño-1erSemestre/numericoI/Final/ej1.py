import numpy as np
import matplotlib.pyplot as plt
import math

def rnewton(f, x_0, err, mit):
    ev_f = f[0](x_0)
    ev_fp = f[1](x_0)
    x_1 = 0.0
    hf = []
    hx = []
    hf.append(ev_f)
    hx.append(x_0)

    if abs(ev_f) < err:
        print("Arrancaste ya con algo cercano a la raiz")
        return (hf, hx)
    
    for n in range(1, mit):
        x_1 = x_0 - ev_f/ev_fp
        ev_f = f[0](x_1)
        ev_fp = f[1](x_1)
        x_0 = x_1

        hf.append(ev_f)
        hx.append(x_0)
        if abs(ev_f) < err:
            print("Bounded error reached")
            print(f"La raiz es {x_0}, el error {ev_f} y la cantidad de iteraciones {n}")
            return (hf, hx)
    
    print("Max iteration reached")
    print(f"La raiz es {x_0}, el error {ev_f} y la cantidad de iteraciones {n}")
    return (hf, hx)


def rnewtondelta(f, x_0, err, mit,delta):
    ev_f = f(x_0)
    ev_fp = (f(x_0+delta)-f(x_0))/delta
    x_1 = 0.0
    hf = []
    hx = []
    hf.append(ev_f)
    hx.append(x_0)

    if abs(ev_f) < err:
        print("Arrancaste ya con algo cercano a la raiz")
        return (hf, hx)
    
    for n in range(1, mit):
        x_1 = x_0 - ev_f/ev_fp
        ev_f = f(x_1)
        ev_fp = (f(x_1+delta)-f(x_1))/delta
        x_0 = x_1

        hf.append(ev_f)
        hx.append(x_0)
        if abs(ev_f) < err:
            print("Bounded error reached")
            print(f"La raiz es {x_0}, el error {ev_f} y la cantidad de iteraciones {n}")
            return (hf, hx)
    
    print("Max iteration reached")
    print(f"La raiz es {x_0}, el error {ev_f} y la cantidad de iteraciones {n}")
    print("asd")
    return (hf, hx)

#------ parte b

def graficar():
    dm = np.linspace(0,10,100)
    im = [math.exp(x) -x -2 for x in dm]
    plt.plot(dm,im)
    plt.show()
graficar()

a = rnewtondelta(lambda x : math.exp(x)-x-2,1,1e-6,100,1e-5)
b = rnewtondelta(lambda x : math.exp(x)-x-2,1,1e-6,100,0.001)
c = rnewton([lambda x : math.exp(x)-x-2,lambda x:math.exp(x)-1],1,1e-6,100)
