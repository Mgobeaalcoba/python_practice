with open('./text.txt', "r+") as file:
    for line in file:
        print(line)

    # tambien puedo escribir en mi archivo: 
    # debo cambiar el permiso en el open a "w" o "r+"
    file.write('\nnuevas cosas en mi archivo')

# Si hago lo mismo pero cambiando el permiso a 'w+' entonces
# voy a estar reemplazando el contenido de mi archivo por el 
# que estoy escribiendo. 