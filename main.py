# Antes de usar un paquete debemos instalarla usando: $ pip install {package_name}/{package_route}

'''
import pkgGobea.mod_1 as mod_1 # Opcion A de importación de paquetes
import pkgGobea.mod_2 as mod_2

print(mod_1.func_1())
print(mod_1.func_2())
print(mod_2.func_3())
print(mod_2.func_4())


from pkgGobea.mod_1 import func_1, func_2 # Opción B de importación de paquetes: 
from pkgGobea.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())


import pkgGobea # Opción C => Para que funcione primero debo especificar el init que voy a importar al importar el package completo

print(pkgGobea.mod_1.func_1())
print(pkgGobea.mod_1.func_2())
print(pkgGobea.mod_2.func_3())
print(pkgGobea.mod_2.func_4())
'''