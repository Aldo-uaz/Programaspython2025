# Calcualndo el volumen de un cilindro

import math as m
import os; os.system('clear')

print('Calcualndo el volumen de un cilindro dado su radio y su altura')
print('Dame el radio y la altura sepadadas por un enter')
radio, altura = float(input()), float(input())

v = m.pi * (radio * radio)*altura

salida= ('El volumen del cilindro\n'
         f'Con un radio de {radio}\n'
         f'con una altura de {altura}\n'
         f'es de {v:.2f}'
         )

print(f'{salida}')