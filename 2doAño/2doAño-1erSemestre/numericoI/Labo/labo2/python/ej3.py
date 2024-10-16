from labo2 import rnewton


def ej3labo(x):
    return (pow(x, 3.0) - 8.0, 3.0 * pow(x, 2.0))

rnewton(ej3labo, -20.0, 10.0e-4, 50)



