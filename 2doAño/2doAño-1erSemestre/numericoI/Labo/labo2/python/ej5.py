from labo2 import ripf

a = ripf(lambda x:(x+1)**(1/3), 10000000000000000, 10e-10,100)
print(a)
print(a[-1])



