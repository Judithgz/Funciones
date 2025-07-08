print('*** Imprimir detalles de una persona usando kwargs ***')

# Funcion que acepta argumentos variables en forma de key-value dict
def detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for key, value in kwargs.items():
        print(f'{key}:{value}')

# Llamar a la funcion
detalle_persona(nombre='Judith', edad=24, ciudad='Cancun')
detalle_persona(nombre = 'Isaar', edad=34, ciudad='Cancun', puesto = 'Gerente')