# Conversion de una temperatura en grados Celcius a Farenheit

import math as m
import os; os.system('clear')

print('Calcualndo la conversion de una temperatura en grados Celcius a Farenheit')
print('Dame los grados: ')

gc = float(input())
gf = (gc * 9/5) + 32

print(f'Grados {gc} celcius a Grados {gf} farenheit ')