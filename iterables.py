# for in range
for i in range(1,11):
    print(i)

# un iterable en python: 
my_iter = iter(range(1,11))
print(my_iter)

# un iterador puede ser ejecutado de forma controlada: 
print(next(my_iter)) #1
print(next(my_iter)) #2
print(next(my_iter)) #3
print(next(my_iter)) #4

# es importante entender esto para leer archivos. 
# si sigo luego del maximo lanza una excepción del tipo 
# stop iteration