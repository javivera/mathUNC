import matplotlib.pyplot as plt

datos_x = [0,1.5,2,2.9,4,5.6,6,7.1,8.05,9.2,10,11.3,12]
datos_y = [0.1,0.2,1,0.56,1.5,2.0,2.3,1.3,0.8,0.6,0.4,0.3,0.2]

# ------ Parte a ------
plt.plot(datos_x,datos_y)
plt.show()

# ------ Parte b ------
def trapecio_simple(a,b,fa,fb):
    return ((b-a)/2)*(fa+fb)

def trapecio_adaptativo(datos_x,datos_y):
    valor_integral = 0
    for j in range(1,len(datos_x)):
        valor_integral += trapecio_simple(datos_x[j-1],datos_x[j],datos_y[j-1],datos_y[j])
    return valor_integral

# No entiendo bien que metodo deberia ser modificado , en el fondo integrar trapecio compuesto
# es hacer trapecio simple en cada particion, de la forma que lo hice me parece que queda
# claro que esta sucediendo esto, y ademas no hay ninguna problema con la equidistancia de 
# particiones


# ------ Parte c ------
print("La cantidad aproximada de tierra a ser removida es: {} m^3"
      .format(round(trapecio_adaptativo(datos_x,datos_y)*10,2)))

