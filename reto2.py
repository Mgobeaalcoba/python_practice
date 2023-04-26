# Seleccionar solo los paises como clave y la World Population Percentage
# como valor y hacer un pie con ello.

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import csv

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable if key in 
                            ('Country/Territory','World Population Percentage')}
            data.append(country_dict)
        return data
    
def do_list(list_dict):
    labels = []
    values = []
    for dict in list_dict:
        labels.append(dict["Country/Territory"])
        values.append(dict["World Population Percentage"])
    return labels, values
    
if __name__ == '__main__':
    data = read_csv('./world_population.csv')
    labels, values = do_list(data)
    generate_pie_chart(labels= labels, values= values)