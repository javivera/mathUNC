from typing import Callable


def rbisec(fun,I,err,mit):
    l,r = fun(I[0]),fun(I[1])
    e = I[1] - I[0]
    hx = []
    hf = []
    if l == r:
        print('la funcion podria no tener raiz')
        return None
    for j in range(mit):
        e = e/2
        c = e + I[0]
        w = fun(c)
        hx.append(c)
        hf.append(w)

        if abs(w) < err:
            print(c)
            print('Result error is bounded')
            return hx,hf
        if w*l < 0: # Signos diferentes  
            I[1] = c
            r = w 
        else:
            I[0] = c
            l = w
    print('Max iteration reached')
    print(c)
    return hx,hf

def rnewton(f, x_0, err, mit):
    ev_f = f(x_0)[0]
    ev_fp = f(x_0)[1]
    x_1 = 0.0
    hf = []
    hx = []
    hf.append(ev_f)
    hx.append(x_0)

    if abs(ev_f) < err:
        print("Arrancaste ya con algo cercano a la raiz")
        return (hf, hx)
    
    for _n in range(1, mit):
        x_1 = x_0 - ev_f/ev_fp
        ev_f = f(x_1)[0]
        ev_fp = f(x_1)[1]
        x_0 = x_1

        hf.append(ev_f)
        hx.append(x_0)
        if abs(ev_f) < err:
            print("Bounded error reached")
            print(f"La raiz es {x_0}, el error {ev_f}")
            return (hf, hx)
    
    print("Max iteration reached")
    print(f"La raiz es {x_0}, el error {ev_f}")
    return (hf, hx)

def ripf(f: Callable ,x_0: float,err: float,mit: int) -> list[float]:
    xn = f(x_0)
    hx = [xn]
    xn1 = 0
    i=0
    while i < mit:
        xn1 = f(xn)
        hx.append(xn1)
        if abs(xn1 - xn) < err:
            print('Bounded error reached')
            print(xn1)
            return hx
        xn = xn1
        i+=1

    print('Max iteration reached')
    print(xn1)
    return hx

