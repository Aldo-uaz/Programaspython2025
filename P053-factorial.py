# Calcular el factorial de un numero entero

import os;
os.system('cls')

print('Calcuala e imprime el factorial de un numero entero')
n = int(input('Dame un numero entero: '))

f=1
sec = ' '
for i in range(1, n+1):
    f = f * i
    sec = sec + str(i)
    if i < n:
        sec = sec + ' * ' # ppara que no imprima el ultimo numero con * por eso se hace eso
print(f'{n}! = {sec} = {f}')