# Vamos a tratar de estimar si un numero tiene una raiz cuadrada exacta pidiendo ese numero por pantalla: 

objetivo = int(input("Escoge un entero: "))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta.')

