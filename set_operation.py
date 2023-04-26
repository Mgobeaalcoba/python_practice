def run():
    set_a = {'col', 'mex', 'bol'}
    set_b = {'pe', 'bol'}

    ## Union de conjuntos: Full join

    set_c = set_a.union(set_b)
    print(set_c)

    # Lo mismo se logra con el operador de union |

    print(set_a | set_b)

    # Intersección de conjuntos trae solo los elementos en comun: Inner join

    set_c = set_a.intersection(set_b)
    print(set_c)

    # También se puede hacer con un operador & esta operación: 

    print(set_a & set_b)

    # Diferencia. Except

    set_c = set_a.difference(set_b)
    print(set_c)

    # Tambien se puede hacer con el operador "-"

    print(set_a - set_b)

    # Diferencia simetrica. Aquello que no coincide entre los dos conjuntos. 

    set_c = set_a.symmetric_difference(set_b)
    print(set_c)

    # Lo mismo se puede hacer con el operador ^

    print(set_a ^ set_b)

if __name__ == '__main__':
    run()