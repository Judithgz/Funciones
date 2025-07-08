print('*** Calcular Potencia De Un Numero Con Funcion Recursiva ***')

def potencia_numero(base,exponente):
    # Caso base
    if exponente == 0:
        return 1
    else: # Caso recursivo
        return base * potencia_numero(base, exponente-1)

print(f'2 Elevado a la 3 = {potencia_numero(2,3)}')
print(f'5 Elevado a la 0 = {potencia_numero(5,0)}')

