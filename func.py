def suma(a,b):
    return a+b

def myPrint3(name):
    print("This is my print", name)
    return True

def myPrint2(name):
    print("This is my print", name)

def myPrint():
    print("This is my print")

def run():
    myPrint()
    myPrint2("Mariano")
    print(myPrint3("Mariano Daniel")) # El print va a imprimir el retorno de mi función
    a = 2
    b = 3
    print(suma(a,b))

if __name__ == '__main__':
    run()