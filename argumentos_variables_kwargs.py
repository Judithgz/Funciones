# *args - argumentos - tupla
# **kwargs - keyword arguments (key, value) como un dict
print('*** Argumentos variables en forma de dict ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas Info: {kwargs}')

# Llamamos la funcion
superheroe_superpoderes('Spiderman', 'Instinto Arácnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Ironman', 'Armadura', 'Playboy', edad=45)

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', personalidad='Buena onda')