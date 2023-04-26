import functools

def run():
    numbers = [1,2,3,4]

    # pasemos la misma lambda a una func normal para entenderla mejor:
    def accum(counter, item):
        print(f'counter: {counter}')
        print(f'item: {item}')
        return counter + item
    
    total = functools.reduce(accum, numbers)
    print(total)

if __name__ == '__main__':
    run()
    # Reduce tota un iterable y reduce el mismo a un solo valor
    # en función de la función que le pasemos como parametro
    # ejs: suma de los valores, el mayor de los valores, el avg, etc