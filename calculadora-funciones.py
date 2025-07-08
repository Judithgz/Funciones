print('*** Calculadora Con Funciones ***')

def suma():
    x = int(input('Ingresa el valor 1: '))
    y = int(input('Ingresa el valor 2: '))
    resultado = x + y
    print(f'El resultado de la suma es: {resultado}')

def resta():
    x = int(input('Ingresa el valor 1: '))
    y = int(input('Ingresa el valor 2: '))
    resultado = x - y
    print(f'El resultado de la resta es: {resultado}')

def multiplicacion():
    x = int(input('Ingresa el valor 1: '))
    y = int(input('Ingresa el valor 2: '))
    resultado = x * y
    print(f'El resultado de la multiplicacion es: {resultado}')

def division():
    x = int(input('Ingresa el valor 1: '))
    y = int(input('Ingresa el valor 2: '))
    resultado = x / y
    print(f'El resultado de la division es: {resultado}')

# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n--- Operaciones que puedes realizar ---
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Division
            5. Salir ''')
        opcion = int(input("Escoge una opcion (1-4): "))
        # Revisamos las opciones del menu
        if opcion == 1: # Suma
            suma()
        elif opcion == 2: # Resta
            resta()
        elif opcion == 3: # Multiplicacion
            multiplicacion()
        elif opcion == 4: # Division
            division()
        elif opcion == 5: # Salir
            print('Hasta luego!')
            break
        else:
            print('Opcion invalida')