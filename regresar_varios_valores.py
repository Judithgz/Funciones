print('*** Regresar una tupla de valores desde una funcion ***')

# Definicion de la funcion
def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta funcion egresa varios valores (tupla)')
    return (nombre.upper(), apellido.upper(), edad)

# Programa principal
nombre, apellido, edad = persona_mayusculas('Sandra', 'Jimenez', 42)
print(f'Resultado: nombre = {nombre}, apellido = {apellido}, edad = {edad}')