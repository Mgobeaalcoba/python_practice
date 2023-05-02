## Una función recursiva es una función que se llama a si misma: 

def factorial(n):
    """Calcula el factorial de n.

    n int > 0
    returns n!
    """

    if n == 1:
        return 1

    return n * factorial(n - 1)

# Otro ejemplo de recursividad es fibonacci: 

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def run():
    num = int(input("Ingrese el numero del cual quiere obtener el factorial: "))
    print(f'El factorial de {num} es {factorial(num)}')

if __name__ == "__main__":
    run()