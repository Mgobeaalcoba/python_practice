# Para realizar busqueda binaria el pre requisito sine qua non es que nuestro universo de busqueda esté ordenado. 
# Mi propia solución: 

objetivo = int(input("Escoge un entero: "))

respuestas_posibles = [x for x in range(1, objetivo//2 + 1)]

respuesta = 0

print(f'Las respuestas posibles son: {respuestas_posibles}')

while (respuesta ** 2) != objetivo and len(respuestas_posibles) > 1:
    
    respuesta = respuestas_posibles[len(respuestas_posibles)//2]
    print(f'La respuesta aproximada sería: {respuesta}')

    if (respuesta ** 2) > objetivo:
        respuestas_posibles = respuestas_posibles[:len(respuestas_posibles)//2]
        print(f'Las proximas respuestas posibles son: {respuestas_posibles}')
    else:
        respuestas_posibles = respuestas_posibles[len(respuestas_posibles)//2:]
        print(f'Las proximas respuestas posibles son: {respuestas_posibles}') 

if (respuesta ** 2) == objetivo: 
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'El numero {objetivo} no tiene raiz cuadrada entre los enteros')