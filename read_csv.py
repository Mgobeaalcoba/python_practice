import csv

def read_csv(path):
    new_list = []
    new_list_dict = []
    dict_line = {}
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Agrego cada lista de mi objeto reader a new_list:
        for row in reader:
            new_list.append(row)    
        # Construyo un dict con clave = primer valor de new_list, 
        # valor = cada uno de los siguiente valores de mi lista
        # luego agrega mi dict a una lista de dict:
        for i in range(1,len(new_list)):
            for j in range(0,len(new_list[i])):
                dict_line[new_list[0][j]] = new_list[i][j]
            new_list_dict.append(dict_line)
            dict_line = {}
        # Itero mi lista de dict para imprimir cada linea con el
        # formato deseado: 
        for dict in new_list_dict:
            print("***" * 5)
            print(dict)

def read_csv2(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            # print(list(iterable)) # imprime tuplas con par key, value
            country_dict = {key: value for key, value in iterable}
            # print(country_dict) # en lugar de guardar la lista la voy imprimiendo...
            data.append(country_dict)
        return data

if __name__ == '__main__':
    data = read_csv2('./world_population.csv')
    print(data)

# Cada fila se imprime como un array: 

'''
***************
['Rank', 'CCA3', 'Country/Territory', 'Capital', 'Continent', '2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']
***************
['36', 'AFG', 'Afghanistan', 'Kabul', 'Asia', '41128771', '38972230', '33753499', '28189672', '19542982', '10694796', '12486631', '10752971', '652230', '63.0587', '1.0257', '0.52']
***************
['138', 'ALB', 'Albania', 'Tirana', 'Europe', '2842321', '2866849', '2882481', '2913399', '3182021', '3295066', '2941651', '2324731', '28748', '98.8702', '0.9957', '0.04']
'''

# Reto transformar nuestra lista en un diccionario. Resuelto arriba

# Otra forma de resolverlo es armando tuplas con zip (resolución del profesor):

