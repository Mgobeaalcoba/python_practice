def run():
    numbers = []
    for element in range(1,11):
        numbers.append(element * 2)
    print(numbers)

    # Con list comprehension puedo hacer lo mismo en una linea de codigo: 

    numbers_2 = [element * 2 for element in range(1,11)]
    print(numbers_2)

    # Puedo ponerle condiciones a la creación de mi lista también. Las mismas van luego del ciclo for. 

    numbers_3 = [element * 2 for element in range(1,101) if element % 3 == 0] # Crea una lista con todos los elementos multiplicados por 2, del 1 al 100 que sean divisibles por 3. 
    print(numbers_3)

    # Lo mismo sin list comprehensions sería así: 

    numbers_4 = []
    for i in range(1,101):
        if (i * 2) % 3 == 0:
            numbers_4.append(i*2)
    print(numbers_4)



if __name__ == '__main__':
    run()