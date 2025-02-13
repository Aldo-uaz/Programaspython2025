# Calculando la hipotenusa de un triangulo

import math as m
import os; os.system('clear')

print('Calculando la hipotenusa de un triangulo rectangulo con longitudes de sus lados')
print('Dame las dos longitudes separadas por un espacio')
l1,l2 = input().split() # split divide la cadena en partes en base al espacio
l1,l2,= int(l1), int(l2)
hipotenusa = m.sqrt(l1*l1 + l2*l2)
print(f'La hipotenusa del triangulo con las longitudes {l1}, {l2} es de : {hipotenusa}')
