def run():
    mySet = {1,1,2,2,2,3,4,4,4,3,6,7,8}
    print(mySet)
    size = len(mySet) # Mido el tamaño de un set

    set_countries = {'col', 'mex', 'bol'}

    print(set_countries)

    print(size)
    print('col' in set_countries) # Verifico si existe el elemento 'col' en el set
    print('pe' in set_countries) # Verifico si existe el elemento 'pe' en el set

    # add 

    set_countries.add('pe')
    print('pe' in set_countries) # Verifico si existe el elemento 'pe' en el set

    # update

    set_countries.update({'ar','ecua','pe'})
    print(set_countries)

    #remove

    set_countries.remove('col')
    print(set_countries)

    # Si elimino un elemento que no existe python directamente va a lanzarme un error: 

    # set_countries.remove('arg') # arrojará error. 

    # Si quiero eliminar solo si existe debo usar el metodo .discard

    set_countries.discard('arg')

    # Si lo que deseo es eliminar todo el conjunto o set entonces debo usar .clear()

    set_countries.clear()

    print(set_countries)

if __name__ == '__main__':
    run()