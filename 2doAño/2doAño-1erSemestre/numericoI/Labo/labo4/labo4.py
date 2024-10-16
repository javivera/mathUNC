import random
import math
import matplotlib.pyplot as plt
import numpy as np

def dataGenerator(f,a,b):
    x = []
    fx = []
    j=0
    while j <= 46:
        c = random.uniform(a,b)
        fx.append(f(c))
        x.append(c)
        j += 1

    # plt.scatter(x,fx)
    # plt.show()
    return x,fx

def polyFit(f,d):
    x,fx = dataGenerator(f,d[0],d[1])

    a = np.flip(np.polyfit(x,fx,20))

    x = [j for j in np.arange(d[0],d[1],0.01)]
    # fx = [a[0] + a[1]*j + a[2]*(j**2) + a[3]*(j**3) + a[4]*(j**4) for j in x]
    # print(fx[-1])
    # plt.plot(x,fx)
    fx = []
    for j in x:
        evx = 0
        for i in range(0,len(a)):
            evx += a[i]*(j**i)
            print(i,a[i],j,evx)
        fx.append(evx)

    print(a)
    plt.plot(x,fx)
    plt.show()

polyFit(lambda x : x**2 + 3*x+2,[0,10])


