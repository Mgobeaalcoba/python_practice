# Cargo el archivo que quiero leer
file = open('./text.txt')
# Imprimo el archivo completo: 
# print(file.read())
# Itero el archivo por linea: 
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# es similar a operar con next un iterable

# Tambien puedo iterar el archivo con un for: 

for line in file:
    print(line)

# es muy importante cerrar la lectura del archivo para
# no mantener la lectura abierta: 
file.close()

# Existe una sintaxis para iterar un archivo sin necesidad
# de cerrarlo al finalizar la lectura:
with open('./text.txt') as file:
    for line in file:
        print(line)

