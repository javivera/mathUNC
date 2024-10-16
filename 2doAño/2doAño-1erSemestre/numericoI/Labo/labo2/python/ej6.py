from labo2 import ripf

a = ripf(lambda x: 2**(x-1), 1.9, 10e-5, 100)
print(a)
print(a[-1])


