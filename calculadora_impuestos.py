print('*** Calculadora de Impuestos ***')

def calcular_impuestos(sinimpuesto, impuesto):
    resultado = sinimpuesto + sinimpuesto * (impuesto/100)
    return resultado


# Programa principal
if __name__ == '__main__':
    sinimpuesto = float(input('Proporcione el pago sin impuesto: '))
    impuesto = float(input('Proporcione el monto del impuesto: '))
    total = calcular_impuestos(sinimpuesto, impuesto)
    print(f'El pago con impuestos es: {total}')
