# ejemplo de prueba unitaria simple
suma = lambda x, y: x + y
assert suma(2,2) == 4
# si no hay errores es porque funciona bien mi func
# si modifico mi func como lo hice arriba me arroja 
# un assertion error. 

# yo mismo puedo lanzar excepciones: 
age = 10
if age < 18:
    raise Exception('No se admiten menores de edad')
# las excepciones detienen el programa. 