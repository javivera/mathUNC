import numpy as np
import scipy.linalg as la


def soltrinf(A,b):
    x = np.zeros(len(b))
    for fila in range(len(A)):
        suma = 0
        for columna in range(fila):
            suma += A[fila,columna]*x[columna]

        x[fila] = (b[fila] - suma)/ A[fila,fila]
    return x

def soltrsup (A,b):
    x = np.zeros(len(b))
    for fila in reversed(range(len(A))):
        suma = 0
        for columna in reversed(range(fila+1,len(A))):
            suma += A[fila,columna]*x[columna]

        x[fila] = (b[fila] - suma)/ A[fila,fila]
    return x

def sollu(A,b):
    P,L,U = la.lu(A)
    
    b_tilde = la.inv(P) @ b
    y = soltrinf(L,b_tilde) # esto deberia ser Soltrinf
    x = soltrsup(U,y) # Esto deberia ser soltrSup
    return x

def solluAlt(A,b):
    P,L,U = la.lu(A)
    Linv = la.inv(L)
    b = Linv.dot(b)
    x = soltrsup(U,b)
    return x

def solluAlt2(A,b):
    P,L,U = la.lu(A)
    y = soltrinf(L,b)
    x = soltrsup(U,y)
    return x


x = [-2,0,2,4]
y = [0,-2,1,2]

a = np.polyfit(x,y,2)
def f(x):
    return a[0] + x*a[1] + x*x*a[0]
print(f(5))
b2 = sollu([[f(5),1,1],[1,f(5),1],[1,1,f(5)]],[1,1,1])
b1 = solluAlt2([[f(5),1,1],[1,f(5),1],[1,1,f(5)]],[1,1,1])
print(b1)
print(b2)

