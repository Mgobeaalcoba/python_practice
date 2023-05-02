## Reto: Componentizar los programas para hallar la raiz cuadrada y ofrecerle al usuario la posibilidad de elegir como quiere hacerlo. 

import time

def aproximación(number):
    mensaje = ""
    inicio = time.time()
    objetivo = number
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    iter = 0
 
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
        iter += 1

    fin = time.time()
    tiempo_total = fin - inicio

    if abs(respuesta**2 - objetivo) >= epsilon:
        mensaje = f'No se encontró la raiz cuadrada de {objetivo}. Se realizaron {iter} iteraciones. Se tardo {round(tiempo_total,1)} segundos.'
    else:
        mensaje = f'La raiz cuadrada de {objetivo} es {respuesta}. Se realizaron {iter} iteraciones. Se tardo {round(tiempo_total,1)} segundos.'

    return mensaje

def enumeracion(number):
    mensaje = ""
    inicio = time.time()
    objetivo = number
    respuesta = 0
    iter = 0

    while respuesta**2 < objetivo:
        respuesta += 1
        iter += 1

    fin = time.time()
    tiempo_total = fin - inicio

    if respuesta**2 == objetivo:
        mensaje = f'La raiz cuadrada de {objetivo} es {respuesta}. Se realizaron {iter} iteraciones. Se tardo {round(tiempo_total,1)}'
    else:
        mensaje = f'{objetivo} no tiene una raiz cuadrada exacta. Se realizaron {iter} iteraciones. Se tardo {round(tiempo_total,1)}'

    return mensaje

def busquedaBinaria(number):
    mensaje = ""
    inicio = time.time()
    objetivo = number
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    iter = 0

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
        iter += 1

    fin = time.time()
    tiempo_total = fin - inicio

    mensaje = f'La raiz cuadrada de {objetivo} es {respuesta}. Se realizaron {iter} iteraciones. Se tardo {round(tiempo_total,1)}'
    return mensaje

def run():
    number = int(input("Ingrese el numero que quiere hallar la raiz cuadrada: "))
    option = int(input("Si quiere hallar la raiz por aproximación presione 1, si quiere hallarla por enumaración presione 2, si quiere hallarla por busqueda binaria presione 3: "))

    while option not in (1,2,3):
        option = int(input("Opción invalida. Por favor seleccione un numero del 1 al 3"))

    if option == 1:
        message = aproximación(number)
    elif option == 2:
        message = enumeracion(number)
    else:
        message = busquedaBinaria(number)
    
    print()
    print("*" * 20)
    print(message)
    print("Gracias por usar nuestro programa!!!")
    print("*" * 20)
    print()

if __name__ == "__main__":
    run()
