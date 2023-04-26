def find_volume(length = 1, width = 1, depth = 1): #Seteo valores por default para mis parametros
    return length * width * depth

def ungroup(cadena): # Función con multiples returns
    palabra1, palabra2 = cadena.split(" ")
    return palabra1, palabra2

def run():
    result = find_volume() # Envio sin argumentos por lo que usará los dados por default
    result2 = find_volume(10,15,20)

    print(result)
    print(result2)

    string1, string2 = ungroup("Hola Mariano")
    print(string1)
    print(string2)

    # Otra forma de guardar el multiple retorno es identificando el lugar que tienen en la tupla: 

    string3 = ungroup("Hola Dolar")

    print(string3[0])
    print(string3[1])

if __name__ == '__main__':
    run()