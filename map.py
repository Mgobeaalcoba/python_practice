# map: función principal: hacer transformaciones a una lista dada de elementos
# consiste en pasar cada uno de los elementos de una lista por una misma función. 

def run():
    numbers = [1,2,3,4]
    numbers2 = [5,6,7,8]
    numbers_v2 = []

    print(numbers)
    print(numbers2)

    for i in numbers:
        numbers_v2.append(i * 2)

    print(numbers_v2)

    # Hacer lo mismo con map: 

    numbers_v3 = list(map(lambda x : x * 2, numbers))
    print(numbers_v3)

    # A un mismo map le puedo enviar todo los iterables que desee
    # mientras los use en el lambda. Siempre tomara el iterable mas chico
    # como parametro para el resultante: 

    numbers_v3 = list(map(lambda x, y : x + y, numbers, numbers2))
    print(numbers_v3)

if __name__ == '__main__':
    run()
