print('*** Suma con argumentos variables ***')

# Funcion sumar que acepta argumentos variables
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Llamams a la funcion sumar
resultado = sumar(1, 2, 3, 4, 5, 12, 19)
print(f'Resultado de la suma: {resultado}')
