print('*** Funcion con argumentos por nombre ***')

def imprimir_persona(nombre, apellido='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Primero llamamos a la funcion pasando los argumentos de manera posicional
imprimir_persona('Judith','Gonzalez',24)

# Llamar la funcion usando argumentos por nombre
imprimir_persona(nombre = 'Isaar', apellido = 'Capistran', edad = 34)

# Llamar la funcion usando argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad=34, apellido='Capistran', nombre='Isaar')

# Argumentos con valor por default
imprimir_persona(nombre='Isaar', apellido='Capistran')
imprimir_persona(apellido='Capistran', nombre='Isaar')