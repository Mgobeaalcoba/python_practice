# Busqueda binaria para valores flotantes. Mucho mas eficiente que la aproximación. Solo funciona si nuestro conjunto tiene un orden.. 

objetivo = int(input("Escoge un entero: "))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

# Garantizamos que el numero no pueda ser negativo con la variable alto: 
while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}, respuesta**2 - objetivo={respuesta**2 - objetivo}, epsilon={epsilon}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    # En cada iteración hacemos mas pequeño nuestro espacio de busqueda: 
    respuesta = (alto + bajo) / 2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')
