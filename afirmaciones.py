## Afirmaciones son herramientas de programación defensiva: 
#  También sirven para debuguear
#  Pueden utilizarse para verificar que los tipos sean correctos en una función.

#  Palabra clave para las afirmaciones: Assert

#  Como funciona, afirmo algo que debe suceder. Si no sucede entonces
#  devuelvo lo que quiera, por ejemplo, un String

#  Devuelven un "Assertion error"

def primera_letra(lista_de_palabra):
    primeras_letras = []

    for palabra in lista_de_palabra:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, "No se permiten str vacios"

        primeras_letras.append(palabra[0])

    return primeras_letras

my_list = ["Hola", "Mariano", "como", "estas", ""]

print(primera_letra(my_list))




