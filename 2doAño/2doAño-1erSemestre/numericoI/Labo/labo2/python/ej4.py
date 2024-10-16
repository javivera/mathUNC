from labo2 import rnewton

def cubic(a,x_0):
    return rnewton(lambda x:(x**3-a,3*x**2), x_0, 10e-6, 20)

a,b = cubic(3,7)     
