# Cargar el CSV de world population, quedarme con un país, y su info
# de población año a año para poderlo graficar en un bar chart. Sin 
# usar pandas, pero si matplotlib: 

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import csv

def generate_bar_chart(labels, values):
    values_int = []
    for value in values[1:]:
        values_int.append(int(value))
    fig, ax = plt.subplots()
    ax.bar(labels[1:],values_int,)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x)}'))
    ax.invert_xaxis()
    plt.xticks(np.arange(8) ,("2022","2020","2015","2010","2000","1990","1980","1970"), rotation=45)
    plt.title(f'Evolución poblacional de {values[0]}')
    plt.show()

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable if key in 
                            ('Country/Territory','2022 Population','2020 Population',
                             '2015 Population','2010 Population','2000 Population',
                             '1990 Population','1980 Population','1970 Population')}
            data.append(country_dict)
        return data
    
if __name__ == '__main__':
    data = read_csv('./world_population.csv')
    generate_bar_chart(labels = list(data[8].keys()), values= list(data[8].values()))
