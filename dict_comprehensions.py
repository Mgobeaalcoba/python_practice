import random

def run():
    # Completo diccionario en varias lineas: 

    dict = {}
    for i in range(1,11):
        dict[i] = i * 2 # La primera parte agrega la key y la segunda el value

    print(dict)

    # Con dict comprehensions: 

    dict_2 = { i : i * 2 for i in range(1, 5) }
    print(dict_2) 

    # Otra ejemplo: 

    countries = ['col','mex','bol','pe']
    population = {}
    for country in countries:
        population[country] = random.randint(20000000, 100000000)

    print(population)

    # Itero un diccionario e imprimo por par clave valor. 

    for country, people in population.items():
        print(country, " = ", people )

    # Puedo crear el mismo dict population con dict comprehensions así: 

    population = { country : random.randint(20000000, 100000000) for country in countries }
    print(population)

    for country, people in population.items():
        print(country, " = ", people )

    # Challenge: Armar un diccionario iterando dos listas: 

    names = ["nico", "zule", "santi"]
    ages = [12, 56, 68]

    myDict = {}
    for i in range(len(names)):
        myDict[names[i]] = ages[i]

    print(myDict)

    ## Ahora con dict comprehensions:

    myDict = { names[i] : ages[i] for i in range(len(names)) } 
    print(myDict)

    # Unimos usando zip

    print(list(zip(names,ages)))

    myDict = {}
    for name, age in zip(names, ages):
        myDict[name] = age

    print("Dict armado con zip: ")
    print(myDict)

    myDict = { name : age for name, age in zip(names, ages)}

    print(myDict)

if __name__ == '__main__':
    run()