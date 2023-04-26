import random

def run():
    countries = ['col','mex','bol','pe']
    population = { country : random.randint(20000000, 100000000) for country in countries }
    print(population)

    # Challenge: generar otro diccionario pero con los paises que tengan un población mayor a 50000000

    population_2 = { country : people for country, people in population.items() if people > 50000000 }

    print(population_2)

    # En python los strings son iterables. Por lo que puedo usarlos para construir diccionarios:

    text = "Hola, soy Mariano Gobea"
    unique = { letra : letra.upper() for letra in text}

    print(text)
    print(unique)

    # Puedo filtrar que letras sumar a mi diccionario de la siguiente forma: 

    unique_2 = { letra : letra.upper() for letra in text if letra in 'aeiouAEIOU'}

    print(unique_2)

if __name__ == '__main__':
    run()