# Pruebas de Caja de Cristal es aquella donde vamos probando todo el flujo del programa. Parte por parte. 

import unittest

def es_mayor_de_edad(edad):
    if edad > 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    # para verificar la def de arriba voy a necesitar dos test. Uno por el flujo if y otro por el flujo else: 

    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado,True)

    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)

if __name__ == "__main__":
    unittest.main()