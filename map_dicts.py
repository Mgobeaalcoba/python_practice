def run(): 
    # Creo una lista de diccionarios: 
    items = [
        {
            'product': 'camisa',
            'price': 100
        },
        {
            'product': 'pantalon',
            'price': 125
        },
                {
            'product': 'short',
            'price': 75
        },
                        {
            'product': 'vestido',
            'price': 190
        }
    ]

    # Como creo a partir de ese diccionario una lista solo de los precios: 

    prices = []
    for element in items:
        prices.append(element["price"])

    print(items)
    print(prices)

    # También lo podría hacer con map: 

    prices2 = list(map(lambda item: item["price"], items))

    print(prices2)

    # Creo nueva función para impuestos que no edita el dict original: 

    items_taxes2 = list(map(taxes2, items))

    print(items_taxes2)
    print(items)

    # Como le sumo el IVA a mi lista de diccionarios con map: 
    # Esto es lo que sucede cuando hacemos una columna calculada en pandas: 
    # No puedo hacerlo con lambda porque me implica mas de una linea de codigo

    # Le sume de plus tipado estatico a python. 
"""     def taxes(product: dict):
        product["taxes"] = product["price"] * 0.21
        return product

    # Observar que acá estoy enviando una función normal al map. 
    items_taxes = list(map(taxes, items))

    print(items_taxes)

    # map no deberia modificar el array original pero en este caso lo hizo: 

    print(items) """

    # Esto tiene que ver con una referencia en memoria y lo vamos a solucionar: 
    # Solución. Hacer una copy de mi dict cuando entra a taxes y trabajar con ella: 

def taxes2(product: dict):
        new_product = product.copy()
        new_product["taxes"] = new_product["price"] * 0.21
        return new_product
    
if __name__ == '__main__':
    run()