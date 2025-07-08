print('*** Sistema de Inventarios (Con Funciones)***')

# Inventario del almacen
inventario = [
    {'id':1, 'nombre':'Camisa', 'precio': 25.99, 'cantidad':50},
    {'id':2, 'nombre':'Pantalones', 'precio': 39.99, 'cantidad':30},
    {'id':3, 'nombre':'Zapatos', 'precio': 49.99, 'cantidad':20}
]

def mostrar_invetario():
    print('--- Inventario del Almacen ---')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
              f'Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}')


def agregar_producto():
    # pass
    print('--- Agregar Nuevo Producto ---')
    id = int(input('Id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id': id, 'nombre':nombre,
                      'precio':precio, 'cantidad':cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')


def buscar_producto():
    print('--- Buscar Producto Por ID ---')
    id_buscar = int(input('Ingresa el id a buscar: '))
    for producto in inventario:
        if producto.get('id') == id_buscar:
            print('\nInformacion del producto encontrado: ')
            print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
                  f'Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}')
            return
    print('\n Producto no encontrado')

# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n--- Menú ---
            1. Mostrar Inventario
            2. Agregar nuevo producto
            3. Buscar producto por ID
            4. Salir''')
        opcion = int(input("Selecciona una opcion (1-4): "))
        # Revisamos las opciones del menu
        if opcion == 1: # Mostrar el inventario
            mostrar_invetario()
        elif opcion == 2: # Agregar un nuevo producto
            agregar_producto()
        elif opcion == 3: # Buscar producto por id
            buscar_producto()
        elif opcion == 4: # Salir
            print('Hasta luego!')
            break
        else:
            print('Opcion invalida')


