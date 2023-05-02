## Caja negra es una forma de hacer Testing en Python. 

import unittest

def suma(n1,n2):
    return n1+n2

class CajaNegraTest(unittest.TestCase):
    
    # Los metodos de la clase CajaNegraTest deben comenzar con la palabra test para
    # ejecutarse al correr unittest.main():
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1,num_2)

        self.assertEqual(resultado, -17)


if __name__ == '__main__':
    unittest.main()

# Modificando el codigo en función de los resultados de los test es que vamos depurando nuestro codigo para dejarlo listo. 


