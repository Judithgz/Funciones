print('*** Calculadora Con Funciones ***')

def mostrar_menu():
    print(f'''--- Operaciones que puedes realizar ---
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir ''')
    opcion = int(input("Escoge una opcion: "))
    return opcion

def pedir_valores():
    num1 = float(input('Dame el valor 1: '))
    num2 = float(input('Dame el valor 2: '))
    return num1, num2


def ejecutar_operacion(opcion, salir):
    # Solicitar los valores de los numeros
    if 1 <= opcion <= 4:
        num1, num2 = pedir_valores()
    resultado = 0
    if opcion == 1: # Sumar
        resultado = num1 + num2
        print(f'El resultado de la suma es: {resultado}\n')
    elif opcion == 2: # Resta
        resultado = num1 - num2
        print(f'El resultado de la resta es: {resultado}\n')
    elif opcion == 3: # Multiplicacion
        resultado = num1 * num2
        print(f'El resultado de la multiplicacion es: {resultado}\n')
    elif opcion == 4: # Division
        resultado = num1 / num2
        print(f'El resultado de la division es: {resultado}\n')
    elif opcion == 5:
        print('Saliendo, hasta luego!')
        salir = True
    else:
        print('Opcion invalida\n')
        return salir

# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)


