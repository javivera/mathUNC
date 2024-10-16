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

def test_sollu():
    A = np.array([
        [3, 1, 1],
        [2, 6, 1],
        [1, 1, 4],
    ], dtype="float"
    )
    b = np.array([5, 9, 6], dtype="float")
    print(sollu(A, b)) # Nos deberia dar [1, 1, 1]

test_sollu()
