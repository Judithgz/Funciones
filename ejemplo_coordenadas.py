print('*** Obtener Coordenadas x, y, z ***')

def obtener__coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z # Aqui se crea una tupla por default

# Llamar la funcion
resultado = obtener__coordenadas()
print(resultado)

# Unpacking de la tupla
x1, y1, z1 = resultado
print(f'Coordenada x = {x1}, Coordenada y = {y1}, Coordenada z = {z1}')
