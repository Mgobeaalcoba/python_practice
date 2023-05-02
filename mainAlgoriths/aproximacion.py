## Existe un verdadero trade off entre rapidez y precisión. Podemos ser rapidos pero no precisos o precisos pero no rapidos...
#  vamos a buscar la "raiz cuadrada aproximada" de cada numero, incluidos flotantes para los que no tienen una raiz cuadrada entera: 

import time

# Guardo el momento de inicio del algoritmo:

inicio = time.time()

objetivo = int(input("Escoge un numero: "))

# Definimos nuestro epsilon, es decir, que tan precisos queremos ser. A mayor epsilon, menor tiempo pero menor precisión y viceversa

epsilon = 0.01

# Definimos que tanto queremos aproximarnos en cada paso: 

paso = epsilon**2 # epsilon al cuadrado es mas chico que epsilon, tiene mas ceros detras de la coma. 

# respuesta va a contener la respuesta una vez que terminemos nuestras iteraciones: 

respuesta = 0.0

# iteraciones:

iter = 0

# la segunda condición simplemente nos proteje contra numeros negativos si es que el usuario inserta uno: 
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    # Usamos print statement para ver como evoluciona nuestra variable que evoluciona a cada iteración
    # print(f'Operación: {abs(respuesta**2 - objetivo)} / Respuesta: {respuesta}')
    respuesta += paso
    iter += 1

# Guardo el final de mi algoritmo: 
fin = time.time()

# Calculo el tiempo tardado:
tiempo_total = fin - inicio

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raiz cuadrada de {objetivo}. Se realizaron {iter} iteraciones. Se tardo {round(tiempo_total,1)} segundos.')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}. Se realizaron {iter} iteraciones. Se tardo {round(tiempo_total,1)} segundos.')

