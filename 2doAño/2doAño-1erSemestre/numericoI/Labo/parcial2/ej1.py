import pandas as pd 
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.interpolate import lagrange
import numpy as np

def dataPipeline():
    data = pd.read_csv('irma.csv',header=None)
    tiempo = list(data.iloc[:,0])
    for j in range(len(tiempo)):
        tiempo[j] = int(str(tiempo[j]))

    long = data.iloc[0:,1]
    lat = data.iloc[0:,2]

    return data,tiempo,lat,long

data,tiempo,lat,long = dataPipeline()

lat_t_spline = CubicSpline(tiempo,lat)
long_t_spline = CubicSpline(tiempo,long)
lat_t_lagrange = lagrange(tiempo,lat)
long_t_lagrange = lagrange(tiempo,long)

# ------ Parte a ------
plt.scatter(long,lat)
plt.xlabel("Longitud")
plt.ylabel("Latitud")
plt.show()

# ------ Parte b ------
# No me queda claro que hacer cuando dice "Estimar longitud y latitud cada una hora"
# Obviamente con spline o lagrange solo evaluando podria obtener aproximaciones cada 
# una hora , pero no llego a compender que se espera que haga con esas aproximaciones
# quizas seria usar como dominio aproximaciones cada una hora 
domain = np.arange(tiempo[0],tiempo[-1],0.1) # que seria cambiar aca el 0.1 por 1

plt.scatter(tiempo,lat)
plt.plot(domain,lat_t_spline(domain),label="Spline")
plt.plot(domain,lat_t_lagrange(domain),label="Lagrange")
plt.legend(loc='best')

plt.show()

plt.scatter(tiempo,long)
plt.plot(domain,long_t_spline(domain),label="Spline")
plt.plot(domain,long_t_lagrange(domain),label="Lagrange")
plt.legend(loc='best')

plt.show()
