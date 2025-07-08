print('*** Maquina de Snacks ***')

# Snacks en inventario
inventario = [
    {'id':1, 'nombre':'Chips Fuego', 'precio': 30},
    {'id':2, 'nombre':'Cacahuates', 'precio': 20},
    {'id':3, 'nombre':'Palomitas', 'precio': 25}
]

# Carrito
carrito = [

]

def mostrar_snacks():
    print('--- Snacks Disponibles ---')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
              f'Precio: ${producto.get('precio')}')


def comprar_snack():
    id_buscar = int(input('¿Que snack quieres? (ID): '))
    for producto in inventario:
        if producto.get('id') == id_buscar:
            print('\nSnack Agregado: ')
            carrito.append(producto)
            print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
                  f'Precio: ${producto.get('precio')}')
            return
    print('\n Snack no encontrado')

def mostrar_ticket():
    ticket = f'\t--- Ticket de Venta ---'
    total = 0
    for producto in carrito:
        ticket += f'\n\t- {producto.get('nombre')} - ${producto.get('precio')}'
        total += producto.get('precio')
    ticket += f'\n\tTOTAL -> ${total}'
    print(ticket)



# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n--- Menú ---
            1. Mostrar Snacks
            2. Comprar Snack
            3. Mostrar Ticket
            4. Salir''')
        opcion = int(input("Selecciona una opcion (1-4): "))
        # Revisamos las opciones del menu
        if opcion == 1: # Mostrar los snacks
            mostrar_snacks()
        elif opcion == 2: # Comprar un Snack
            comprar_snack()
        elif opcion == 3: # Mostrar ticket
            mostrar_ticket()
        elif opcion == 4: # Salir
            print('Hasta luego!')
            break
        else:
            print('Opcion invalida')