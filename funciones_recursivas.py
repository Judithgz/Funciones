print('*** Imprimir del 1 al 5 de forma recursiva ***')

# Definir la funcion recursiva
def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero, end=' ') # 1 2 3 4 5
    else:  # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')

# Programa principal
funcion_recursiva(5)

print('\n\nAl reves')
# Al reves
def funcion_recursiva2(numero):
    # Caso Base
    if numero == 1:
        print(numero, end=' ') # 1 2 3 4 5
    else:  # Caso recursivo
        print(numero, end=' ')
        funcion_recursiva(numero - 1)

funcion_recursiva2(5)