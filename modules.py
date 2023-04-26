# Que es un modulo en Python? 
# Cualquier archivo que termine en ".py"

# paquete para visualizar datos de nuestro sistema
import sys
print(sys.path)

# paquete para trabajar con regex:
import re
text = "Mi numero de telefono es el 11 27475569 y mi dirección es El Delta 1740"
# Quiero quedarme solo con los numeros de mi text
result = re.findall('[0-9]+', text) # El + indica que no se quede solo con 1. Sino con todos los que coincidan
print(result) # Lo devuelve como lista: ['11', '27475569', '1740']

# paquete para manejar horas y fechas
import time
timestamp = time.time()
print(timestamp) # Imprime hora en float: 1682452882.9777968
local = time.localtime()
result = time.asctime(local)
print(result)
# Tambien lo podemos hacer mas pythonico en 1 sola linea: 
print(time.asctime(time.localtime()))
print(time.localtime())

# paquete para manejar listas:
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter) # Imprime un dict con la frecuencia de cada uno de los numeros
# Counter({1: 4, 2: 2, 3: 2, 4: 1, 5: 1, 21: 1})

# Yo puedo guardar mis modulos en archivos aparte y luego acceder a ellos desde acá: 
import mod_prueba
print(mod_prueba.saludar(mod_prueba.myName))
# Así se modulariza nuestra aplicación. Separando funciones, clases, variables, etc en archivos distintos. 

# Los modulos se pueden llamar con import o como scripts... ¿Como es esto? 
# Si no modularizo mis archivos, al solo llamarlos desde otro script se
# comienzan a ejecutar. Por eso lo ideal es que nuestro codigo esté dentro
# de funciones. 
