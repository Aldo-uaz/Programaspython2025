# Calcular el area de un circulo

import math

print('Calculando el area de un circulo')

print('Dame el radio del circulo: ')
radio = float(input())

# area = 3.1416 * radio * radio
area = math.pi*math.pow(radio,2)

print(f'El circulo de radio {radio} tiene un area de {area:,.4f}')
