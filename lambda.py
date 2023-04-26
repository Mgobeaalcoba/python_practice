def increment(x):
    return x + 1

# Misma función con lambda function: 

increment2 = lambda x : x + 1

# Función lambda que recibe dos argumentos: 

full_name = lambda name, last_name : f'Full name es {name.title()} {last_name.title()}'

def run():
    print(increment(10))
    print(increment2(10))
    print(full_name("mariano","gobea"))

if __name__ == "__main__":
    run()