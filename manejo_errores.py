# los errores se manejan con try except

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)
finally:
    print("Hola")

# al encerrar mi error en un try el programa sigue. Y puedo
# hacer tracking de mis errores para ver donde está fallando

print("Hola 2")

# las pruebas de tipo assert también las puedo capturar

try:
    assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
    print(error)
finally:
    print('Asi se manejan los errores en Python')

# puedo tambien capturar distintos tipos de errores todos juntos:

try:
    print(0/0)
    assert 1 != 1, 'Uno no es igual que uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error: 
    print(error)

print("Hola")